person = {
  name: "Ulan",
  surname: "Kospan",
  age: 12,

  sayHi: function () {
    console.log("Hello from", this.name);
  },
};

console.log(person.name);
person.sayHi();
