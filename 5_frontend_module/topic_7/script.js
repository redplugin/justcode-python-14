const resultElement = document.getElementById("res");

const input1 = document.getElementById("input1");
const input2 = document.getElementById("input2");

const historyElement = document.getElementById("history-list");

let operator = "+";
let result = 0;

let history = [];

function handleClick(event) {
  console.log(event);
  console.log(event.target.id);
  operator = event.target.id;

  //   if (operator === "btnPlus") {
  //     result = Number(input1.value) + Number(input2.value);
  //   } else if (operator === "btnMinus") {
  //     result = Number(input1.value) - Number(input2.value);
  //   } else if (operator === "btnMul") {
  //     result = Number(input1.value) * Number(input2.value);
  //   } else if (operator === "btnDiv") {
  //     result = Number(input1.value) / Number(input2.value);
  //   } else {
  //     result = "К сожалению, пока не реализовано:(";
  //   }

  switch (operator) {
    case "btnPlus": {
      result = Number(input1.value) + Number(input2.value);
      operator = "+";
      break;
    }
    case "btnMinus": {
      result = Number(input1.value) - Number(input2.value);
      operator = "-";
      break;
    }
    case "btnMul": {
      result = Number(input1.value) * Number(input2.value);
      operator = "*";
      break;
    }
    // case "test":
    case "btnDiv": {
      result = Number(input1.value) / Number(input2.value);
      operator = "/";
      break;
    }
  }

  //   try {
  // throw "Какая нибудь ошибка!";
  // throw "Какая нибудь другая ошибка!";
  //   } catch (err) {
  //     if (err == "Какая нибудь ошибка!") {
  //       console.log("мы знаем эту ошибку:", err);
  //     } else {
  //       console.log("ошибка:", err);
  //       throw err;
  //     }
  //   }

  history.push(`${input1.value} ${operator} ${input2.value} = ${result}`);

  resultElement.textContent = result;
  historyElement.innerHTML += `<li>${input1.value} ${operator} ${input2.value} = ${result}</li>`;
}
