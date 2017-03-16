function saveData(id) {
    var content = $(id).val()
    localStorage.setItem(id, content)
    var drag = localStorage.content
    $(".drag").html(drag)
}


// $(".add").click(function () {
//     var createDiv = document.createElement("div")
//     var findCard = document.getElementById("cardLoc")
//     var addDiv = findCard.appendChild(createDiv)
//     $(addDiv).addClass(".card")
//     $(".card").draggable({

//     });
// })