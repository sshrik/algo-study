class IIFETest {
    constructor() {
        this.props = "IIFE_TEST_PROPS";
        (function() {
            console.log(this);
        }).apply(this);
    }
}

const IifeTestClass = new IIFETest();
