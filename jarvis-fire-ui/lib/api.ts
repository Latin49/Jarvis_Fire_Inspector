const API_BASE_URL = "https://jarvis-fire-inspector.onrender.com";

export async function askJarvis(question: string) {
  const response = await fetch(`${API_BASE_URL}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question,
    }),
  });

  if (!response.ok) {
    throw new Error("Jarvis API request failed");
  }

  return response.json();
}