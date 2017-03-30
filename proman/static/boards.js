$(document).ready(function() {
    var num = 0;
    $('.add_new_board').click(function(){
        num++;
        boardId = 'board'+num;
        $('.boardlist').append('<div class="board"><p class="board-name" contenteditable="true" id='+boardId+'>Board '+num+'</p></div>');
    });
});