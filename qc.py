import argparse, re

def pre_process(q : str):
    return re.sub(r"[^a-zA-Z0-9\s'?!,.]", r"", q)

def remove_extra_spaces(q : str):
    return re.sub(r"\s\s+", r" ", q)

def remove_space_before_apost(q : str):
    return re.sub(r"\s'", r"'", q)

def remove_endline_char(q : str):
    return re.sub(r"\n", r"", q)

def execute():
    pass

def main(fpath : str):
    file = open(fpath, "r")
    for line in file:
        processed = remove_endline_char(
                remove_space_before_apost(
                    remove_extra_spaces(
                        pre_process(line))))
        print("Before:({})\nAfter:({})"
                .format(line, processed))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fpath", type=str,
                        help="path to input file")
    args = parser.parse_args()
    main(args.fpath)
