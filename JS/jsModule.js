var arrowThis = (function () {
    this.props = "OUTER_PROPS"
    return {
        arrow: () => {
            console.log(this);
            console.log(this.props);
        }
    };
})();

window.props = "WINDOW_PROPS";
arrowThis.arrow();