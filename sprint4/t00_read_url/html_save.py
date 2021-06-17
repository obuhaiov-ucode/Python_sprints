import re
import requests
from helper import print_stderr, print_stdout

def html_save(url: str, file: str):
    pattern = r"^(http:\/\/|https:\/\/)" \
              "\-?\w+(?:(\.|:)\-?\w+)+" \
              "(?:(\/|#|\?|=|&|\-|\(|\)|\.|\w+))*$"

    if isinstance(url, str) and isinstance(file, str)\
            and re.match(pattern, url):
        try:
            print_stdout(f"Sending the request to the '{url}'")
            req = requests.get(url)

            print_stdout(f"Request to the '{url}' has been sent")
            print_stdout(f"<Response [{str(req.status_code)}]>")

            if req.status_code != requests.codes.ok:
                print_stderr(f"Request failed")
            else:
                print_stdout("Parsing page data")
                tmp = str(req.text)
                print_stdout("Page data has been parsed")

                with open(file, 'w') as f:
                    print_stdout(f"Saving page data to '{file}'")
                    f.write(tmp)
                    print_stdout(f"Page data has been saved")

        except requests.exceptions.RequestException as e:
            print_stderr(str(e))
            return
        except FileNotFoundError as e:
            print_stderr(str(e))
            return
    else:
        print_stderr("The site URL format is invalid")
