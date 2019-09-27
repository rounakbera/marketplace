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
        "img": [
            "https://cdn.shopify.com/s/files/1/0044/0863/9561/products/Rolex_Gents_c._1998_Stainless_Submariner_7_425_525-0071_2000x.JPG?v=1538407695",
            "https://cdn2.chrono24.com/images/uhren/images_78/s6/7782678_xxl.jpg?v=1540826328588"
        ],
        "messages": [
            "rounakbera@gmail.com",
            "Hi, I'd like to buy this watch."
        ]
    },
    {
        "number": 1,
        "id": "Luke",
        "movement": "automatic",
        "model": "Rolex Day-Date II",
        "price": 4800,
        "img": [
"https://img-static.tradesy.com/item/23415832/rolex-day-date-ii-president-ii-18k-rose-gold-ref-218235-box-watch-0-1-960-960.jpg",
            "https://www.crmjewelers.com/wp-content/uploads/218235BKCAP_7.jpg"
        ],
        "messages": [
            "Would you be willing to go lower on the price?"
        ] 
    },
    {
        "number": 2,
        "id": "Raymond",
        "movement": "automatic",
        "model": "Breitling Navitimer",
        "price": 5900, 
        "img": [
            "https://cdn2.jomashop.com/media/catalog/product/b/r/breitling-navitimer-1-chronograph-automatic-silver-dial-mens-watch-a13324121g1x1--.jpg"
        ],
    },
    {
        "number": 3,
        "id": "Rounak",
        "movement": "automatic",
        "model": "IWC Portofino",
        "price": 3200,
        "img": [
            "https://b34959663f5a3997bd0d-2668915a1d3a077262c88fab6aa0aa02.ssl.cf3.rackcdn.com/17810324_1_640.jpg"
        ],
    },
    {
        "number": 4,
        "id": "Luke",
        "movement": "automatic",
        "model": "Breitling Superocean",
        "price": 6000,
        "img": [
            "https://www.ablogtowatch.com/wp-content/uploads/2019/03/Breitling-Superocean-Automatic-11-e1553206425585.jpg",
            "https://cdn2.chrono24.com/images/uhren/images_12/s3/10008312_xxl.jpg?v=1546855671515"
        ], 
    },
    {
        "number": 5,
        "id": "Raymond",
        "movement": "quartz",
        "model": "Grand Seiko SBGV207",
        "price": 4500, 
        "img": [
            "https://cdn2.chrono24.com/images/uhren/images_92/s2/7326292_xxl.jpg?v=1541918049439"
        ], 
    },
    {
        "number": 6,
        "id": "Arsalaan",
        "movement": "quartz",
        "model": "Citizen Eco-Drive One",
        "price": 1500,
        "img":[
            "https://i.ytimg.com/vi/p9l38pGu9w4/maxresdefault.jpg"
        ]
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
        "price": 1200,
        "img":[
            "https://www.ablogtowatch.com/nomos-club-campus-watches/nomos-glashutte-club-campus-ablogtowatch-9/"
        ]
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
        "price": 1800,
        "img":[
            "https://cdn2.chrono24.com/images/uhren/images_99/s4/7568499gross.jpg?v=1"
        ]
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
        "price": 1100,
        "img":[
            "https://www.fratellowatches.com/wp-content/uploads/2019/08/Hamilton-Khaki-Pilot-Pioneer-Mechanical-7-of-10-975x650.jpg"
        ]  
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


# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/', methods=['GET','POST'])
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
        print(results)
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
        if json.get("username") != None and json.get("number") == None and json.get("model") == None:
            results = []
            username = json.get("username")
            for w in watches:
                if w["id"] == username:
                    results.append(w)
                    print("getting " + str(w))
            return jsonify(results)
        elif json.get("number") != None and json.get("model") != None:
            num = int(json.get("number"))
            for w in watches:
                if w["number"] == num:
                    w["model"] = json.get("model")
                    w["movement"] = json.get("movement")
                    w["price"] = json.get("price")
            results = []
            username = json.get("username")
            for w in watches:
                if w["id"] == username:
                    results.append(w)
                    print("getting " + str(w))
            return jsonify(results)
        elif json.get("number") != None and json.get("username") == None:
            num = int(json.get("number"))
            print("deleting" + str(num))
            for w in watches:
                print(w["number"])
                if w["number"] == num:
                    watches.remove(w)
                    print('removed')
            return jsonify(watches)
        elif json.get("number") == None and json.get("model") != None:
            num = watches[len(watches)-1]["number"] + 1
            watches.append({
                "number": num,
                "model": json.get("model"),
                "movement": json.get("movement"),
                "price": json.get("price"),
                "id": json.get("username")
            })
            return jsonify(watches[len(watches)-1])        
        else:
            return jsonify([])
    else:
        return render_template('sell.html', results="", username = "", number = -1)

if __name__ == '__main__':
   app.run(debug=True)