$(document).ready(function(){

    $("#button").click(function(){
		login()
    })
    
    $("#new_listing").click(function(){
		new_listing()
	})

})

var display_results = function(results){
    $("#results").empty()
    console.log(results)
    var row = $("<div class='result'>")
    var toAdd = "<input id=model type=text name=model value='" + results["model"] + "'><input id=movement type=text name=movement value=" + results["movement"] + "><input id=price type=text name=price value=" + results["price"] + "><br/><button id=update type=submit>Update</button><button id=deleted type=submit>Delete</button>" 
    if (results["messages"] != null){
        toAdd += "<h3>Messages</h3>"
        results["messages"].forEach(element => {
            toAdd += "<br/>"
            toAdd += element
            toAdd += "<br/>"
        });
    }
    $(row).append(toAdd)
    $("#results").append(row)
    $("#update").click(function(){
        update()
    })
    $("#deleted").click(function(){
        deleted()
    })
}

var login = function(){
    var username = $("#username").val()
    var num = $("#number").val()
    if (username != "" && number != ""){
        $.ajax({
            type: "POST",
            url: "sell",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify({"username": username,"number": num}),
            success: function(data){
                results = data
                number = num
                if (results.length == 0){
                    $("#results").empty()
                    $("#results").append("<div class='result'><h3>The listing could not be found</h3></div>")
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
            data : JSON.stringify({"number": number, "model": model, "movement": movement, "price": price}),
            success: function(data){
                results = data
                number = -1
                $("#results").empty()
                $("#results").append("<div class='result'><h3>Listing updated</h3></div>")
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

var deleted = function(){
    $.ajax({
        type: "POST",
        url: "sell",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify({"number": number}),
        success: function(data){
            results = data
            number = -1
            $("#results").empty()
            $("#results").append("<div class='result'><h3>Listing deleted</h3></div>")
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
    var username = $("#username").val()
    if (username != ""){
        $("#results").empty()
        var row = $("<div class='result'>")
        var toAdd = "<input id=model type=text name=model placeholder='Model'><input id=movement type=text name=movement placeholder='Movement'><input id=price type=text name=price placeholder='Price'><br/><button id=make_new type=submit>Submit</button>" 
        $(row).append(toAdd)
        $("#results").append(row)
        $("#make_new").click(function(){
            make_new()
        }
        )
    }
}

var make_new = function(){
    var username = $("#username").val()
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
                results = data
                number = -1
                $("#results").empty()
                toAdd = "<div class='result'><h3>New listing created with username " + results[results.length-1]["id"] + " and ID number " + results[results.length-1]["number"] + "</h3></div>"
                $("#results").append(toAdd)
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