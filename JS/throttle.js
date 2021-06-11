let clickable_div = document.getElementById("body-div");

let timer;

console.log(clickable_div)

clickable_div.addEventListener('click', function (e) {
console.log('Clicked!');
  if (!timer) {
    timer = setTimeout(() => {
      timer = null;
      console.log('Now clicked!');
    }, 200);
  }
});