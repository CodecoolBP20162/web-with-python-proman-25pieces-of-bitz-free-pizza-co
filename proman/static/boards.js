$(document).ready(function() {
    var num = 0;
    $('.add_new_board').click(function(){
        num++;
        boardId = 'board'+num;
        $('.boardlist').append('<div class="board"><p class="board-name" contenteditable="true" id='+boardId+'>Board '+num+'</p></div>');
    });

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