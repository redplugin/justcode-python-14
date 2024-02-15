const divElement = document.getElementById("main");
const btnStartStop = document.getElementById("btn");

var isActive = false;
var intervalId = "";

const showTest = function () {
  var testNode = document.createElement("p");
  testNode.textContent = "test";
  divElement.appendChild(testNode);
};

const intervalManager = function () {
  if (isActive) {
    clearInterval(intervalId);
    isActive = false;
    btnStartStop.textContent = "Start";
  } else {
    intervalId = setInterval(showTest, 2000);
    isActive = true;
    btnStartStop.textContent = "Stop";
  }
};
