const POSTS_URL = "https://jsonplaceholder.typicode.com/posts";

// async / await

async function fetchData() {
  const response = await fetch(POSTS_URL);
  console.log(response);

  const postsData = await response.json();
  insertData(postsData);
}

function insertData(posts) {
  console.log(posts);
  // let mainElement = document.getElementsByClassName("main")[0];
  let mainElement = document.getElementById("main");

  posts.forEach((post) => {
    let postBlock = document.createElement("div");
    postBlock.classList.add("bg-warning", "rounded", "mt-3", "p-3");
    postBlock.innerHTML = `
      <h1>${post.title}</h1>
      <p>${post.body}</p>`;

    mainElement.appendChild(postBlock);
  });
}

fetchData();
