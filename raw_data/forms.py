import json, requests
def forms (s_input): # s is string
    url = "https://ws3.morpher.ru/russian/declension"
    params = dict (
    s=s_input,
    format="json"
    )
    response = requests.get(url=url, params=params)
    data = json.loads(response.text)
    keys = []
    for acc, key in data.items():
        keys += [key]
    keys.pop(-1)
    return (list(set(keys)))
