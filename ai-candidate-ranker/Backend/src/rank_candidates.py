import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
OUTPUT_FILE = ROOT / "output" / "submission.csv"

INPUT_FILE = DATA_DIR / "candidates.jsonl"
JOB_DESCRIPTION_TXT = DATA_DIR / "job_description.txt"
JOB_DESCRIPTION_DOCX = DATA_DIR / "job_description.docx"
TOP_K = 100

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

AI_TITLES = [
    "ai engineer",
    "ml engineer",
    "machine learning engineer",
    "applied ml engineer",
    "nlp engineer",
    "search engineer",
    "recommendation systems engineer",
    "data scientist",
    "ai specialist",
    "senior ai engineer",
    "senior machine learning engineer",
    "senior data scientist",
    "staff machine learning engineer",
]

BAD_TITLES = [
    "marketing",
    "hr",
    "accountant",
    "sales",
    "graphic designer",
    "content writer",
    "customer support",
    "operations manager",
]

CORE_SKILLS = [
    "embeddings",
    "semantic search",
    "vector search",
    "information retrieval",
    "retrieval",
    "rag",
    "faiss",
    "pinecone",
    "milvus",
    "qdrant",
    "weaviate",
    "opensearch",
    "elasticsearch",
    "bm25",
    "learning to rank",
    "recommendation systems",
    "sentence transformers",
    "llms",
    "fine-tuning llms",
    "lora",
]

JD_PHRASE_WEIGHTS = {
    "embeddings": 15,
    "retrieval": 15,
    "semantic search": 15,
    "ranking": 15,
    "hybrid retrieval": 12,
    "llm": 12,
    "fine-tuning": 12,
    "bm25": 10,
    "production": 12,
    "deployed": 12,
    "evaluation": 10,
    "benchmark": 10,
    "metrics": 8,
    "product": 8,
    "startup": 8,
    "shipper": 10,
    "researcher": 6,
    "recruiter": 8,
}

results = []


def normalize_text(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def load_job_description_text():
    txt_path = Path(JOB_DESCRIPTION_TXT)
    if txt_path.exists():
        return normalize_text(txt_path.read_text(encoding="utf-8"))

    docx_path = Path(JOB_DESCRIPTION_DOCX)
    if docx_path.exists():
        with zipfile.ZipFile(docx_path, "r") as docx:
            xml = docx.read("word/document.xml").decode("utf-8")
        text = " ".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml))
        return normalize_text(text)

    return ""


job_description = load_job_description_text()


def candidate_text(profile, skills, history):
    history_text = []
    for job in history:
        history_text.append(job.get("title", ""))
        history_text.append(job.get("description", ""))

    parts = [
        profile.get("current_title", ""),
        " ".join(skills),
        " ".join(history_text),
        profile.get("summary", ""),
    ]
    return normalize_text(" ".join(parts))


def apply_job_description_match(candidate_text_unit):
    if not job_description:
        return 0

    score = 0
    for phrase, weight in JD_PHRASE_WEIGHTS.items():
        if phrase in job_description and phrase in candidate_text_unit:
            score += weight

    if ("5-9" in job_description or "5–9" in job_description or "5 - 9" in job_description) and "years of experience" in job_description:
        score += 5

    if "pure research" in job_description and "production" not in candidate_text_unit and "deployed" not in candidate_text_unit:
        score -= 5

    return score


with open(INPUT_FILE, "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        score = 0

        profile = candidate.get("profile", {})
        title = profile.get("current_title", "").lower()
        years = profile.get("years_of_experience", 0)

        skills = [
            s.get("name", "").lower()
            for s in candidate.get("skills", [])
        ]

        history = candidate.get("career_history", [])
        signals = candidate.get("redrob_signals", {})

        # ------------------
        # TITLE MATCH
        # ------------------

        if any(t in title for t in AI_TITLES):
            score += 40

        if any(t in title for t in BAD_TITLES):
            score -= 60

        # ------------------
        # EXPERIENCE
        # ------------------

        if 5 <= years <= 9:
            score += 25
        elif 4 <= years <= 11:
            score += 15

        # ------------------
        # SKILLS
        # ------------------

        for skill in skills:
            for target in CORE_SKILLS:
                if target in skill:
                    score += 5

        # ------------------
        # CAREER HISTORY
        # ------------------

        for job in history:

            job_title = job.get("title", "").lower()
            desc = job.get("description", "").lower()

            if "search engineer" in job_title:
                score += 30

            if "recommendation" in job_title:
                score += 35

            if "nlp engineer" in job_title:
                score += 25

            if "applied ml engineer" in job_title:
                score += 25

            if "machine learning engineer" in job_title:
                score += 25

            if "ai engineer" in job_title:
                score += 25

            if "data scientist" in job_title:
                score += 15

            keywords = [
                "recommendation",
                "ranking",
                "retrieval",
                "semantic search",
                "vector search",
                "embeddings",
                "learning to rank",
                "sentence-transformer",
                "pinecone",
                "milvus",
                "qdrant",
                "faiss",
                "bm25",
                "ndcg",
                "mrr",
                "map",
                "evaluation",
                "production",
                "deployed",
            ]

            for kw in keywords:
                if kw in desc:
                    score += 10

        # ------------------
        # JOB DESCRIPTION MATCH
        # ------------------

        candidate_content = candidate_text(profile, skills, history)
        score += apply_job_description_match(candidate_content)

        # ------------------
        # RESPONSE RATE
        # ------------------

        response_rate = signals.get("response_rate", 0)
        score += response_rate * 20

        # ------------------
        # OPEN TO WORK
        # ------------------

        if signals.get("open_to_work", False):
            score += 10

        # ------------------
        # SEARCH APPEARANCE
        # ------------------

        appearances = signals.get(
            "search_appearance_30d",
            0
        )

        score += min(appearances / 20, 15)

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(score, 2),
            "title": profile.get(
                "current_title",
                "Unknown"
            ),
        })

# ------------------
# SORT
# ------------------

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 20 CANDIDATES\n")

for i, c in enumerate(results[:20], start=1):
    print(
        f"{i}. {c['candidate_id']} | "
        f"{c['title']} | "
        f"Score={c['score']}"
    )

# ------------------
# SUBMISSION FILE
# ------------------

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write("candidate_id,rank,score\n")

    for rank, c in enumerate(
        results[:TOP_K],
        start=1
    ):
        f.write(
            f"{c['candidate_id']},"
            f"{rank},"
            f"{c['score']}\n"
        )

print(f"\n{OUTPUT_FILE} generated successfully.")