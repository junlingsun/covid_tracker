from flask import Flask
from flask import request
from flask import render_template
import time
import service
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/ajax", methods=["post"])
def ajax():
    return "result";


@app.route("/time", methods=["get"])
def time():
    return service.getTime()


@app.route("/c1")
def get_c1_data():
    data = service.get_c1_data()
    return jsonify({"positive": data[0], "death": data[1], "positive_increase": data[2], "death_increase": data[3]})


@app.route("/c2")
def get_c2_data():
    states = {
        "AL": "Alabama",
        "AK": "Alaska",
        "AS": "American Samoa",
        "AZ": "Arizona",
        "AR": "Arkansas",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "DC": "District Of Columbia",
        "FM": "Federated States Of Micronesia",
        "FL": "Florida",
        "GA": "Georgia",
        "GU": "Guam",
        "HI": "Hawaii",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "IA": "Iowa",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "ME": "Maine",
        "MH": "Marshall Islands",
        "MD": "Maryland",
        "MA": "Massachusetts",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MS": "Mississippi",
        "MO": "Missouri",
        "MT": "Montana",
        "NE": "Nebraska",
        "NV": "Nevada",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NY": "New York",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "MP": "Northern Mariana Islands",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PW": "Palau",
        "PA": "Pennsylvania",
        "PR": "Puerto Rico",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VT": "Vermont",
        "VI": "Virgin Islands",
        "VA": "Virginia",
        "WA": "Washington",
        "WV": "West Virginia",
        "WI": "Wisconsin",
        "WY": "Wyoming"
    }
    data = service.get_c2_data()
    response = []
    for d in data:
        dict = {}
        dict['name'] = states.get(d[0])
        dict['value'] = d[1]
        response.append(dict)

    return jsonify({"response": response})


@app.route("/l1")
def get_l1_data():
    data = service.get_l1_data()
    legend = ["positive", "death"]
    x_data = []
    positive_data = []
    death_data = []

    for d in reversed(data):
        date = d[0].strftime("%m-%d")
        positive = d[1]
        death = d[2]
        x_data.append(date)
        positive_data.append(positive)
        death_data.append(death)

    return jsonify({"legend": legend, "x_data": x_data, "positive_data": positive_data, "death_data": death_data})


@app.route("/l2")
def get_l2_data():
    data = service.get_l2_data()
    legend = ["positive_increase", "death_increase"]
    x_data = []
    positive_data = []
    death_data = []

    for d in reversed(data):
        date = d[0].strftime("%m-%d")
        positive_increase = d[1]
        death_increase = d[2]
        x_data.append(date)
        positive_data.append(positive_increase)
        death_data.append(death_increase)

    return jsonify({"legend": legend, "x_data": x_data, "positive_data": positive_data, "death_data": death_data})

@app.route("/r1")
def get_r1_data():
    data = service.get_r1_data()
    names = []
    positive = []
    for d in data:
        names.append(d[0])
        positive.append(d[1])

    return jsonify({"names": names, "positive": positive})


if __name__ == '__main__':
    app.run(threaded=True)
