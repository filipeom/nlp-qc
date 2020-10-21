import argparse, re


def pre_process(q : str):
    # FIXME: 
    #   1. `` ... '' -> " ... " ?
    #   2. ` ... ' -> ' ... ' ?

    def normalize(q : str):
        return re.sub(r"[^a-zA-Z0-9\s'?!,.]", r"", q)

    def remove_extra_spaces(q : str):
        return re.sub(r"\s\s+", r" ", q)

    def remove_space_before_apost(q : str):
        return re.sub(r"\s'", r"'", q)

    def remove_endline_char(q : str):
        return re.sub(r"\n", r"", q)

    return remove_endline_char(
            remove_space_before_apost(
                remove_extra_spaces(
                    normalize(q))))

def execute(tdata : dict, questions : list):
    for q in tdata['q']:
        print(q)

    for q in questions:
        print(q)

def main(train_file : str, questions_file: str):
    tdata = dict(
        c = list(),
        f = list(),
        q = list())
    questions = list() 

    # parse training data into dictionary "tdata"
    with open(train_file, "r") as file:
        for line in file:
            cls, q = line.split(maxsplit=1)
            c_cls, f_cls = cls.split(':')
            tdata['c'].append(c_cls)
            tdata['f'].append(f_cls)
            tdata['q'].append(pre_process(q))
        file.close()

    # parse questions into list "questions"
    with open(questions_file, "r") as file:
        for line in file:
            questions.append(
                pre_process(line))
        file.close()

    # execute qc
    execute(tdata, questions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("train_file", type=str,
        help="path of the training file")
    parser.add_argument("questions_file", type=str,
            help="path of the questions")
    args = parser.parse_args()
    main(args.train_file, args.questions_file)
