let clickable_div = document.getElementById("body-div");

let timer;

console.log(clickable_div)

clickable_div.addEventListener('click', function(e) {
    console.log("Clicked!")
    if(timer) {
        clearTimeout(timer);
    }
    timer = setTimeout(() => {
        console.log("Now Clicked Event Occur")
    }, 200);
});

