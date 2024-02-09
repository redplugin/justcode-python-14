// const changeColorBtn = document.getElementById("changeColorBtn");
const containerElement = document.getElementById("main");

function clickHandler() {
  col = containerElement.style.backgroundColor;
  console.log(col);
  if (!col) {
    containerElement.style.backgroundColor = "#6aff00";
  }
}
