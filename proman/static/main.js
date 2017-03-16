
$( function() {
    $( "#status-field" ).sortable();
    $( "#status-field" ).disableSelection();
  } );
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
/*$('.card_content, .card_title').click(function(){
  $(this).toggleClass('clicked');
}*/