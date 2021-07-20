
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


def write_docs(srcname: str, filename: str):
    # sources = get_sources()

    test_f = SRC + 'test.json'
    # test_f = SRC + 'new1.json'
    tsq_f = SRC + 'train.json'
    test_f = read_json(tsq_f)

    cnt_definition = 0
    cnt_mean = 0
    # rule and the related patterns
    # RULE 1:grep 'DEFINITIONS'
    rule_1 = re.compile("DEFINITIONS", flags=re.IGNORECASE)
    pattern_1 = re.compile('"([\w+\s]+)" means(,*) (.*)')
    pattern_2 = re.compile('"([\w+\s]+)" shall mean (.*)')

    for i_d, data_one in enumerate(test_f['data']):
        if not srcname:
            content = data_one['paragraphs'][0]['context']
        else:  # for DEBUG
            # source = SRC + 'full_contract_txt/' + data_one['title'] + '.txt'
            content = parse_source(srcname)

        # store the 'DEFINITIONS' info in list
        defn_data = []
        """
        if not content:
            data_one['definition'] = defn_data
            continue
        """

        if re.search(rule_1, content):
            if not srcname:
                print("src: ", str(data_one['title']).split('/')[-1])
            else:
                print("src: ", srcname)
            cnt_definition += 1
            # f.write(str(source))
            # f.write("\n")
            #
            dict = {}
            #cnt_mean = 0
            for line in content.split("\n"):
                if re.search('means|mean', line):
                    # the keyword 'meaning' does mean anything
                    sentences = line.split(".")
                    for sentence in sentences:
                        sentence = sentence.strip()
                        cnt_mean += 1
                        if len(sentence) < 5:
                            continue

                        print("the sentence:", sentence)
                        # format one
                        searchObj = re.findall(
                            pattern_1, sentence)
                        if not searchObj:
                            # format two
                            searchOjb = re.findall(
                                pattern_2, sentence)
                        else:
                            # any others
                            # continue
                            print("searchObj: ", searchObj)
                            # matchObj = re.search
                            print("key words: ", searchObj[0][0])
                            print("Definition: ", searchObj[0][2])
                            # print("line: ", line)
                            dict[searchObj[0][0]] = searchObj[0][2]
                            # f.write(str(line) + "\n")

            defn_data.append(dict)
            # f.write("\n")
            # f.close()

        else:
            pass

        data_one['definition'] = defn_data

    print("num of files including 'DEFINITION:", cnt_definition)
    print("num of files including 'mean:", cnt_mean)
    with open(filename, 'w') as f:
        json.dump(test_f, f)

    return


SRC = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/cuad/'

if __name__ == '__main__':
    # sources = get_sources(src)
    srcname = ''
    #srcname = SRC + 'BNCMORTGAGEINC_05_17_1999-EX-10.4-LICENSING AND WEB SITE HOSTING AGREEMENT.txt'
    output = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/result/new_train.json'
    write_docs(srcname, output)

    """
    cuadv1_f = 'cuadv1.json'
    test_f = 'test.json'
    tsq_f = 'train.json'

    test_f = read_json(test_f)
    tsq_f = read_json(tsq_f)
    """
