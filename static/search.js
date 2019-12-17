$(document).ready(function(){
    models = []
    login = 'false'
    admin = false
    title = ""
    desc = ""
    img = ""
    number = -1
    $('#viewModal').modal('hide')
    $('#loginModal').modal('hide')
    $('#newModal').modal('hide')
    $('#newsubmit').hide()
    $('#logoutButton').hide()
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
    $("#loginButton").on('click', function(e){
        var username = $("#username").val();
        if (username != ""){
            $.ajax({
                type: "POST",
                url: "",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify({"login": username}),
                success: function(data){
                    if (data["login"]==true){
                        login = username
                        console.log('login')
                        console.log(login)
                        $("#login").html("Welcome, " + username)
                        $("#newsubmit").show()
                        $("#logoutButton").show()
                    }
                    if (data["admin"]==true){
                        admin = true
                    }
                    display_results(results)
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
    $("#save").on('click',function(e){
        title = $("#editTitle").val();
        desc = $("#editDesc").val();
        img = $("#editImg").val();
        if (title != "" && desc != "" && img != ""){
            $.ajax({
                type: "POST",
                url: "",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify({"edit": "true","number":number,"model":title,"movement":desc,"price":img}),
                success: function(data){
                    display_results(data)
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
    $("#save2").on('click',function(e){
        title = $("#editTitle2").val();
        desc = $("#editDesc2").val();
        img = $("#editImg2").val();
        if (title != "" && desc != "" && img != ""){
            $.ajax({
                type: "POST",
                url: "",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify({"new": "true","username":login,"model":title,"movement":desc,"price":img}),
                success: function(data){
                    display_results(data)
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
    $("#delete").on('click',function(e){
        $.ajax({
            type: "POST",
            url: "",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify({"delete": "true","number":number}),
            success: function(data){
                display_results(data)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        })
    })
    $("#logoutButton").on('click',function(e){
        login = 'false'
        admin = false
        $("#login").html("Login!")
        $("#newsubmit").hide()
        $("#logoutButton").hide()
        display_results(results)
    }
    )
}
)

var loadComments = function(id){
    var res = null
    for (let i in results){
        if(results[i]["number"] == id){
            res = results[i]
            break;
        }
    }
    var toAdd = ""
    $("#viewComments").html("<div id='appendComments'></div>");
    for (let i in res["messages"]){
        console.log(res["messages"][i])
        if(res["messages"][i]["admin"]){
            toAdd="<div class='comment'><h5 class='admin'>" + res["messages"][i]["user"] + "</h5>"
        }
        else{
            toAdd="<div class='comment'><h6>" + res["messages"][i]["user"] + "</h6>"
        }
        toAdd+="<h9>" + res["messages"][i]["msg"] + "<h9></div>"
        $("#appendComments").append(toAdd)
    }
}

var display_results = function(results){
    $("#results").empty()
    $("#box").attr("value", term)
    console.log(results)
    if (results.length == 0){
        $("#results").append("<div class='result'><h3>No submissions found</h3></div>")
    }
    else {$.each(results, function(i, result){
            var toAdd = "<div class='card' id = " + result["number"] + " style=\'width: 18rem;\'>"
            toAdd += "<img src='"+result["img"]+"' class='card-img-top' id = img" + result["number"] + " alt='...'>"
            toAdd += "<div class='card-body'>"
            toAdd += "<h5 class='card-title' id = title" + result["number"] + " >"+result["model"]+"</h5>"
            toAdd += "<p class='card-text' id = desc" + result["number"] + " >"+result["movement"]+"</p>"
            if (login == 'false'){
                toAdd += "<button class='view btn btn-primary' id='view"+result["number"]+"'>View</button>"
            }
            else{
                toAdd += "<button class='view btn btn-primary' id='view"+result["number"]+"'>Comment</button>"
            }
            if (login == result["id"] || admin){
                toAdd += "<button class='edit btn btn-primary' id='edit"+result["number"]+"'>Edit</button>"
            }
            toAdd += "<div class=vote id=\"vote" + result["number"] + "\">" + result["votes"] + "</div></div>"
            toAdd += "</div></div>"
            $(toAdd).hover(
                function(){
                    console.log('hello');
                    $(toAdd).css('transform', 'scale(1.2)');
                },
                function(){$(toAdd).css('transform', 'scale(1)')}
            ) 
            $("#results").append(toAdd)
            $(".vote").click(function(){
                if($(this).css("background-color") === "rgb(255, 140, 0)"){
                    return;
                }
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
            $(".vote").mouseenter(function(){
                if($(this).css("background-color") === "rgb(52, 124, 245)"){
                    $(this).css("background-color","#2B6AD3")
                }  
            })
            $(".vote").mouseleave(function(){
                if($(this).css("background-color") === "rgb(43, 106, 211)"){
                    $(this).css("background-color","#347CF5");
                }
            })
            $(".card").on('click', function(e){
                console.log(e.target.className)
                if (e.target.className === 'vote'){
                    return;
                } 
                if (e.target.className === 'edit btn btn-primary'){
                    return;
                }
                var cardID = parseInt(this.id)
                var res = null
                for (let i in results){
                    if(results[i]["number"] === cardID){
                        res = results[i]
                        break;
                    }
                }
                console.log(res)
                var imgurl = "url(" + res["img"] + ")"
                $('#view-modal-body').css("background-image", imgurl)
                $('#viewTitle').html(res["model"])
                $('#viewDesc').html(res["movement"])
                if(login === 'false'){
                    $("#msg").hide()
                    $("#send").hide()
                }
                else{
                    $("#msg").show()
                    $("#send").show()
                }
                if(res["messages"] != null){
                    loadComments(cardID)
                }
                else{
                    $("#viewComments").html("<h4>No comments yet!</h4>");
                }
                $('#viewModal').modal('show')
                $(cardID).css("background-color","darkgray")
            })
            $(".card").hover(
                function(){
                    $(this).css('transform', 'scale(1.1)');
                },
                function(){$(this).css('transform', 'scale(1)')}
            )
            $("#loginButton").on('click', function(e){
                var username = $("#username").val();
                if (username != ""){
                    $.ajax({
                        type: "POST",
                        url: "",                
                        dataType : "json",
                        contentType: "application/json; charset=utf-8",
                        data : JSON.stringify({"login": username}),
                        success: function(data){
                            if (data["login"]==true){
                                login = username
                                $("#login").html("Welcome, " + username)
                            }
                            else {
        
                            }
                            if (data["admin"]==true){
                                admin = true
                            }
                            display_results(results)
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
            $(".edit").on('click', function(e){
                console.log(this.id.substring(4))
                var cardID = parseInt(this.id.substring(4))
                number = cardID
                var res = null
                for (let i in results){
                    if(results[i]["number"] === cardID){
                        res = results[i]
                        break;
                    }
                }
                console.log(res)
                var imgurl = "url(" + res["img"] + ")"
                $('#editTitle').attr('value',res["model"])
                $('#editDesc').html(res["movement"])
                $('#editImg').attr('value',res["img"])
                $('#edit-modal-body').css("background-image", imgurl)
                $('#editModal').modal('show')
            })
            $("#updateImg").on('click', function(e){
                var imgurl = "url(" + $('#editImg').val() + ")"
                $('#edit-modal-body').css("background-image", imgurl)
            }
            )
            $("#updateImg2").on('click', function(e){
                var imgurl = "url(" + $('#editImg').val() + ")"
                $('#new-modal-body').css("background-image", imgurl)
            }
            )
        }
        )
    }
}