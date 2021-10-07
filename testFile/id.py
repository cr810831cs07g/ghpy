import requests, re
def id(url):
    id_reg = "[a-zA-z][12][0-9]{8}"

    html = requests.get(url).text
    result = re.findall(id_reg, html)
    i = 0
    for results in result:
        i += 1
        print("{} :{}".format(i, results))
    