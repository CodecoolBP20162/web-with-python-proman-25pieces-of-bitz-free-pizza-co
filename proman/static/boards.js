$(document).ready(function () {
    class Board {
        constructor(number) {
            this.number = number;
        };
    };
    class Card {
        constructor(number, status) {
            this.number = number;
            this.status = status;
        };
    };

    var boards = [];
    var board1 = new Board(1);
    var card1 = new Card(1, "todo");
    Storage.prototype.setObject = function (key, value) {
        this.setItem(key, JSON.stringify(value));
    }
});