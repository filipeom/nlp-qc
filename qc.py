import argparse, re, nltk

def pre_process(q : str, skip=False):

    def normalize(q : str):
        return re.sub(r"[^a-zA-Z0-9\s]", r"", q.lower())

    def remove_endline_char(q : str):
        return q.rstrip()

    proc = remove_endline_char(normalize(q))

    return proc if not skip else q

#def distance(s1 : list, s2 : list):
#    set1, set2 = set(s1), set(s2)
#    return 1 - (2 * len(set1.intersection(set2))) / (len(set1) + len(set2))

def distance(s1 : list, s2 : list):
    return nltk.jaccard_distance(set(s1), set(s2))

def execute(tdata : dict, questions : list, is_fine=False):
    # classifications list
    lbls = list()

    for q in questions:
        # calculate distances from training data
        dists = \
            list(map(lambda d : \
                distance(d['q'].split(), q.split()),
                tdata))
        # get the min distance classification
        d = tdata[dists.index(min(dists))]
        lbls.append( \
            "{}:{}".format(d['c'], d['f']) if is_fine else
            d['c'])

    return lbls 

def main(train_file : str, questions_file: str, ty : bool):
    tdata = list()
    questions = list() 

    # parse training data into dictionary "tdata"
    with open(train_file, "r") as file:
        for line in file:
            lbl, qst = line.split(maxsplit=1)
            coa, fin = lbl.split(':')
            tdata.append(dict(
                c = coa,
                f = fin,
                q = pre_process(qst)))
        file.close()

    # parse questions into list "questions"
    with open(questions_file, "r") as file:
        for line in file:
            questions.append(
                pre_process(line))
        file.close()

    # execute qc
    lbls = execute(tdata, questions, ty)

    # print classifications
    list(map(lambda c : print(c), lbls))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-coarse", dest="ty", 
        action="store_false")
    parser.add_argument("-fine", dest="ty",
        action="store_true")
    parser.add_argument("train_file", type=str,
        help="path of the training file")
    parser.add_argument("questions_file", type=str,
        help="path of the questions")
    args = parser.parse_args()
    main(args.train_file, args.questions_file, args.ty)
