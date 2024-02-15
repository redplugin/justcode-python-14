const timeElement = document.getElementById("time");
const btnStartStop = document.getElementById("btn");

var isActive = false;
var intervalId = "";

const showCurrentTime = function () {
  var datetime = new Date();
  // console.log(datetime);

  const options = {
    hour: "numeric",
    minute: "2-digit",
    second: "2-digit",
  };
  datetime = datetime.toLocaleDateString("ru-RU", options);

  timeElement.textContent = `${datetime}`;
};

const intervalManager = function () {
  if (isActive) {
    clearInterval(intervalId);
    isActive = false;
    btnStartStop.textContent = "Start";
  } else {
    intervalId = setInterval(showCurrentTime, 1000);
    isActive = true;
    btnStartStop.textContent = "Stop";
  }
};
