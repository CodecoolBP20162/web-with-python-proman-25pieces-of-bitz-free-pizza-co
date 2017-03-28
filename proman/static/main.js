$(document).ready(function () {
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
    $('.card').mouseenter(function () {
        $(this).animate({
            width: '+=60px'
        }, "fast");
    });
    $('.card').mouseleave(function () {
        $(this).animate({
            width: '-=60px'
        }, "fast");
    });
    $(function () {
        document.getElementById("cardContent1").innerHTML = localStorage.getItem("#cardContent1");
        document.getElementById("cardContent2").innerHTML = localStorage.getItem("#cardContent2");
        document.getElementById("cardContent3").innerHTML = localStorage.getItem("#cardContent3");
        document.getElementById("cardContent4").innerHTML = localStorage.getItem("#cardContent4");
        document.getElementById("cardContent5").innerHTML = localStorage.getItem("#cardContent5");
    });

    $('.add_new_card').click(function(){
        $('#to-do .clmn-content').append('<div class="card" id="drag1" draggable="true" ondragstart="drag(event)"><header><input class="card_title" placeholder="Card Title"></header><br><article class="card_text"><textarea class="card_content" id="cardContent1" placeholder="Card Content"></textarea><button class="submit_content">Save</button> </article> </div>');
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