import json

from flask import Flask, Response, jsonify, render_template, request

app = Flask(__name__)

term = ""
username = ""
number = -1
watches = [
    {
        "number": 0,
        "id": "Rounak",
        "movement": "Half the air conditioners on our floor in Schapiro have been broken for 5 weeks, and Housing hasn't responded to our emails. Could Spec report on this?",
        "model": "Broken Air Conditioners",
        "img": "https://f1.media.brightcove.com/8/1078702682/1078702682_5081417885001_1608DIY-AC-Still-2016-08-12-14-32.jpg?pubId=1078702682&videoId=5081414894001",
        "messages": [
            "Hi, we'd like to report on this. Email Rounak Bera at rounak.bera@columbiaspectator.com and we'll move forward."
        ],
        "votes": 10
    },
    {
        "number": 1,
        "id": "Luke",
        "movement": "It would be useful for us to have a campus-wide calendar with public events listed on it. Maybe even an app to make it more accessible",
        "model": "Event Calendar?",
        "img": "https://staticx.ibncollege.com/wcsstore/ExtendedSitesCatalogAssetStore/706_100_20_347318721_NI/images/LARGEIMAGE_1661950.jpg",
        "votes": 8
    },
    {
        "number": 2,
        "id": "Raymond",
        "movement": "A rundown of how to apply for journalism internships would be really useful for the writing-oriented community at Columbia.",
        "model": "Journalism Internship Panel",
        "img": "https://cdn.newsday.com/polopoly_fs/1.7924552.1399309530!/httpImage/image.jpg_gen/derivatives/landscape_768/image.jpg",
        "votes": 6
    },
    {
        "number": 3,
        "id": "Raymond",
        "movement": "Many of the walls in EC suites have been growing mold, and we've seen no response from Housing.",
        "model": "Mold on walls of EC Suites",
        "img": "https://www.mold-advisor.com/images/mold-walls-ceiling.jpg",
        "votes": 5
    },
    {
        "number": 4,
        "id": "Rounak",
        "movement": "Hi! CSI will be launching a research mission in December of this year; we were wondering if someone from Spec could report on it?",
        "model": "Columbia Space Initiative Mission Launch",
        "img": "https://www.blueorigin.com/assets/BlueOrigin_NewShepard_Launch.jpg",
        "votes": 4
    },
    {
        "number": 5,
        "id": "Rounak",
        "movement": "Upperclassmen have lots of notes they've taken for classes in previous years; students could compile a set of notes for the most common classes and share for everyone to use.",
        "model": "Study Guide Database",
        "img": "https://external-preview.redd.it/z5cGF_fT0GZ7m_zUwkHUcc5fdNnBNNyc4Qxoi_dSu2w.jpg?auto=webp&s=80c7eb874aac831a356f87fac0cc7cef5f106ad4",
        "votes": 1
    }
]


# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/', methods=['GET','POST'])
def search():
    global watches
    global term
    with open('data.json') as f:
        watches = json.load(f)
    term = request.args.get('term', None)
    jsons = request.get_json()
    if jsons != None:
        if jsons.get("votes") != None:
            num = jsons.get("number")
            for w in watches:
                if w["number"] == num:
                    w["votes"] = jsons.get("votes")
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            return jsonify(watches)
        else:
            num = jsons.get("number")
            for w in watches:
                if w["number"] == num:
                    if "messages" not in w.keys():
                        w["messages"] = [jsons.get("msg")]
                    else:
                        w["messages"].append(jsons.get("msg"))
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            return jsonify(watches)
    if term != None:
        results = list(sorted(list(filter(searching, watches)), key = lambda i: i["votes"],reverse=True))
        print(results)
        return render_template('search.html', results=results, term = term, number = -1)
    else:
        results = list(sorted(watches, key = lambda i: i["votes"],reverse=True))
        return render_template('search.html', results=results, term = "", number = -1)

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
    jsons = request.get_json()
    if jsons != None:
        if jsons.get("username") != None and jsons.get("number") == None and jsons.get("model") == None:
            results = []
            username = jsons.get("username")
            for w in watches:
                if w["id"] == username:
                    results.append(w)
                    print("getting " + str(w))
            return jsonify(results)
        elif jsons.get("number") != None and jsons.get("model") != None:
            num = int(jsons.get("number"))
            for w in watches:
                if w["number"] == num:
                    w["model"] = jsons.get("model")
                    w["movement"] = jsons.get("movement")
                    w["img"] = jsons.get("price")
            with open('data.json', 'w') as f:
                json.dump(watches, f)
            results = []
            username = jsons.get("username")
            for w in watches:
                if w["id"] == username:
                    results.append(w)
                    print("getting " + str(w))
            print(str(results))
            return jsonify(results)
        elif jsons.get("number") != None and jsons.get("username") == None:
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
        elif jsons.get("number") == None and jsons.get("model") != None:
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
            return jsonify(watches[len(watches)-1])        
        else:
            return jsonify([])
    else:
        return render_template('sell.html', results="", username = "", number = -1)

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug='true')
