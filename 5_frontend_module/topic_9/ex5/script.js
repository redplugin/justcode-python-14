const btnChangeColor = document.getElementById("btn");

var isGreen = true;

const changeBtnColor = function () {
  // btnChangeColor.setAttribute("disabled", true);
  console.log("Before setTimeout...");
  setTimeout(() => {
    console.log("In setTimeout...");
    // btnChangeColor.removeAttribute("disabled");
    // btnChangeColor.setAttribute("disabled", false);
    if (isGreen) {
      btnChangeColor.style.backgroundColor = "red";
      isGreen = false;
    } else {
      btnChangeColor.style.backgroundColor = "green";
      isGreen = true;
    }
  }, 3000);

  console.log("After setTimeout...");
};
