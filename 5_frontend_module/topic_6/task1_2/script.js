const sumBtn = document.getElementById("sumButton");

const numbers = document.getElementsByClassName("number");

const resultElement = document.getElementById("result");

function getNumberPart(pTextContent) {
  // Number 1: 10
  number = pTextContent.split(":")[1];
  number = number.trim(); // strip() in python
  return Number(number);
}

function getNumberPartWithSlices(pTextContent) {
  // Number 1: 10
  ind = pTextContent.indexOf(":");
  number = pTextContent.slice(ind + 1);
  number = number.trim(); // strip() in python
  return Number(number);
}

function clickHandler() {
  var res = 0;
  console.log(`number: ${numbers}`);

  for (let i = 0; i < numbers.length; i++) {
    console.log(`number: ${numbers[i].textContent}`);
    res += getNumberPartWithSlices(numbers[i].textContent);
  }

  console.log(`Result: ${res}`);

  resultElement.textContent = `Result: ${res}`;
}

sumBtn.addEventListener("click", clickHandler);

// const sumBtn = document.getElementById("sumButton");

// const number1 = document.getElementById("number1");
// const number2 = document.getElementById("number2");
// const number3 = document.getElementById("number3");
// const number4 = document.getElementById("number4");

// const resultElement = document.getElementById("result");

// function clickHandler() {
//   const res =
//     Number(number1.textContent) +
//     Number(number2.textContent) +
//     Number(number3.textContent) +
//     Number(number4.textContent);
//   console.log(`Result: ${res}`);

//   resultElement.textContent = `Result: ${res}`;
// }

// sumBtn.addEventListener("click", clickHandler);
