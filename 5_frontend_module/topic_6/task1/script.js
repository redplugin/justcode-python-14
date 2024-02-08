const sumBtn = document.getElementById("sumButton");

const input1 = document.getElementById("input1");
const input2 = document.getElementById("input2");

const resultElement = document.getElementById("result");

function clickHandler() {
  const res = Number(input1.value) + Number(input2.value);
  console.log(`ResultElement type: ${resultElement}`);
  console.log(`Result: ${res}`);

  //   resultElement.innerHTML = `<p>Result: ${res}</p>`;
  //   resultElement.textContent = `<p>Result: ${res}</p>`;
  resultElement.textContent = `Result: ${res}`;
}

sumBtn.addEventListener("click", clickHandler);
