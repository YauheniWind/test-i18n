import os
from bs4 import BeautifulSoup

tags_to_check = ["p", "button", "h2", "h"]


def check_tag(tag_list, mark, path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line_num, line in enumerate(lines, start=1):
            for tag in tag_list:
                if tag in line:
                    soup = BeautifulSoup(line, "lxml")
                    for element in soup.find_all(tag):
                        if not element.has_attr(mark):
                            print(
                                f"Tag {tag} not contain {mark} in file {os.path.abspath(path)} at line {line_num}: {element}"
                            )
