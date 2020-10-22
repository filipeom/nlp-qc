import argparse

def execute(dev : list, predictions : list):
    tp = 0
    total = len(dev)

    for i in range(total):
        if dev[i]['c'] == predictions[i]:
            tp += 1
    print(tp/total * 100)

def main(dev_file : str, predicted_file : str):
    dev = list()
    predictions = list()

    with open(dev_file, "r") as file:
        for line in file:
            coa, fin = line.rstrip().split(':')
            dev.append(dict( \
                c = coa,
                f = fin))
        file.close()

    with open(predicted_file, "r") as file:
        for line in file:
            lbl = line.rstrip().split(':')
            predictions.append(dict( \
                c = lbl[0],
                f = lbl[1]) if len(lbl) > 1 else lbl[0])
        file.close()

    execute(dev, predictions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dev_file", type=str,
        help="path of the dev labels")
    parser.add_argument("predicted_file", type=str,
        help="path of the predicted labels")
    args = parser.parse_args()
    main(args.dev_file, args.predicted_file)
