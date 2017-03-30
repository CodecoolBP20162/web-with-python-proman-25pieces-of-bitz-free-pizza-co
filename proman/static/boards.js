$(document).ready(function () {
    var $container = $('.boardlist')
    var num = 0;
    $('.add_new_board').click(function () {
        num++;
        boardId = 'board' + num;
        $('.boardlist').append('<div class="board"><p class="board-name" contenteditable="true" id=' + boardId + '>Board ' + num + '</p></div>');
    });
    $container.delegate('.board', 'click', function () {
        $(this).find(".submit_content_board").fadeIn();
    });
    $container.delegate('.board', 'mouseleave', function () {
        $(this).find(".submit_content_board").fadeOut(100);
    });
    /*save does not work*/
    $(".submit_content_board").click(function (event) {
        var button = $(event.target);
        var board_id = $(button).attr("id");
        var new_name = $(button).parent().find("p").val();
        console.log(board_name, board_id);
        $.ajax({
            url: "/update/" + board_id + "/" + new_name, success: function (data) {
                console.log(data);
            }
        });
    });
});