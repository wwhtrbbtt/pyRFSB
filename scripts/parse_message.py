from json import loads
import html
from bs4 import BeautifulSoup
from time import ctime


class rank_colors:
    """
    the ranks on the website are colored. Why not 
    color them here too? You can switch them around if you want
    """
    rf_elite = '\033[95m'   # pink
    rf_vip = '\033[94m'     # purple
    rf_member = '\033[96m'  # cyan
    rf_noob = '\033[90m'    # grey
    rf_god = '\033[93m'     # gold
    rf_admin = '\033[91m'   # red
    rf_mvp = '\033[97m'     # white
    rf_tryhard = '\033[1m'  # bold white
    rf_uber = '\033[2m'     # idk
    rf_leet = '\033[4m'     # idk
    ENDC = '\033[0m'        # at the end of every message


def get_rank_color(x):
    if x == "noob":
        return rank_colors.rf_noob
    elif x == "elite":
        return rank_colors.rf_elite
    elif x == "vip":
        return rank_colors.rf_vip
    elif x == "mvp":
        return rank_colors.rf_mvp
    elif x == "mp":
        return rank_colors.rf_mvp
    elif x == "god":
        return rank_colors.rf_god
    elif x == "admin":
        return rank_colors.rf_admin
    elif x == "a":
        return rank_colors.rf_admin
    elif x == "tryhard":
        return rank_colors.rf_tryhard
    elif x == "uber":
        return rank_colors.rf_uber
    elif x == "member":
        return rank_colors.rf_member
    elif x == "leet":
        return rank_colors.rf_leet
    else:
        print(x)
        return False


def parse_message(raw: str, LOG) -> None:
    data = raw[21:-1]
    try:
        rank = data.split("\|")[0].split('"')[-1].replace('rf_', '').replace(
            'i ', '')
        msg = data.split('"msg":"')[1].split('","nickto":"')[0]

        ##### PARSING RANK COLOR
        if rank.count(" ") == 1:
            ranks = rank.split(" ")
            for x in ranks:
                rankColor = get_rank_color(x)
                if rankColor != False:
                    break

        elif rank.count(" ") == 0:
            rankColor = get_rank_color(rank)

        else:
            print(rank.split(" "))
            rankColor = rank_colors.rf_elite

        soup = BeautifulSoup(data, features="lxml")
        name = soup.get_text().split('"nick":"')[1].split('","')[0]

        print(f"{rankColor}[{rank}] {name}\033[0m: {msg}")
        if LOG:
            with open("log.txt", "a") as f:
                f.write(f"{ctime()}: [{rank}] {name}: {msg}" + "\n")

    except:
        print("Error parsing the message.")


def parse(raw, LOG, DEBUG=False):
    raw = raw.replace('class="', "class=|")
    raw = raw.replace('">', "|>")
    raw = html.unescape(raw)

    if raw.startswith('42/member,["message"'):
        if DEBUG:
            print(raw)
        """
        New message
        """
        
        parse_message(raw, LOG)
# TODO: implement the other packets.
# Maybe a /members or something so see online members?
# This would require to keep track of difficult stuff
