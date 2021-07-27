
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


def search_special_patterns(sentence: str):
    """ search some pattern in sentence
    """
    # the other cases
    dict = {}
    pattern_6 = re.compile(
        '"([\w+\s]+)" or "([\w+\s]+)" means? (.*)', flags=re.IGNORECASE
    )

    pattern_7 = re.compile(
        '"([\w+\s]+)" or "([\w+\s]+)" shall mean (.*)', flags=re.IGNORECASE)

    searchObj = re.findall(
        pattern_6, sentence)

    if not searchObj:
        searchObj = re.findall(pattern_7, sentence)

        if not searchObj:
            return dict

    print("searchObj: ", searchObj)
    # matchObj = re.search
    print("the 1st key word: ", searchObj[0][0])
    print("the 2nd key word: ", searchObj[0][1])
    print("Definition: ", searchObj[0][2])
    # print("line: ", line)
    dict[searchObj[0][0].strip()] = searchObj[0][2].strip()
    dict[searchObj[0][1].strip()] = searchObj[0][2].strip()

    return dict


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
    pattern_5 = re.compile(
        '([\w+\s]+) shall mean (.*)', flags=re.IGNORECASE)
    pattern_4 = re.compile(
        '([\w+\s]+) means? (.*)',  flags=re.IGNORECASE)

    # the other special patterns

    # cnt_mean = 0
    for line in content.split("\n"):
        sentences = line.split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            # cnt_mean += 1
            if len(sentence) < 5:
                continue

            print("the sentence:", sentence)
            # the other special cases
            dict1 = search_special_patterns(sentence)
            if len(dict1):
                dict.update(dict1)
                continue

            # format one
            searchObj = re.findall(
                pattern_1, sentence)
            if not searchObj:
                # format two
                searchObj = re.findall(
                    pattern_2, sentence)

                if not searchObj:
                    # format four
                    searchObj = re.findall(
                        pattern_4, sentence)

                    if not searchObj:
                        # format five
                        searchObj = re.findall(
                            pattern_5, sentence)

                        # BUGS
                        if searchObj and (len(searchObj[0][0].strip()) > 20 or len(searchObj[0][0].strip()) < 3 or
                                          len(searchObj[0][1].strip()) < 10):
                            continue

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


def search_special_case(content: str):
    """
    """
    dict = {}
    pattern_3 = re.compile('([\w+\s]+): (.*)',  flags=re.IGNORECASE)
    pattern_7 = re.compile('"([\w+\s]+)" - (.*)',  flags=re.IGNORECASE)
    #searchObj = ""
    for line in content.split("\n"):
        sentences = line.split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 5:
                continue
            print("sentence: ", sentence)
            # format three
            searchObj = re.findall(
                pattern_3, sentence)
            # BUGS
            if searchObj and (len(searchObj[0][0].strip()) > 20 or len(searchObj[0][0].strip()) < 3 or
                              len(searchObj[0][1].strip()) < 10):
                continue

            if not searchObj:
                # format seven
                searchObj = re.findall(
                    pattern_7, sentence)

                if not searchObj:
                    continue

            print("searchObj: ", searchObj)
            # matchObj = re.search
            print("key words: ", searchObj[0][0])
            print("Definition: ", searchObj[0][1])
            # print("line: ", line)
            dict[searchObj[0][0].strip()] = searchObj[0][1].strip()

    return dict


def write_docs(srcname: str, filename: str):
    """ write the fitted content from srcname into filename
    """
    cnt_definition = 0
    cnt_mean = 0
    # rule and the related patterns
    # RULE 1:grep 'DEFINITIONS'
    rule_1 = re.compile("DEFINITIONS|Definitions", flags=re.IGNORECASE)
    # pattern = re.compile('mean(s*)', flags=re.IGNORECASE)
    # pattern_1 = re.compile('"([\w+\s]+)" means(,*) (.*)')
    # pattern_2 = re.compile('"([\w+\s]+)" shall mean (.*)')

    defn_data = []
    if srcname:
        # sources = get_sources()
        # source = SRC + 'full_contract_txt/' + data_one['title'] + '.txt'
        print("src: ", srcname)
        content = parse_source(srcname)
        defn_data.append(search(content))
        # defn_data.append(search_special_case(content))
    else:
        test_f = SRC + 'test.json'
        train_f = SRC + 'train.json'

        json_f = read_json(test_f)

        for i_d, data_one in enumerate(json_f['data']):
            print("src: ", data_one['title'])

            source = SRC + 'full_contract_txt/' + \
                data_one['title'] + '.txt'
            content = parse_source(source)
            if not content:
                data_one['paragraphs'][0]['context'] = content
            else:
                content = data_one['paragraphs'][0]['context']

            # for special cases in some file
            # pattern_3 = re.compile('([\w+\s]+): (.*)')
            if i_d in [9]:  # bugs
                data_one['definition'] = search_special_case(content)

            else:
                #content = data_one['paragraphs'][0]['context']
                #
                data_one['definition'] = search(content)

        # TODO - the cases

        # write into filename
        with open(filename, 'w') as f:
            json.dump(json_f, f)

    # print("num of files including 'DEFINITION:", cnt_definition)
    # print("num of lines including 'mean:", cnt_mean)

    return


SRC = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/cuad/'

if __name__ == '__main__':
    # sources = get_sources(src)
    srcname = ''
    #srcname = SRC + 'STARTECGLOBALCOMMUNICATIONSCORP_11_16_1998-EX-10.30-CONSTRUCTION AND MAINTENANCE AGREEMENT.txt'
    output = '/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/result/new_test.json'
    write_docs(srcname, output)

    """
    cuadv1_f = 'cuadv1.json'
    test_f = 'test.json'
    tsq_f = 'train.json'

    test_f = read_json(test_f)
    tsq_f = read_json(tsq_f)
    """
