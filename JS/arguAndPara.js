function add(a, b, c, ...argv) {
    console.log(arguments);
    console.log(argv);
    return a + b + c;
}

console.log(add.length);

console.log(add(2, 3));
console.log(add(2, 3, 4, 5, 6, 7));
console.log(Object.keys(add));