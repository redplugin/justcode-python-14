function handleSubmit(event) {
  event.preventDefault();

  const usernameElement = document.getElementById("username");

  const resultElement = document.getElementById("result");

  console.log(resultElement.innerHTML);
  //   resultElement.innerHTML = `<p>Привет, ${usernameElement.value}!</p>`;
  resultElement.innerHTML += `<p>Привет, ${usernameElement.value}!</p>`;
}

const formElement = document.getElementById("form1");
formElement.addEventListener("submit", handleSubmit);
// formElement.addEventListener("click", handleClick);
