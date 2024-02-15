const square = document.getElementById("square");

x_len = 0;

var intervalId = "";

const moveSquare = function () {
  // intervalId = setInterval(() => {
  //   x_len += 1;
  //   square.style.marginLeft = `${x_len}px`;
  // }, 100);

  x_len += 1;
  square.style.marginLeft = `${x_len}px`;

  if (x_len < 1000) {
    requestAnimationFrame(moveSquare);
  }
};
// moveSquare();

document.addEventListener("click", (event) => {
  console.log(`x: ${event.clientX}, y: ${event.clientY}`);

  square.style.marginLeft = `${event.clientX - 50}px`;
  square.style.marginTop = `${event.clientY - 50}px`;
});
