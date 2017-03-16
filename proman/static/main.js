$(document).ready(function () {
    $('.column .movable-header').mouseenter(function () {
        $(this).animate({
            height: '+=10px',
            width: '+=5px'
        }, "fast");
    });
    $('.column .movable-header').mouseleave(function () {
        $(this).animate({
            height: '-=10px',
            width: '-=5px'
        }, "fast");
    });
});


$(function () {
    $(".column .clmn-content").sortable();
    $(".column .clmn-content").disableSelection();
});
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}