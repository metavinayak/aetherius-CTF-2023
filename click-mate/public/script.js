let button = document.getElementById('item');
button.onmousedown = function() {
    button.style.boxShadow = '3px 2px 1px rgb(80, 0, 110)';
}
button.onmouseup = function() {
    button.style.boxShadow = "4px 4px 0px rgb(82, 0, 114)";
    button.style.animation = 'wobble 1s';
}

var x = 0;
var y = 0;

var button_x = 200;
var button_y = 200;

document.addEventListener('mousemove', runAway, false);

function runAway(e) {
    x = e.pageX;
    y = e.pageY;
    button.style.left = (x + 20) + 'px';
    button.style.top = (y + 20) + 'px';
}