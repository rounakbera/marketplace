from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

term = ""
username = ""
number = -1
watches = [
    {
        "number": 0,
        "id": "Rounak",
        "movement": "automatic",
        "model": "Rolex Submariner",
        "price": 7500,
        "messages": [
            "hello",
            "hi"
        ] 
    },
    {
        "number": 1,
        "id": "Luke",
        "movement": "automatic",
        "model": "Rolex Day-Date II",
        "price": 4800,
        "messages": [
            "bye"
        ] 
    },
    {
        "number": 2,
        "id": "Raymond",
        "movement": "automatic",
        "model": "Breitling Navitimer",
        "price": 5900  
    },
    {
        "number": 3,
        "id": "Rounak",
        "movement": "automatic",
        "model": "IWC Portofino",
        "price": 3200  
    },
    {
        "number": 4,
        "id": "Luke",
        "movement": "automatic",
        "model": "Breitling Superocean",
        "price": 6000  
    },
    {
        "number": 5,
        "id": "Raymond",
        "movement": "quartz",
        "model": "Grand Seiko SBGV207",
        "price": 4500  
    },
    {
        "number": 6,
        "id": "Arsalaan",
        "movement": "quartz",
        "model": "Citizen Eco-Drive One",
        "price": 1500  
    },
    {
        "number": 7,
        "id": "Arsalaan",
        "movement": "automatic",
        "model": "Omega Speedmaster",
        "price": 3300 
    },
    {
        "number": 8,
        "id": "Kevin",
        "movement": "automatic",
        "model": "Rolex Datejust",
        "price": 2100  
    },
    {
        "number": 9,
        "id": "Luke",
        "movement": "automatic",
        "model": "Tudor Pelagos",
        "price": 3100  
    },
    {
        "number": 10,
        "id": "Rounak",
        "movement": "automatic",
        "model": "Nomos Glashütte Club Campus",
        "price": 1200  
    },
    {
        "number": 11,
        "id": "Kevin",
        "movement": "automatic",
        "model": "Junghans Max Bill Chronoscope",
        "price": 1500  
    },
    {
        "number": 12,
        "id": "Kevin",
        "movement": "quartz",
        "model": "Sinn UX",
        "price": 2000  
    },
    {
        "number": 13,
        "id": "Kevin",
        "movement": "automatic",
        "model": "Rolex Submariner",
        "price": 6600  
    },
    {
        "number": 14,
        "id": "Arsalaan",
        "movement": "quartz",
        "model": "Omega X-33",
        "price": 2200  
    },
    {
        "number": 15,
        "id": "Arsalaan",
        "movement": "quartz",
        "model": "Breitling Aerospace Evo",
        "price": 3400  
    },
    {
        "number": 16,
        "id": "Luke",
        "movement": "automatic",
        "model": "Rolex Daytona II",
        "price": 7200  
    },
    {
        "number": 17,
        "id": "Luke",
        "movement": "automatic",
        "model": "Rolex Oyster Perpetual",
        "price": 3400  
    },
    {
        "number": 18,
        "id": "Luke",
        "movement": "automatic",
        "model": "Tag Heuer Formula 1",
        "price": 1400  
    },
    {
        "number": 19,
        "id": "Rounak",
        "movement": "automatic",
        "model": "Longines Legend Diver",
        "price": 1800  
    },
    {
        "number": 20,
        "id": "Luke",
        "movement": "quartz",
        "model": "Omega Globemaster",
        "price": 7100  
    },
    {
        "number": 21,
        "id": "Rounak",
        "movement": "automatic",
        "model": "Hamilton Khaki Pilot Pioneer",
        "price": 1100  
    },
    {
        "number": 22,
        "id": "Rounak",
        "movement": "automatic",
        "model": "Stowa Flieger",
        "price": 950  
    },
    {
        "number": 23,
        "id": "Rounak",
        "movement": "automatic",
        "model": "Nomos Orion",
        "price": 1600  
    },
    {
        "number": 24,
        "id": "Kevin",
        "movement": "automatic",
        "model": "Oris Artelier Complications",
        "price": 1200  
    },
    {
        "number": 25,
        "id": "Luke",
        "movement": "automatic",
        "model": "Junghans & Meister Kalendar Moon",
        "price": 1900  
    },
    {
        "number": 26,
        "id": "Luke",
        "movement": "automatic",
        "model": "Nomos Tangomat",
        "price": 2600  
    },
    {
        "number": 27,
        "id": "Arsalaan",
        "movement": "automatic",
        "model": "Rolex Explorer II",
        "price": 3600  
    },
    {
        "number": 28,
        "id": "Luke",
        "movement": "automatic",
        "model": "Tudor Black Bay",
        "price": 2100  
    },
    {
        "number": 29,
        "id": "Raymond",
        "movement": "automatic",
        "model": "Rolex Datejust I",
        "price": 3300  
    }
]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET','POST'])
def search():
    global watches
    global term
    term = request.args.get('term', None)
    json = request.get_json()
    if json != None:
        num = json.get("number")
        for w in watches:
            if w["number"] == num:
                if "messages" not in w.keys():
                    w["messages"] = [json.get("msg")]
                else:
                    w["messages"].append(json.get("msg"))
        return jsonify(watches)
    if term != None:
        results = list(filter(searching, watches))
        return render_template('search.html', results=results, term = term, number = -1)
    else:
        return render_template('search.html', results=watches, term = "", number = -1)

def searching(var):
    global term
    term = term.lower()
    if var["movement"].lower().find(term) > -1 or var["model"].lower().find(term) > -1:
        return True
    else:
        return False

@app.route('/sell', methods=['GET','POST'])
def sell():
    global watches
    global username
    global number
    json = request.get_json()
    if json != None:
        if json.get("username") != None and json.get("number") != None:
            username = json.get("username")
            number = int(json.get("number"))
            for w in watches:
                if w["number"] == number:
                    if w["id"] == username:
                        results = w
                        print("getting " + str(w))
                        return jsonify(results)
            else:
                return jsonify([])
        elif json.get("username") != None:
            number = watches[-1]["number"] + 1
            watches.append({
                "number": number,
                "id": json.get("username"),
                "model": json.get("model"),
                "movement": json.get("movement"),
                "price": json.get("price")
            })
            print("creating " + str(watches[-1]))
            return jsonify(watches)
        elif json.get("model") != None:
            number = int(json.get("number"))
            for w in watches:
                if w["number"] == number:
                    w["model"] = json.get("model")
                    w["movement"] = json.get("movement")
                    w["price"] = json.get("price")
                    print("updating " + str(w))
            return jsonify(watches)
        elif json.get("number") != None:
            number = int(json.get("number"))
            for w in watches:
                if w["number"] == number:
                    print("deleting " + str(w))
                    watches.remove(w)
            return jsonify(watches)
        else:
            return jsonify([])
    else:
        return render_template('sell.html', results="", username = "", number = -1)

if __name__ == '__main__':
   app.run(debug=True)