$(document).ready(function() {

    $('.board').click(function(){
       $(this).fadeOut('500');
    });

    $('.add_new_board').click(function(){
        $('.boardlist').append('<div class="board"><p>New Board</p></div>');
    });
});