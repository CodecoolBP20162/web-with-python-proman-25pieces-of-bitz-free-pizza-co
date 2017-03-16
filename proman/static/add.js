$(document).ready(function () {

    function saveData() {
        var task = $(".task").val()
        localStorage.setItem("task", task)
        var vaze = localStorage.task
        $(".drag").html(vaze)

    }


    $(".add").click(function () {
        var createDiv = document.createElement("div")
        var findCard = document.getElementById("cardLoc")
        var addDiv = findCard.appendChild(createDiv)
        $(addDiv).addClass("cards")
        $(".cards").draggable({

        });

    })


});