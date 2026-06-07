# TalentLens AI Candidate Ranker

## Overview

TalentLens AI is a hybrid AI-powered candidate ranking system that combines rule-based scoring with semantic embeddings to identify the best-fit candidates for specialized AI/ML roles. 

**Submission includes:**
- **GitHub Repository**: Complete working code, frontend, and backend
- **Approach PDF**: [APPROACH.pdf](APPROACH.pdf) — detailed explanation of the ranking algorithm and methodology
 - **Approach PDF**: [APPROACH.pdf](ai-candidate-ranker/Frontend/src/APPROACH.pdf) — detailed explanation of the ranking algorithm and methodology
- **Ranked Output**: `output/submission.csv` — top 100 ranked candidates

---

## Problem Statement

Recruiters often review hundreds of candidate profiles and may miss highly relevant candidates for specialized AI/ML roles.

This project builds a candidate ranking system that analyzes candidate profiles, reads the job description, and ranks candidates based on their fit for the role.

The system processes candidate data, assigns a relevance score, and generates a ranked submission file.

## Data Sets

The code uses the provided dataset and job description to compute candidate fit.
- Candidate data: `ai-candidate-ranker/data/candidates.jsonl`
- Job description: `ai-candidate-ranker/data/job_description.docx`
- Generated ranked output: `output/submission.csv`

Challenge dataset link:

[Click Here](https://drive.google.com/file/d/1MfD47XvVdRKBGRAyzGOxDCEf2ve96Jjo/view?usp=drive_link)

The backend ranking algorithm reads the job description file and weights candidates based on relevance to the role, including retrieval, embeddings, ranking, LLM, product, startup, and production deployment signals.

---

## Approach

The ranking model uses a weighted scoring system based on four major factors:

### 1. Job Title Matching

Candidates receive higher scores if their current title aligns with AI/ML-related roles such as:

- AI Engineer
- ML Engineer
- Applied ML Engineer
- Search Engineer
- NLP Engineer
- Recommendation Systems Engineer
- Data Scientist

Non-relevant titles such as Accountant, Marketing, HR, Sales, etc. receive penalties.

---

### 2. Experience

Candidates with experience levels closer to the target range receive additional points.

Preferred experience range:

- 5–9 years

Acceptable experience range:

- 4–11 years

---

### 3. Skills Matching

The model rewards candidates possessing skills relevant to the job description, including:

- RAG
- Embeddings
- Semantic Search
- Vector Search
- Information Retrieval
- Pinecone
- FAISS
- Milvus
- Qdrant
- Weaviate
- Elasticsearch
- OpenSearch
- BM25
- Learning to Rank
- Recommendation Systems
- Sentence Transformers
- LLMs
- LoRA
- Fine-Tuning LLMs

---

### 4. Career History Analysis

The strongest signal comes from previous work experience.

The model searches job history descriptions for evidence of:

- Recommendation Systems
- Ranking Systems
- Semantic Search
- Retrieval Systems
- Learning-to-Rank
- Embeddings
- Vector Search
- Pinecone
- FAISS
- Milvus
- Qdrant
- BM25
- Production Deployments
- Evaluation Metrics
- Search Relevance Optimization

Candidates with hands-on experience building ranking, search, retrieval, or recommendation systems receive significantly higher scores.

---

### 5. Recruiter Signals

Additional signals used:

- Open To Work
- Response Rate
- Search Appearance Frequency

These signals help prioritize candidates who are both relevant and more likely to engage with recruiters.

---

## Project Structure

AI_Candidate_Ranker/
│
├── data/
│   ├── candidate_schema.json
│   ├── candidates.jsonl
│   ├── job_description.docx
│   └── sample_submission.csv
│
├── output/
│   └── submission.csv
│
├── src/
│   ├── rank_candidates.py
│   └── validate_top20.py
│
├── README.md
└── venv/

## How to Run

Move into the backend source folder:

```bash
cd ai-candidate-ranker/Backend/src
```

Run the ranking script:

```bash
python rank_candidates.py
```

This generates the ranked output file:

```text
output/submission.csv
```

### Frontend dashboard

The React dashboard loads the `submission.csv` file from `ai-candidate-ranker/Frontend/public/submission.csv`.
If you want to preview the latest results, copy the generated file into the frontend public directory:

```bash
cp output/submission.csv ai-candidate-ranker/Frontend/public/submission.csv
```

Then start the dashboard:

```powershell
cd c:\Users\acer\OneDrive\Desktop\AI_Candidate_Ranker\ai-candidate-ranker
npm install
npm run preview
```

Open the app in your browser at the local preview link shown by Vite.

For example:

```text
http://localhost:4173
```

The dashboard includes:

- `Home`: shows the loaded file and row count
- `Input`: explains the source file and loading status
- `Explore`: search the dataset and display only matching rows
- `Full Output`: shows the complete ranked output
- `Assistant`: chatbot-style candidate insights

---

## Output

The ranking script generates:

```text
output/submission.csv
```

Format:

```csv
candidate_id,rank,score
CAND_0018499,1,390
CAND_0030953,2,370
CAND_0092278,3,365
...
```

The file contains the ranked candidates sorted by relevance score. Copy that file into `ai-candidate-ranker/Frontend/public/submission.csv` to make the frontend show the correct full output.

---

## Scoring Philosophy

The scoring system prioritizes:

1. Relevant AI/ML job titles
2. Search, Retrieval, and Recommendation experience
3. Matching technical skills
4. Appropriate experience level
5. Recruiter engagement signals

The objective is to surface candidates most likely to succeed in AI-powered search, recommendation, and ranking-related roles.

---

## Result

The system produces a ranked list of candidates and exports the top candidates into the required submission format for evaluation.