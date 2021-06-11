function Person() {}
Person.prototype.eyes = 2;
Person.prototype.nose = 1;
var kim  = new Person();
var park = new Person();
console.log(kim.eyes);
console.log(park.eyes);

kim.eyes=3;
console.log(kim.eyes);
console.log(park.eyes);