import { motion } from "framer-motion";

export default function Header() {
  return (
    <motion.header
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      className="hero-card hero-header"
    >
      <div>
        <span className="eyebrow">TalentLens AI</span>
        <h1>TalentLens Candidate Insights</h1>
        <p>
          TalentLens AI is building an intelligent candidate discovery platform that goes beyond keyword matching.
          Using semantic understanding, behavioral signals, and explainable AI, we help recruiters identify the best-fit talent faster and more accurately.
        </p>
      </div>

      <div className="hero-pill">
        <strong>Designed to win</strong>
        <p>Intelligent shortlist review, faster insights, and polished finalist-ready output.</p>
      </div>
    </motion.header>
  );
}
