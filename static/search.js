$(document).ready(function(){
    $("#modal").hide()
    $("#close").click(function(){
        $("#modal").hide()
        $("#msg_container").empty()
        $("#msg_container").append("<div class=info>Messaging seller</div><textarea id='msg' type='text' name='email'></textarea><br/><button id='send' type='submit' name='send'>Send</button>")
    }
    )
    $("#send").click(function(){
        var msg = $("#msg").val();
        if (msg != ""){
            $.ajax({
                type: "POST",
                url: "search",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify({"number": number, "msg": msg}),
                success: function(data){
                    $("#msg_container").empty()
                    $("#msg_container").append("<div class='info'><h3>Message sent!</h3></div>")
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
    display_results(results)
})

var display_results = function(results){
    $("#results").empty()
    $("#box").attr("value", term)
    console.log(results)
    if (results.length == 0){
        $("#results").append("<div class='result'><h3>No watches found</h3></div>")
    }
    else {$.each(results, function(i, result){
            var row = $("<div class='result'>")
            var toAdd = "<h2>" + result["model"] + "</h2><br/><h3>Movement: " + result["movement"] + "</h3><h3>$" + result["price"] + "</h3><br/>"
            $(row).append(toAdd)
            $(row).click(function(){
                console.log("clicked")
                number = result["number"]
                $("#modal").show()
            })
            $("#results").append(row)
        }
        )
    }
}