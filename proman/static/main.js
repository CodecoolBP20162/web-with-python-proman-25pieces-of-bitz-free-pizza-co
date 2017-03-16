$(document).ready(function () {
    $('.card-status .movable-header').mouseenter(function () {
        $(this).animate({
            height: '+=10px',
            width: '+=5px'
        }, "fast");
    });
    $('.card-status .movable-header').mouseleave(function () {
        $(this).animate({
            height: '-=10px',
            width: '-=5px'
        }, "fast");
    });
});

class Board {
    constructor(number, column1, column2, column3, column4) {
        this.number = number;
        this.column1 = column1;
        this.column2 = column2;
        this.column3 = column3;
        this.column4 = column4;
    }
}