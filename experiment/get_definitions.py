
import pathlib
import re
from typing import Iterator

def get_sources(root: str) -> Iterator[pathlib.Path]:
    return pathlib.Path(root).glob("*.txt")

def parse_source(source: pathlib.Path) -> str:
    post = pathlib.Path(source).read_text()
    return post

def write_docs(sources: pathlib.Path, filename: str):
    #sources = get_sources()
    for source in sources:
        #grep 'DEFINITIONS'
        content = parse_source(source)
        f = pathlib.Path(filename).open("a")
        if re.search("DEFINITIONS", content):
            print("src: ", source)
            f.write(str(source))
            f.write("\n")
            #
            for line in content.split("\n"):
                if re.search(r'("\w+"\s+)means', line):
                    #print("line: ", line)
                    f.write(str(line) + "\n")
            f.write("\n")
        else:
            pass
        f.close()
    return


if __name__ == '__main__':
    src = "/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/full_contract_txt"
    sources = get_sources(src)
    filename = "/Users/zhaowenlong/workspace/proj/dev.goal2021/experiment/data/definitions.md"
    write_docs(sources, filename)