test();

function test() {
    console.log(foo);
    var foo = "foo variable";
}

let a = 30;
function callVariable() {
    console.log(a);
    let a = 50;
    console.log(a);
}

callVariable();