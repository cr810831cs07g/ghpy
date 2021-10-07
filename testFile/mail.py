import requests, re
def ma(url):

  regex = r"([a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

  html = requests.get(url).text
  emails = re.findall(regex, html)
  i = 0
  for email in emails:
    i += 1
    print("{} :{}".format(i, email))