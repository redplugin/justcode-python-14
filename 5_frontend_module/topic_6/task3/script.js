// const changeColorBtn = document.getElementById("changeColorBtn");
const inputElement = document.getElementById("taskInput");
const tasksElement = document.getElementById("tasks");

function clickHandler() {
  // const newTask = inputElement.value;

  tasksElement.innerHTML += `<li>${inputElement.value}</li>`;
}
