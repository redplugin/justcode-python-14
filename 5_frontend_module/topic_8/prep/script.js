document.addEventListener("DOMContentLoaded", fetchData);

async function fetchData() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    displayData(data);
  } catch (error) {
    console.error("There was a problem with your fetch operation:", error);
  }
}

function displayData(data) {
  const dataContainer = document.getElementById("data-container");

  data.forEach((post) => {
    const postElement = document.createElement("div");
    postElement.classList.add("post");
    postElement.innerHTML = `
      <h2>${post.title}</h2>
      <p>${post.body}</p>
    `;
    dataContainer.appendChild(postElement);
  });
}
