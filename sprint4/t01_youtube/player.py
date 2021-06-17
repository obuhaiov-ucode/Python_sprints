import re
import sys
import webbrowser
from helper import print_stderr, print_stdout

if __name__ == '__main__':
    pattern = r"^https:\/\/www\.youtube\.com(?:(\/|#|\?|=|&|\-|\(|\)|\w+))*$"

    if len(sys.argv) > 1 and isinstance(sys.argv[1], str) \
            and re.match(pattern, sys.argv[1]):
        print_stdout(f"Opening the YouTube video at {sys.argv[1]}")
        webbrowser.open_new_tab(sys.argv[1])
        print_stdout(f"YouTube video opened")
    elif len(sys.argv) == 1:
        print_stderr("The site URL was not passed")
    else:
        print_stderr("The URL is invalid")
