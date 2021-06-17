import requests
import json
import sys
import re
from bs4 import BeautifulSoup

if __name__ == "__main__" and len(sys.argv) == 2:
    all_dicts = []
    url = sys.argv[1]
    req = requests.get(url).content
    soup = BeautifulSoup(req, "html.parser")
    url_pattern = r"^(http:\/\/|https:\/\/)" \
              "\-?\w+(?:(\.|:)\-?\w+)+" \
              "(?:(\/|#|\?|=|&|\-|\(|\)|\.|\w+))*$"

    all_a = soup.find_all("a", class_="reference external", href=re.compile(url_pattern))
    for a in all_a:
        text = a.contents[0]
        href = a['href']

        req_title = requests.get(a['href']).content
        new_soup = BeautifulSoup(req_title, "html.parser")

        title = new_soup.title
        if title:
            title = new_soup.title.text
        all_dicts.append({"link_text": text, "url": href, "title": title})

    heading = re.sub(r"[^\w\s]", "", soup.find("h1").text)
    heading = re.sub(r"\s", "_", heading) + '.json'
    with open(heading, 'w') as f:
        json.dump(all_dicts, f, sort_keys=False, indent=1, ensure_ascii=False)
