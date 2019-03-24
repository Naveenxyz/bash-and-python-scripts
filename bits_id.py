import requests
from bs4 import BeautifulSoup

url = "http://id.bits-hyderabad.ac.in/moodle/login/index.php"
s = requests.Session()
# *** should be actual password xP
payload = {'username': 'f2016089', 'password': 'prjwl82&&'}
r = s.post(url, data=payload)
# print(r.status_code)
url2 = "http://id.bits-hyderabad.ac.in/moodle/my/index.php?mynumber=-2"
r = s.get(url2)
soup = BeautifulSoup(r.content, "lxml")
# print(soup.prettify())
f = open("courses.txt", "w")
for a in soup.find_all("h2", class_="title"):
    s = str(a.contents[0].contents)
    f.write((s[2:-2]+"\n"))
    # print(a)
