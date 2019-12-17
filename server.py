import json

from flask import Flask, Response, jsonify, render_template, request

app = Flask(__name__)

term = ""
username = ""
number = -1
users = {
    "Rounak": True,
    "Raymond": False,
    "Luke": False,
    "Manav": False,
    "Matt": True,
    "Maria": False
}

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/', methods=['GET','POST','PUT','DELETE'])
def search():
    global watches
    global term
    with open('data.json') as f:
        watches = json.load(f)
    term = request.args.get('term', None)
    jsons = request.get_json()
    if jsons != None:
        with open('data.json') as f:
            watches = json.load(f)
        if jsons.get("votes") != None:
            num = int(jsons.get("number"))
            for w in watches:
                if w["number"] == num:
                    w["votes"] = jsons.get("votes")
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            return json.dumps(allsearch(""))
        elif jsons.get("msg") != None:
            num = int(jsons.get("number"))
            for w in watches:
                if w["number"] == num:
                    if "messages" not in w.keys():
                        w["messages"] = [jsons.get("msg")]
                    else:
                        w["messages"].append(jsons.get("msg"))
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            return json.dumps(allsearch(""))
        elif jsons.get("edit") != None:
            num = int(jsons.get("number"))
            for w in watches:
                if w["number"] == num:
                    w["model"] = jsons.get("model")
                    w["movement"] = jsons.get("movement")
                    w["img"] = jsons.get("price")
            print("hello4")
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            print("hello5")
            return json.dumps(allsearch(""))
        elif jsons.get("new") != None:
            with open('data.json') as f:
                watches = json.load(f)
            num = watches[len(watches)-1]["number"] + 1
            watches.append({
                "number": num,
                "model": jsons.get("model"),
                "movement": jsons.get("movement"),
                "img": jsons.get("price"),
                "id": jsons.get("username"),
                "votes": 0
            })
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            return json.dumps(allsearch(""))
        elif jsons.get("delete") != None:
            with open('data.json') as f:
                watches = json.load(f)
            for w in watches:
                if w["number"] == jsons.get("number"):
                    watches.remove(w)
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            return json.dumps(allsearch(""))
        elif jsons.get("login"):
            use = jsons.get("login")
            if use in users and users[use]:
                return jsonify({"login":True,"admin":True})
            elif use in users and not users[use]:
                return jsonify({"login":True,"admin":False})
            else:
                return jsonify({"login":True,"admin":False})
        else:
            with open('data.json') as f:
                watches = json.load(f)
            num = int(jsons.get("number"))
            print("deleting" + str(num))
            for w in watches:
                print(w["number"])
                if w["number"] == num:
                    watches.remove(w)
                    print('removed')
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            return jsonify(watches)
    if term != None:
        results = allsearch(term)
        return render_template('search.html', results=results, term = term, number = -1)
    else:
        result=allsearch("")
        return render_template('search.html', results=result, term = "", number = -1)

def allsearch(var2):
    global watches
    global term
    with open('data.json') as f:
        watches = json.load(f)
    if var2 == "":
        print("hello2")
        results = list(sorted(watches, key = lambda i: i["votes"],reverse=True))
        print("hello3")
        print(type(results))
        return(results)
    filtered = list(filter(searching, watches))
    resulted = sorted(filtered, key = lambda i: i["votes"],reverse=True)
    listresult = list(resulted)
    return listresult

def searching(var):
    global term
    term = term.lower()
    if var["movement"].lower().find(term) > -1 or var["model"].lower().find(term) > -1:
        return True
    else:
        return False

# @app.route('/sell', methods=['GET','POST'])
# def sell():
#     global watches
#     global username
#     global number
#     with open('data.json') as f:
#         watches = json.load(f)
#     jsons = request.get_json()
#     if jsons != None:
#         if jsons.get("username") != None and jsons.get("number") == None and jsons.get("model") == None:
#             with open('data.json') as f:
#                 watches = json.load(f)
#             results = []
#             username = jsons.get("username")
#             for w in watches:
#                 if w["id"] == username:
#                     results.append(w)
#                     print("getting " + str(w))
#             return jsonify(results)
#         elif jsons.get("number") != None and jsons.get("model") != None:
#             with open('data.json') as f:
#                 watches = json.load(f)
#             num = int(jsons.get("number"))
#             for w in watches:
#                 if w["number"] == num:
#                     w["model"] = jsons.get("model")
#                     w["movement"] = jsons.get("movement")
#                     w["img"] = jsons.get("price")
#             with open('data.json', 'w') as f:
#                 json.dump(watches, f)
#             results = []
#             username = jsons.get("username")
#             for w in watches:
#                 if w["id"] == username:
#                     results.append(w)
#                     print("getting " + str(w))
#             print(str(results))
#             return jsonify(results)
#         elif jsons.get("number") != None and jsons.get("username") == None:
#             with open('data.json') as f:
#                 watches = json.load(f)
#             num = int(jsons.get("number"))
#             print("deleting" + str(num))
#             for w in watches:
#                 print(w["number"])
#                 if w["number"] == num:
#                     watches.remove(w)
#                     print('removed')
#             with open('data.json', 'w') as f:
#                 json.dump(watches, f)
#             return jsonify(watches)
#         elif jsons.get("number") == None and jsons.get("model") != None:
#             with open('data.json') as f:
#                 watches = json.load(f)
#             num = watches[len(watches)-1]["number"] + 1
#             watches.append({
#                 "number": num,
#                 "model": jsons.get("model"),
#                 "movement": jsons.get("movement"),
#                 "img": jsons.get("price"),
#                 "id": jsons.get("username"),
#                 "votes": 0
#             })
#             with open('data.json', 'w') as f:
#                 json.dump(watches, f)
#             return jsonify(watches[len(watches)-1])        
#         else:
#             return jsonify([])
#     else:
#         return render_template('sell.html', results="", username = "", number = -1)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug='true')
