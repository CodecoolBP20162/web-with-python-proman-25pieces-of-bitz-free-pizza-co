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
    // saving stuff, yo
    $(".submit_content").click(function (event) {
        var button = $(event.target);
        var card_id = $(button).attr("id");
        var card_title = $(button).parent().parent().find("input").val();
        var card_textarea = $(button).parent().parent().find("textarea").val();
        console.log(card_textarea);
        $.ajax({
            url: "/update/" + card_id + "/" + card_title + "/" + card_textarea, success: function (data) {
                console.log(data);
            }
        });
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

var num = 0;

function addNewCard(column) {

    num += 1;
    var cardId = "drag" + num;
    $(column + ' .clmn-content').append("<div class='card' id=" + cardId + " draggable='true' ondragstart='drag(event)'><header><input class='card_title' placeholder='Card Title'></header><br><article class='card_text'><textarea class='card_content' id='cardContent1' placeholder='Card Content'></textarea><button class='submit_content'>Save</button></article></div>");
};