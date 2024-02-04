function sumN(n) {
  if (n == 1) {
    return 1;
  }
  return n + sumN(n - 1);
}

// 4 + 6 = 10

// n = 4
// 1 + 2 + 3 + 4 = 10
// 4 + 3 + 2 + 1

res = sumN(6);
console.log(res);
