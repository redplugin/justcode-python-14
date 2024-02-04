// var a = [1, 4, 7, 10, 5, 3];

function getSum(a, b, ...numbers) {
  console.log(a, b);
  return numbers.reduce((total, current) => total + current);
}

console.log(getSum(1, 3, 4, 5, 1, 2));
