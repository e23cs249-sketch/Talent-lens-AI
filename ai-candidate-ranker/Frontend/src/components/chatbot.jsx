import { useState } from "react";
import { motion } from "framer-motion";
import { getAIResponse } from "../utils/chatEngine";

export default function ChatBot({ data }) {
  const [messages, setMessages] = useState([
    { role: "bot", text: "Hi! Ask me anything about your candidate shortlist." }
  ]);

  const [input, setInput] = useState("");

  const send = (event) => {
    event?.preventDefault?.();
    const trimmed = input.trim();
    if (!trimmed) return;

    const userMsg = { role: "user", text: trimmed };
    const botMsg = {
      role: "bot",
      text: getAIResponse(trimmed, data)
    };

    setMessages((prev) => [...prev, userMsg, botMsg]);
    setInput("");
  };

  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="card chat-panel"
    >
      <div className="chat-header">
        <div>
          <span className="eyebrow">AI Assistant</span>
          <h3>Ask the dataset</h3>
        </div>
      </div>

      <div className="chat-history">
        {messages.map((m, i) => (
          <div key={i} className={m.role === "user" ? "chat-bubble user" : "chat-bubble bot"}>
            {m.text}
          </div>
        ))}
      </div>

      <form className="chat-actions" onSubmit={send}>
        <input
          className="chat-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask: top score? average? best candidate?"
        />
        <button type="submit" className="button button-primary">
          Send
        </button>
      </form>
    </motion.section>
  );
}
