const POSTS_URL = "https://jsonplaceholder.typicode.com/posts";

var postsData = [];

fetch(POSTS_URL)
  .then((response) => response.json())
  .then((data) => {
    insertData(data);
  });

function insertData(posts) {
  console.log(posts);
  let mainElement = document.getElementsByClassName("main")[0];

  for (let i = 0; i < posts.length; i++) {
    mainElement.innerHTML += `<div class="post">
        <h1>${posts[i].title}</h1>
        <p>${posts[i].body}</p>
        </div>`;
  }
}
