const API_KEY = "AIzaSyDBs3Sg-Pv4zv6Vlb4TFMhAy0XVOLBd-Oo";

async function generateOutfit(promptText) {
  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        contents: [
          {
            parts: [{ text: promptText }]
          }
        ]
      }),
    }
  );

  if (!response.ok) {
    throw new Error("API request failed");
  }

  const data = await response.json();

  if (
    data.candidates &&
    data.candidates.length > 0 &&
    data.candidates[0].content &&
    data.candidates[0].content.parts &&
    data.candidates[0].content.parts.length > 0
  ) {
    return data.candidates[0].content.parts[0].text;
  } else {
    throw new Error("Invalid response format");
  }
}

document
  .getElementById("fashionForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const resultElement = document.getElementById("result");
    resultElement.innerText = "Generating outfit... 👗✨";

    const gender = document.getElementById("gender").value;
    const occasion = document.getElementById("occasion").value;
    const color = document.getElementById("color").value;
    const budget = document.getElementById("budget").value;

    const prompt = `
You are a professional fashion stylist.

Suggest a complete outfit for:
Gender: ${gender}
Occasion: ${occasion}
Preferred Color: ${color}
Budget: ${budget}

Give:
1. Outfit
2. Accessories
3. Footwear
4. Styling Tips
`;

    try {
      const result = await generateOutfit(prompt);
      resultElement.innerText = result;
    } catch (error) {
      resultElement.innerText =
        "Error generating outfit. Check API key or console.";
      console.error(error);
    }
  });