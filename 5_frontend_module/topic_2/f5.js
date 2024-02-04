var a = [1, 4, 7, 10, 5, 3];

var res = a.map((elem) => elem + 1);

// var res = a.map((elem) => {
//     return elem + 1
// });

var res2 = res.filter((elem) => elem % 2 == 0);

console.log("res:", res);
console.log("res2:", res2);
