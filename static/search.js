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
    $(".vote").click(function(){
        console.log(this.id.substring(4))
        var number = parseInt(this.id.substring(4))
        id = number
        votes = parseInt(this.innerHTML) + 1
        $.ajax({
            type: "POST",
            url: "",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify({"votes": votes,"number": id}),
            success: function(data){
                $("#vote" + id).css("background-color","darkorange")
                $("#vote" + id).html(votes)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        })
    })
}
)

var display_results = function(results){
    $("#results").empty()
    $("#box").attr("value", term)
    console.log(results)
    if (results.length == 0){
        $("#results").append("<div class='result'><h3>No suggestions found</h3></div>")
    }
    else {$.each(results, function(i, result){
            var row = $("<div class='result' id = " + result["number"] + ">")
            var toAdd = "<h2>" + result["model"] + "</h2><div class=details><h4>Description:</h4><div class=desc>" + result["movement"] + "</div><br/></div><div class=imgDiv><img class=newImg src=" + result["img"] + "></div><div class=vote id=\"vote" + result["number"] + "\">" + result["votes"] + "</div></div>"
            $(row).append(toAdd)
            $(row).on('click', function(e){
                if (e.target.className === 'vote'){
                    console.log("vote")
                    return;
                }
                number = result["number"]
                model = result["model"]
                console.log(model)
                $('#messageModal').modal('show')
                $(row).css("background-color","darkgray")
            })
            $(row).hover(
                function(){$(row).css("background-color","#fffbf5")},
                function(){$(row).css("background-color","#fff2e0")}
            )            
            $("#results").append(row)
        }
        )
    }
}