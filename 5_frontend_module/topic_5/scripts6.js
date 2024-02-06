function handleSubmit() {
  const usernameElement = document.getElementById("username");

  console.log(`Form submitted in js file! ${usernameElement.value}`);
  alert("Отлично!");
}

const formElement = document.getElementById("form1");
formElement.addEventListener("submit", handleSubmit);
