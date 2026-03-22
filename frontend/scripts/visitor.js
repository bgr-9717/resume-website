 const API_URL =
  "https://hljgoysvxl.execute-api.af-south-1.amazonaws.com/Prod/count";

async function fetchVisitorCount() {
  try {
    const response = await fetch(API_URL, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    });

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const count = await response.text();
    document.getElementById("visitor-count").textContent = count;

  } catch (error) {
    console.error("Failed to fetch visitor count:", error);
    document.getElementById("visitor-count").textContent = "Unavailable";
  }
}

document.addEventListener("DOMContentLoaded", fetchVisitorCount);
