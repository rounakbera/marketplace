$(document).ready(function(){
    models = []
    results.forEach(element => {
        models.push(element["model"])
    })
    console.log(models)
    $("#box").autocomplete({
        source: models
    })
    $('#box').keypress(function(e){
        if(e.which == 13){//Enter key pressed
            $('#button').click();//Trigger search button click event
        }
    });
    display_results(results)
    $("#send").click(function(){
        $("#" + number).css("background-color","white")
        console.log("hello")
        var msg = $("#msg").val();
        if (msg != ""){
            $.ajax({
                type: "POST",
                url: "search",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify({"number": number, "msg": msg}),
                success: function(data){
                    $("#" + number).append("<div class='info'><h3>Message sent!</h3></div>")
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            })
        }
    }
    )
}
)

var display_results = function(results){
    $("#results").empty()
    $("#box").attr("value", term)
    console.log(results)
    if (results.length == 0){
        $("#results").append("<div class='result'><h3>No watches found</h3></div>")
    }
    else {$.each(results, function(i, result){
            var row = $("<div class='result' id = " + result["number"] + ">")
            var toAdd = "<h2>" + result["model"] + "</h2><div class=details><h5>Movement: " + result["movement"] + "</h5><h5>Price: $" + result["price"] + "</h5><br/></div>"
            if (result["img"] != null){
                toAdd += "<div class=imgDiv>"
                result["img"].forEach(element => {
                    toAdd += "<img class=newImg src=" + element + ">"
                })
                toAdd += "</div>"
            }
            $(row).append(toAdd)
            $(row).click(function(){
                number = result["number"]
                model = result["model"]
                console.log(model)
                $('#messageModal').modal('show')
                $(row).css("background-color","darkgray")
            })
            $(row).hover(
                function(){$(row).css("background-color","lightgray")},
                function(){$(row).css("background-color","white")}
            )
            $("#results").append(row)
        }
        )
    }
}