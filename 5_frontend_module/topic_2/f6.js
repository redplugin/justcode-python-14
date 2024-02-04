// res = 0;
// var a = [1, 4, 7, 10, 5, 3];

// for (let i = 0; i < a.length; i++) {
//   res = res + a[i];
// }

var a = [1, 4, 7, 10, 5, 3];
var res = a.reduce((total, current) => total + current, 5);

console.log(res);
