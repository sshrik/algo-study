const props = "windowObj";
const testObj = {
    props: "testObj",
    arrow: () => {
        const props = 'arrowProps'
        console.log("[ ARROW FUNCTION ]");
        console.log("this :", this);
        console.log("this.props :", this.props);
        const moreArrow = () => {
            console.log("[ MORE ARROW FUNCTION ]");
            console.log("this :", this);
            console.log("this.props :", this.props);
        }
        moreArrow();
    },
    func: function() {
        console.log("[ DEFINE FUNCTION ]");
        console.log("this :", this);
        console.log("this.props :", this.props);
    }
}

const arrowObj = {
    props: "arrowObj",
    arrow: {
        props: "moreArrowObj",
        moreArrow: () => {
            console.log("[ MORE ARROW FUNCTION ]");
            console.log("this :", this);
            console.log("this.props :", this.props);
            const props = "MORE MORE ARROW"
            const moreMoreArrow = () => {
                console.log("[ MORE MORE ARROW FUNCTION ]");
                console.log("this :", this);
                console.log("this.props :", this.props);
                console.log("props :", props);
            }
            moreMoreArrow();
        }
    },
}

arrowObj.arrow.moreArrow();


/*
console.log("TEST OBJ RUN");
testObj.arrow();
testObj.func();

console.log("THIS BREAKER OBJ CREATE");
const thisBreaker = {
    props: "breakerObj",
    arrow: (() => {
        const props = "breakerObj Arrows";
        testObj.arrow(props);
    })(),
    func: testObj.func(),
}

console.log("THIS BREAKER OBJ RUN");
testObj.arrow(thisBreaker);
testObj.func(thisBreaker);
*/