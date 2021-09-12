class Parent {
    constructor() {
        this.__age = 40;
    }

    get age(){
        return this.__age;
    }
}

class Mother extends Parent {
    constructor() {
        super();
        this._age = 30;
    }

    get age() {
        return this._age;
    }
}

const mother = new Mother();
console.log(mother.age);


