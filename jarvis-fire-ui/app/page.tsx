"use client";

import { useState } from "react";
import { askJarvis } from "../lib/api";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleAsk() {
    if (!question) return;

    try {
      setLoading(true);

      const data = await askJarvis(question);

      setResponse(
        data.response ||
        data.answer ||
        JSON.stringify(data, null, 2)
      );
    } catch (error) {
      console.error(error);
      setResponse("Error talking to Jarvis.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main
      style={{
        minHeight: "100vh",
        backgroundColor: "black",
        color: "white",
        padding: "40px",
        fontFamily: "Arial",
      }}
    >
      <h1
        style={{
          fontSize: "56px",
          marginBottom: "20px",
        }}
      >
        Jarvis Fire Inspector
      </h1>

      <p
        style={{
          color: "#9ca3af",
          fontSize: "20px",
          marginBottom: "30px",
        }}
      >
        AI-powered fire inspection assistant.
      </p>

      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask Jarvis a fire code or inspection question..."
        style={{
          width: "100%",
          maxWidth: "900px",
          height: "140px",
          padding: "20px",
          borderRadius: "16px",
          backgroundColor: "#18181b",
          color: "white",
          border: "1px solid #333",
          fontSize: "18px",
          marginBottom: "20px",
        }}
      />

      <br />

      <button
        onClick={handleAsk}
        disabled={loading}
        style={{
          backgroundColor: "#dc2626",
          color: "white",
          fontSize: "24px",
          padding: "18px 36px",
          borderRadius: "16px",
          border: "none",
          cursor: "pointer",
          marginBottom: "40px",
        }}
      >
        {loading ? "Thinking..." : "Ask Jarvis"}
      </button>

      {response && (
        <div
          style={{
            marginTop: "30px",
            backgroundColor: "#18181b",
            padding: "30px",
            borderRadius: "20px",
            maxWidth: "1000px",
            whiteSpace: "pre-wrap",
            lineHeight: "1.7",
            fontSize: "18px",
          }}
        >
          {response}
        </div>
      )}
    </main>
  );
}