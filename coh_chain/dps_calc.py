import re
import time
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("c:/Users/norma/OneDrive/Documents/t/nomwnom/logs/chatlog 2020-09-18.txt")

DT_FORMAT = "%Y-%m-%d %H:%M:%S"
DMG_LINE_RE = re.compile(r"^(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<toon>\w+) hit.* (?P<damage>\d+\.\d+)")
ACTIVATION_LINE_RE = re.compile(r"^(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")


class DpsTotal:
    def __init__(self):
        self.total_damage = 0



def main():

    total_dmg = 0
    start_time = None

    with open(LOG_FILE) as file:
        while 1:
            where = file.tell()
            line = file.readline().rstrip()
            if not line:
                time.sleep(1)
                file.seek(where)
            elif start_time is None and "You activated" in line:
                # We start the timer with the first power activation
                dt_string = re.match(ACTIVATION_LINE_RE, line).group("datetime")
                start_time = dt_from_string(dt_string)
                print(f"Timer starting at {start_time}")
            elif "You hit" in line and "damage" in line:
                if start_time is None:
                    continue
                re_match = re.match(DMG_LINE_RE, line)
                if re_match:
                    current_time = dt_from_string(re_match.group("datetime"))
                    #toon = re_match.group("toon")
                    dmg = re_match.group("damage")
                    total_dmg += float(dmg)
                    ellapsed_time = (current_time - start_time).total_seconds()
                    if ellapsed_time >0:
                        print(f"Current DPS: {total_dmg / ellapsed_time}")
            elif "RESETDPS" in line:
                print("RESETTING DPS COUNTER!!!")
                total_dmg = 0
                start_time = None

def dt_from_string(dt_string):
    return datetime.strptime(dt_string, DT_FORMAT)

if __name__ == "__main__":
    main()