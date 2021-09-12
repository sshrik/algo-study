class A0 {
    constructor() {
        this.a = 0;
    }
}

class A1 extends A0 {
    constructor() {
        super();
    }

    chainRuleTest() {
        let a = 30;
        
        const logA = () => {
            console.log(a);
            console.log(this.a);
        };

        logA();
    }
}

const a1 = new A1();

a1.chainRuleTest();