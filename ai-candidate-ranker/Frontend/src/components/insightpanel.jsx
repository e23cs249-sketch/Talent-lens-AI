import { motion } from "framer-motion";
import { analyzeData } from "../utils/analyzeData";

export default function InsightPanel({ data }) {
  const insights = analyzeData(data);

  if (!insights) return null;

  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="card insight-card"
    >
      <div className="insight-header">
        <div>
          <span className="eyebrow">Insight engine</span>
          <h3>Score summary</h3>
        </div>
      </div>

      <div className="insight-grid">
        <div className="metric-card">
          <span>Average score</span>
          <strong>{insights.avg}</strong>
        </div>

        <div className="metric-card">
          <span>Highest score</span>
          <strong>{insights.max}</strong>
        </div>

        <div className="metric-card">
          <span>Lowest score</span>
          <strong>{insights.min}</strong>
        </div>
      </div>

      <div className="top-candidate-card">
        <span className="eyebrow">Top ranked candidate</span>
        <h4>{insights.topRow.candidate_id}</h4>
        <p>
          Rank {insights.topRow.rank} with a score of {insights.topRow.score}. This is the strongest candidate in your current shortlist.
        </p>
      </div>
    </motion.section>
  );
}
