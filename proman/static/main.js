$(document).ready(function () {
    var $container = $('.clmn-content')
    $('.column').mouseenter(function () {
        $(this).animate({
            opacity: 1,
            width: '+=12px'
        }, "fast");
    });
    $('.column').mouseleave(function () {
        $(this).animate({
            opacity: 0.7,
            width: '-=12px'
        }, "fast");
    });
    $container.delegate('.card', 'mouseenter', function () {
        $(this).animate({
            width: '+=60px'
        }, "fast");
        $(this).find(".submit_content").fadeIn();
    });
    $container.delegate('.card', 'mouseleave', function () {
        $(this).animate({
            width: '-=60px'
        }, "fast");
        $(this).find(".submit_content").fadeOut(100);
    });
    $container.delegate('.card', 'click', function () {
        $(this).find(".submit_content").fadeOut(100);
    });
    // saving card content
    $container.delegate('.submit_content', 'click', function (event) {
        var button = $(event.target);
        console.log(button)
        var card_id = $(button).attr("id");
        console.log(card_id)
        var card_title = $(button).parent().parent().find("input").val();
        console.log(card_title)
        var card_textarea = $(button).parent().parent().find("textarea").val();
        console.log(card_textarea)
        var card_status = $(button).parent().parent().parent().parent().attr('id');
        // console.log(card_status);
        $.ajax({
            url: "/update/" + card_id + "/" + card_title + "/" + card_textarea + "/" + card_status, success: function (data) {
                console.log(data);
            }
        });
    });
    // end of saving card content
});
// document ready end

// new card
var numberOfCards = 6;


function addNewCard(column) {

    numberOfCards += 1
    var cardId = "card" + numberOfCards;
    console.log(numberOfCards)
    $(column + ' .clmn-content').append("<div class='card' status='to-do' id=" + cardId + " draggable='true' ondragstart='drag(event)'><header><input class='card_title' placeholder='Card Title'></header><br><article class='card_text'><textarea class='card_content' id='cardContent1' placeholder='Card Content'></textarea><button id=" + numberOfCards + " class='submit_content'>Save</button></article></div>");
    // var card_position has to be implemented
    var assigned_board = 1;
    var card_status = "to-do";
    console.log(card_status)
    $.ajax({
        url: "/new/" + card_status + "/" + assigned_board, success: function (data) {
            console.log(data);
        }
    });
};
// end of new card

// update card status and position
function updateStatus(column) {
    var position = 0;
    $(column).children(".card").each(function () {
        var card_id = $(this).attr("id").replace("card", "");
        console.log(card_id)
        var board_id = $(this).attr('boardId');
        var card_title = $(this).find("input").val();
        console.log(card_title)
        var card_content = $(this).find("textarea").val();
        console.log(card_content)
        var card_status = column.replace('#', '');
        position++;
        $.ajax({
            url: "/" + card_id + "/" + board_id + "/" + card_status + "/" + position
        });
    });
}
// end of update card status and position

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id); /*on drag, saving essential data to identify the html element that are being moved*/
}


function drop(ev) {
    ev.preventDefault();
    var card_id = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(card_id)); /*on drop, appending the element identified with the data*/
    var card_status = $(ev.target).parent().attr("id")
    var board_id = 1;
    card_id = card_id.replace("card", "")
    $.ajax({
        url: "/update_card_position/" + card_id + "/" + board_id + "/" + card_status, success: function (data) {
            console.log(data);
        }
    });
};
