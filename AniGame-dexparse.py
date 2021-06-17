import sys.argv as argv
import argparse
from pathlib import Path

def char2csv(chara: str):
    elems = {}
    talents = {}
    chara.replace(": :", ":")
    info, stats = chara.split("\n")
    name, element, talent = info.split(":")
    HP, ATK, DEF, SPD = stats.split(", ")
    name = name.strip()
    element = elems[element.strip().lower()]
    talent = talents[talent.strip().lower()]
    HP = HP.replace("HP: ", "").strip()
    ATK = ATK.replace("ATK: ", "").strip()
    DEF = DEF.replace("DEF: ", "").strip()
    SPD = SPD.replace("SPD: ", "").strip()
    return f"{name},{element},{HP},{ATK},{DEF},{SPD},{talent}\n"

def process_series(dex: str):
    invals = dex.replace("\r\n", "\n").split("\n\n")
    entries = []
    for chara in invals:
        entries.append(char2csv(chara))
    return entries

def main(infile: str, outfile: str):
    print("Welcome to the AniGame Dex Parser!")
    stdin = ["input", "stdin", "read", "type", "user", "keyboard", "kbd"]
    stdout = ["output", "stdout", "cli", "print", "type", "dump"]
    if not infile or infile.lower() in stdin:
        data = input("Copy-paste a dex page here\n> ")
        infile = "stdin"
    else:
        with open(infile, "r") as i:
            data = i.read()
    print(f"Reading data from {infile}...")
    results = process_series(data)
    if outfile.lower() in stdout:
        for line in results:
            print(line)
        return
    with open(outfile, 'w+') as o:
        for line in results:
            o.write(line)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process AniGame dex entries")
    parser.add_argument("--input", "-i", "--infile", allow_abbrev=False,
                        help="A path to a file, or blank to specify later.")
    parser.add_argument("--output", "-o", "--outfile", allow_abbrev=False,
                        default="./output.csv",
                        help="A path to an outfile, blank for ./output.csv")
    args = parser.parse_args()
    main(infile=args.input, outfile=args.output)
    print("All done, enjoy!")