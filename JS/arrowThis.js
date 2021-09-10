const arrow = () => {
    console.log(this);
    console.log(this.props);   
    console.log("");
}

class TestClass {
    constructor() {
        this.props = "TEST_CLASS_PROPS";
    }

    callArrowReal = () => {
        console.log("CALL REAL ARROW");
        console.log(this);
        console.log(this.props);
        console.log("");
    }

    callArrow() {
        arrow();
        return () => {
            console.log("JUST ARROW");
            arrow();

            console.log("MORE ARROW");
            console.log(this);
            console.log(this.props);
            console.log("");
        };
    }
    
    bindArrow() {
        arrow.call(this);
    }
}

const tc = new TestClass();

console.log("CALL ARROW");
const moreArrow = tc.callArrow();

console.log("MORE ARROW");
moreArrow();

console.log("PROPERTY ARROW");
tc.callArrowReal();

console.log("BIND ARROW");
tc.bindArrow();

console.log("PURE ARROW");
arrow();

const TestObj = {
    props: "Test Object Props",
    consoleThis: function() {
        console.log(this);
        console.log(this.props);   
        console.log("");
    },
    arrowThis: () => {
        console.log(this);
        console.log(this.props);   
        console.log("");
    }
}

const InjectThisObj = {
    props: "Injected Object Props",
}

/*
console.log("Test Obj Injected!")
moreArrow.call(TestObj);
moreArrow.bind(TestObj)();

TestObj.consoleThis();
TestObj.consoleThis.call(InjectThisObj);
TestObj.consoleThis.call(null);

TestObj.arrowThis();
TestObj.arrowThis.call(InjectThisObj);
TestObj.arrowThis.call(null);
*/

(function() { console.log(this) })()