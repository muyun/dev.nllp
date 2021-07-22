
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


def search(content: str):
    """ search the following patterns in content
    """
    # print("src: ", srcname)

    dict = {}
    # so BAD
    pattern_1 = re.compile(
        '"([\w+\s]+)" means? (.*)',  flags=re.IGNORECASE)
    pattern_2 = re.compile(
        '"([\w+\s]+)" shall mean (.*)', flags=re.IGNORECASE)
    pattern_4 = re.compile(
        '([\w+\s]+) means? (.*)',  flags=re.IGNORECASE)
    pattern_3 = re.compile('([\w+\s]+): (.*)')

    # cnt_mean = 0
    for line in content.split("\n"):
        sentences = line.split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            # cnt_mean += 1
            if len(sentence) < 5:
                continue

            print("the sentence:", sentence)
            # format one
            searchObj = re.findall(
                pattern_1, sentence)
            if not searchObj:
                # format two
                searchObj = re.findall(
                    pattern_2, sentence)

                if not searchObj:
                    # format three
                    searchObj = re.findall(
                        pattern_3, sentence)
                    # BUGS
                    if searchObj and (len(searchObj[0][0].strip()) > 20 or
                                      len(searchObj[0][1].strip()) < 10):
                        continue

                    if not searchObj:
                        # format four
                        searchObj = re.findall(
                            pattern_4, sentence)

                        if not searchObj:
                            continue

            print("searchObj: ", searchObj)
            # matchObj = re.search
            print("key words: ", searchObj[0][0])
            print("Definition: ", searchObj[0][1])
            # print("line: ", line)
            dict[searchObj[0][0].strip()] = searchObj[0][1].strip()
            # f.write(str(line) + "\n")

    return dict


def write_docs(srcname: str, filename: str):
    """ write the fitted content from srcname into filename
    """
    cnt_definition = 0
    cnt_mean = 0
    # rule and the related patterns
    # RULE 1:grep 'DEFINITIONS'
    rule_1 = re.compile("DEFINITIONS|Definitions", flags=re.IGNORECASE)
    #pattern = re.compile('mean(s*)', flags=re.IGNORECASE)
    # pattern_1 = re.compile('"([\w+\s]+)" means(,*) (.*)')
    # pattern_2 = re.compile('"([\w+\s]+)" shall mean (.*)')

    defn_data = []
    if srcname:
        # sources = get_sources()
        # source = SRC + 'full_contract_txt/' + data_one['title'] + '.txt'
        print("src: ", srcname)
        content = parse_source(srcname)
        defn_data.append(search(content))
    else:
        test_f = SRC + 'test.json'
        train_f = SRC + 'train.json'

        json_f = read_json(test_f)

        for i_d, data_one in enumerate(json_f['data']):
            print("src: ", data_one['title'])
            content = data_one['paragraphs'][0]['context']

            # store the 'DEFINITIONS' info in list
            #defn_data = []
            data_one['definition'] = search(content)

        # write into filename
        with open(filename, 'w') as f:
            json.dump(json_f, f)

    #print("num of files including 'DEFINITION:", cnt_definition)
    #print("num of lines including 'mean:", cnt_mean)

    return


SRC = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/cuad/'

if __name__ == '__main__':
    # sources = get_sources(src)
    srcname = ''
    #srcname = SRC + 'WESTERN COPPER - NON-COMPETITION AGREEMENT.txt'
    output = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/result/new_test.json'
    write_docs(srcname, output)

    """
    cuadv1_f = 'cuadv1.json'
    test_f = 'test.json'
    tsq_f = 'train.json'

    test_f = read_json(test_f)
    tsq_f = read_json(tsq_f)
    """
