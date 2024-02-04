function outer(x) {
  function inner(y) {
    return x + y;
  }

  return inner;
}

var addFive = outer((x = 5)); // x = 5, inner(y) {return 5 + y}
var addOne = outer((x = 1)); // x = 1, inner(y) {return 5 + y}

console.log(typeof addFive);

var res = addFive((y = 3)); // 8
var res2 = addOne((y = 3)); // 4
console.log(res);
console.log(res2);

console.log("last:", outer(5)(7));
