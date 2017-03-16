$(document).ready(function () {
    $('.column').mouseenter(function () {
        $(this).animate({
            opacity: 1,
            width: '+=12px'
        }, "fast");
    });
    $('.column').mouseleave(function () {
        $(this).animate({
            opacity: 0.5,
            width: '-=12px'
        }, "fast");
    });
    $('.card').mouseenter(function () {
        $(this).animate({
            width: '+=20px'
        }, "fast");
    });
    $('.card').mouseleave(function () {
        $(this).animate({
            width: '-=20px'
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