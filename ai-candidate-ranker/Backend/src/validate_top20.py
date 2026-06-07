import json

top_ids = [
"CAND_0018499",
"CAND_0071974",
"CAND_0009691",
"CAND_0005649",
"CAND_0050876",
"CAND_0041669",
"CAND_0077337",
"CAND_0088025",
"CAND_0046064",
"CAND_0061339"
]

with open("../data/candidates.jsonl","r",encoding="utf-8") as f:

    for line in f:

        c = json.loads(line)

        if c["candidate_id"] in top_ids:

            print("\n"+"="*80)
            print(c["candidate_id"])

            print(
                "TITLE:",
                c["profile"].get("current_title")
            )

            print(
                "EXP:",
                c["profile"].get("years_of_experience")
            )

            print(
                "OPEN:",
                c["redrob_signals"].get("open_to_work_flag")
            )

            print(
                "RESPONSE:",
                c["redrob_signals"].get(
                    "recruiter_response_rate"
                )
            )

            print("\nSKILLS")

            for s in c.get("skills",[])[:15]:
                print("-",s["name"])