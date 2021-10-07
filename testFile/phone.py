import requests, re

def ph(list):
  phone_reg = r'(?:0|886-?)9\d{2}(?:\d{6}|-\d{6}|-\d{3}-\d{3}?)'
  hm_reg = r'(\d{4}-\d{7}|\d{3}-\d{8})'
# OK
  html = requests.get(list).text

  phones = re.findall(phone_reg, html)
  hms = re.findall(hm_reg, html)

  i = 0
  for phone in phones:
    i += 1
    print("{} :{}".format(i, phone))
  for hm in hms:
    i += 1
    print("{} :{}".format(i, hm))