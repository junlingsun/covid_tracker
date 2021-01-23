import requests
import json
import time


def data_fetch():
    # collect cumulative data of usa for each day
    url = "https://api.covidtracking.com/v1/us/daily.json"
    response = requests.get(url)
    data_all = json.loads(response.text)

    us_data = {}
    for data in data_all:
        date = str(data["date"])
        date = time.strptime(date, "%Y%m%d")
        date = time.strftime("%Y-%m-%d", date)
        positive = data["positive"]
        death = data["death"]
        death_increase = data["deathIncrease"]
        positive_increase = data["positiveIncrease"]
        us_data[date] = {"positive": positive, "death": death, "death_increase": death_increase,
                         "positive_increase": positive_increase}

    # collect cumulative data of each tate for each day
    url = "https://api.covidtracking.com/v1/states/daily.json"
    response = requests.get(url)
    data_all = json.loads(response.text)

    states_data = []
    for data in data_all:
        date = str(data["date"])
        date = time.strptime(date, "%Y%m%d")
        date = time.strftime("%Y-%m-%d", date)

        positive = data["positive"]
        death = data["death"]
        state = data["state"]
        states_data.append({"date": date, "state": state, "positive": positive, "death": death})



    return us_data, states_data


if __name__ == "__main__":
    data_fetch()