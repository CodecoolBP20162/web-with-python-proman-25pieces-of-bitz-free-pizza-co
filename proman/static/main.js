$(document).ready(function () {
    $('card-status').mouseenter(function () {
        $(this).animate({
            height: '+=10px'
        });
    });
    $('card-status').mouseleave(function () {
        $(this).animate({
            height: '-=10px'
        });
    });
    $('card-status').click(function () {
        $(this).toggle(1000);
    });
});