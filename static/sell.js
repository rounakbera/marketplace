$(document).ready(function(){

    $("#button").click(function(){
		login()
    })
    
    $("#new_listing").click(function(){
		new_listing()
    })
    
    $("#update").click(function(){
        update()
    })

    $("#createNew").click(function(){
        make_new()
    })

    var id = -1
    var username
})

var display_results = function(results){
    $("#results").empty()
    console.log(results)
    {$.each(results, function(i, result){
            var row = $("<br/><div class='result' id = " + result["number"] + ">")
            var toAdd = "<h2>" + result["model"] + "</h2><div class=details><h4>Description:</h4><div class=desc>" + result["movement"] + "</div>"
            if (result["messages"] != null){
                toAdd += "<h4>Messages:</h4><div class=msglist>"
                result["messages"].forEach(element => {
                    toAdd += element
                    toAdd += "<br/>"
                });
                toAdd+="</div>"
            }
            toAdd += "<div class=imgDiv>"
            toAdd += "<img class=newImg src=" + result["img"] + ">"
            toAdd += "</div><div class=vote id=\"vote" + result["number"] + "\">" + result["votes"] + "</div>"
            toAdd += "</div><br/><button class='updated btn btn-primary' id=updated" + result["number"] + " type='button' data-toggle='modal' data-target='#updateModal'>Update</button><button class=deleted id=deleted" + result["number"] + " type=submit>Delete</button>"
            row.append(toAdd);
            $(row).hover(
                function(){$(row).css("background-color","#fffbf5")},
                function(){$(row).css("background-color","#fff2e0")}
            )
            $("#results").append(row)
        }
        )
    }
    $(".updated").click(function(){
        console.log(this.id.substring(7))
        var number = parseInt(this.id.substring(7))
        id = number
        for (w of results){
            console.log(w)
            if (w["number"] == id){
                var model = w["model"]
                var movement = w["movement"]
                var price = w["img"]
            }
        }
        console.log(model + movement + price)
        var toAdd = "Issue: <input id=model type=text name=model value=\"" + model + "\"><br/>Description: <input id=movement type=text name=movement value=\"" + movement + "\"><br/>Image URL: <input id=price type=text name=price value=" + price + ">"
        $("#modal-body").empty()
        $("#modal-body").append(toAdd)
        $("#updateModal").modal('show')
    })
    $(".deleted").click(function(){
        console.log(this.id.substring(7))
        deleted(this.id.substring(7))
    })
}

var login = function(){
    username = $("#username").val()
    if (username != ""){
        $.ajax({
            type: "POST",
            url: "sell",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify({"username": username}),
            success: function(data){
                results = data
                if (results.length == 0){
                    $("#results").empty()
                    $("#results").append("<div class='result'><h3>The username had no submissions</h3></div>")
                }
                else{
                    display_results(data)
                }
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        })
    }
    else{
        $("#error-body").empty()
        $("#error-body").append("Enter a username before getting your submissions.")
        $("#errorModal").modal('show')
    }
}

var update = function(){
    var model = $("#model").val()
    var movement = $("#movement").val()
    var price = $("#price").val()
    if (model != "" && movement != "" && price != ""){
        $.ajax({
            type: "POST",
            url: "sell",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({"number": id, "model": model, "movement": movement, "price": price, "username": username}),
            success: function(data){
                results = data
                console.log(results)
                display_results(results)
                number = -1
                $("#"+id).append("<div class='result'><h3>Submission updated</h3></div>")
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

var deleted = function(id){
    console.log("deleting " + id)
    $.ajax({
        type: "POST",
        url: "sell",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify({"number": id}),
        success: function(data){
            results = data
            number = -1
            $("#" + id).empty()
            $("#" + id).append("<h3>Submission deleted</h3>")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}

var new_listing = function(){
    username = $("#username").val()
    console.log(username)
    if (username != ""){
        $("#newModal").modal('show')
        var toAdd = "Issue: <input id=model type=text name=model><br/>Description: <input id=movement type=text name=movement><br/>Image URL: <input id=price type=text name=price>"
        $("#new-modal-body").empty()
        $("#new-modal-body").append(toAdd)
    }
    else{
        $("#error-body").empty()
        $("#error-body").append("Enter a username before creating a new submission.")
        $("#errorModal").modal('show')
    }
}

var make_new = function(){
    var model = $("#model").val()
    var movement = $("#movement").val()
    var price = $("#price").val()
    if (username != "" && model != "" && movement != "" && price != ""){
        $.ajax({
            type: "POST",
            url: "sell",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({"username": username, "model": model, "movement": movement, "price": price}),
            success: function(data){
                result = data
                number = -1
                var row = $("<br/><div class='result' id = " + result["number"] + ">")
                var toAdd = "<h2>" + result["model"] + "</h2><div class=details><h4>Description:</h4><div class=desc>" + result["movement"] + "</div>"
                toAdd += "<div class=imgDiv>"
                toAdd += "<img class=newImg src=" + result["img"] + ">"
                toAdd += "</div><div class=vote id=\"vote" + result["number"] + "\">" + result["votes"] + "</div>"
                toAdd += "</div><div class=info><h3>Listing created</h3></div>"
                row.append(toAdd);
                $("#results").prepend(row)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        })
    }
    else{
        $("#error-body").empty()
        $("#error-body").append("Enter a valid issue, description, and an image URL.")
        $("#errorModal").modal('show')
    }
}