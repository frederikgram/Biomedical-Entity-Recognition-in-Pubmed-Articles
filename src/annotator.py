import sys, tty, termios, os, json
from extract_titles import fetch_article_titles
from typing import Dict

def getch() -> str:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def pinfo():
    os.system("clear")
    print("1 = compound, 2 = ignore, q = quit")


def annotate() -> Dict[str, int]:

    compounds = dict()

    if os.path.isfile("../data/compound_tags.json"):
        compounds = json.load(open("../data/compound_tags.json", 'r'))
        print("loaded compounds from file")
    else:
        print("no saved compound tags found, creating new json file")

    input("press any key to start tagging")

    for title in fetch_article_titles():

        i = 0
        words = title.split(' ')
        while (i < len(words)):
            word = words[i] 
            
            if word in list(compounds.keys()):
                i += 1
                continue
            
            pinfo() 
            print(f"  '{word}'   ") 

            inp = getch()
            if inp not in ["1", "2", "q"]:
                print("Invalid action: " + inp)
                input("press enter to ignore")
                continue 
            elif inp == 'q':
                return compounds
        
            else:
                compounds[word] = int(inp)
                i += 1
    return compounds

# bad code, doesn't matter for a temp text processing script
os.system("clear")
compounds = annotate()
os.system("clear")
[print(f"{key}: {'compound' if value == 1 else 'ignore'} ") for key, value in compounds.items()]
print(f"  >>  Finished tagging {len(list(compounds.keys()))} tokens")
json.dump(compounds, open("../data/compound_tags.json",'w'))
print(f"  >>  Saved tags in '../data/compound_tags.json'")
