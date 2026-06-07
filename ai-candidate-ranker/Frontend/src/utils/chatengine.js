import { analyzeData } from "./analyzeData";

export function getAIResponse(question, data) {
  const insights = analyzeData(data);

  if (!insights) return "Upload data first.";

  const q = question.toLowerCase();

  if (q.includes("average")) {
    return `The average score is ${insights.avg}.`;
  }

  if (q.includes("highest") || q.includes("top")) {
    return `The highest score is ${insights.max}. Top candidate: ${insights.topRow.candidate_id} (rank ${insights.topRow.rank}).`;
  }

  if (q.includes("lowest")) {
    return `The lowest score is ${insights.min}.`;
  }

  if (q.includes("candidate")) {
    return `The top candidate is ${insights.topRow.candidate_id} with score ${insights.topRow.score}.`;
  }

  return "Ask about average, highest, lowest, or the top candidate in the dataset.";
}
