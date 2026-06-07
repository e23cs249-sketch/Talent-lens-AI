import { motion } from "framer-motion";

export default function Table({ data }) {
  if (!data.length) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        className="card empty-state"
      >
        No candidate shortlist loaded yet.
      </motion.div>
    );
  }

  const cols = Object.keys(data[0]);

  return (
    <motion.section
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      className="card table-panel"
    >
      <div className="table-header">
        <div>
          <p className="eyebrow">Ranked shortlist</p>
          <h3>Candidate ranking table</h3>
        </div>
      </div>

      <div className="table-scroll">
        <table className="rank-table">
          <thead>
            <tr>
              {cols.map((column) => (
                <th key={column}>{column.toUpperCase()}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={`${row.candidate_id}-${index}`} className={index < 3 ? "highlight-row" : ""}>
                {cols.map((column) => (
                  <td key={`${column}-${index}`}>
                    {column === "rank" ? (
                      <span className="badge">{row[column]}</span>
                    ) : column === "score" ? (
                      <strong>{row[column]}</strong>
                    ) : (
                      row[column]
                    )}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </motion.section>
  );
}
