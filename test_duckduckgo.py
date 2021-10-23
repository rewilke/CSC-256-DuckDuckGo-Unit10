import requests

def test_duckduckgo_presidents():

    query          = "presidents of the united states"
    topic_list     = requests.get("https://api.duckduckgo.com/?q=" + query + "&format=json").json()["RelatedTopics"]
    president_list = [
        "Adams",
        "Arthur",
        "Biden",
        "Buchanan",
        "Buren",
        "Bush",
        "Carter",
        "Cleveland",
        "Clinton",
        "Coolidge",
        "Eisenhower",
        "Fillmore",
        "Ford",
        "Garfield",
        "Grant",
        "Harding",
        "Harrison",
        "Hayes",
        "Hoover",
        "Jackson",
        "Jefferson",
        "Johnson",
        "Kennedy",
        "Lincoln",
        "Madison",
        "McKinley",
        "Monroe",
        "Nixon",
        "Obama",
        "Pierce",
        "Polk",
        "Reagan",
        "Roosevelt",
        "Taft",
        "Taylor",
        "Truman",
        "Trump",
        "Tyler",
        "Washington",
        "Wilson"
    ]

    for president in president_list:
        found = False

        for topic in topic_list:
            if president in topic["Text"]:
                found = True
                break

        if not found:
            assert False

    assert True
