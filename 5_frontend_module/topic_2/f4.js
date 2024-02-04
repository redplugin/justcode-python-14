const sayHi = (name) => console.log("Hello world!", name);

const getSum = function (a) {
  return a + 1;
};

// sayHi("Ulan");
// f(); // error

var a = [1, 4, 7, 10, 5, 3];

var res = a.map(getSum);
console.log(res);
