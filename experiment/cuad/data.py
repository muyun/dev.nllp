
import pathlib
import re
from typing import Iterator

#
import json


def read_json(addr):
    with open(addr) as reader:
        f = json.load(reader)
    return f


def get_sources(root: str) -> Iterator[pathlib.Path]:
    return pathlib.Path(root).glob("*.txt")


def parse_source(source: pathlib.Path) -> str:
    post = ""
    try:
        post = pathlib.Path(source).read_text()
    except IOError as io:
        print(io)
    return post


def write_docs(filename: str):
    #sources = get_sources()

    test_f = SRC + 'test.json'
    #test_f = SRC + 'new1.json'
    tsq_f = SRC + 'train.json'
    test_f = read_json(tsq_f)

    #
    for i_d, data_one in enumerate(test_f['data']):
        # for i_q, qa in enumerate(data_one['title']):
        source = SRC + 'full_contract_txt/' + data_one['title'] + '.txt'

        # source = SRC + \
        #    'HarpoonTherapeuticsInc_20200312_10-K_EX-10.18_12051356_EX-10.18_Development Agreement.txt'
        # grep 'DEFINITIONS'

        #f = pathlib.Path(filename).open("a")
        # store the 'DEFINITIONS' in list
        defn_data = []

        content = parse_source(source)
        if not content:
            data_one['definition'] = defn_data
            continue

        if re.search("DEFINITIONS", content):
            print("src: ", str(source).split('/')[-1])
            # f.write(str(source))
            # f.write("\n")
            #
            dict = {}
            for line in content.split("\n"):
                if re.search('("\w+") means (.*)', line):
                    sentences = line.split(".")
                    for setence in sentences:
                        searchObj = re.findall(
                            '"([\w+\s]+)" means (.*)', setence)
                        if searchObj:
                            print("searchObj: ", searchObj)
                            #matchObj = re.search
                            print("key words: ", searchObj[0][0])
                            print("Definition: ", searchObj[0][1])
                            #print("line: ", line)
                            dict[searchObj[0][0]] = searchObj[0][1]
                            #f.write(str(line) + "\n")

            defn_data.append(dict)
            # f.write("\n")
            # f.close()

        else:
            pass

        data_one['definition'] = defn_data

    with open(filename, 'w') as f:
        json.dump(test_f, f)

    return


SRC = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/cuad/'

if __name__ == '__main__':
    #sources = get_sources(src)
    filename = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/result/new_train.json'
    write_docs(filename)

    """
    cuadv1_f = 'cuadv1.json'
    test_f = 'test.json'
    tsq_f = 'train.json'

    test_f = read_json(test_f)
    tsq_f = read_json(tsq_f)
    """
