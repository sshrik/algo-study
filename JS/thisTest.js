function aa() {
    console.log(this.a);
    console.log(a);
}

let a = 3;

let aaa = {
    fu : aa,
    a : 5
}

aa();
aaa.fu();

function acd(callback) {
    let a = 6;
    callback();
}

acd(aa);
acd(() => {
    console.log(this.a);
    console.log(a);
});

let asd = {
    fu: acd,
    fu2: aa,
    aaa: aaa,
    a: 7
}

asd.fu(aa);
asd.fu(aaa.fu);
asd.aaa.fu();
asd.fu2();