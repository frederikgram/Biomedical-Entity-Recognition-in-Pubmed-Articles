""" """

import os
import json
from typing import List, Dict

def fetch_article_titles():

    base_path = "../data/raw/"
    filenames = os.listdir(base_path)

    # Ensure that only proper datatype are picked up
    filenames = [filename for filename in filenames if filename.split('.')[-1] == "txt"]

    titles = list()

    for filename in filenames:
    
        path = os.path.join(base_path, filename)
        with open(path, 'r') as f:
            data = f.read()
            title = data.split("<text>")[1].split("</text>")[0]
            titles.append(title)

    return titles



