from PyPDF2 import PdfMerger, PdfReader
import webbrowser
import os
import json
import re
import sys


def merge_pdf(dir_path):
    dir_path = os.path.abspath(dir_path)
    pdfs = [f for f in os.listdir(dir_path) if f.endswith('.' + "pdf")]

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))

    with open('result.pdf', 'wb') as fout:
        merger.write(fout)

    webbrowser.open_new('file://' + dir_path + '/result.pdf')


def dump_pdf(path):

    # creating a pdf reader object
    reader = PdfReader(path)

    # print the number of pages in pdf file
    print(len(reader.pages))

    # print the text of the first page
    for page in reader.pages:
        print(f"{page.extract_text()}")


def parse_dump(path):
    regex = re.compile('([0-9]{2}\.[0-9]{2}\.[0-9]{4})')
    regex_expense = re.compile(
        '(\−\s*[0-9]*\.{0,1}[0-9]+,[0-9]+\s*|[0-9]*\.{0,1}[0-9]+,[0-9]+)\s+\u20AC', flags=re.UNICODE)
    expenses = {}
    with open(path, "r", encoding='utf-8') as f:
        while True:
            line = f.readline()
            match = re.search(regex, line)
            if match:
                line2 = f.readline()
                match2 = re.search(regex, line2)
                if match2:
                    if match.group(1) != match2.group(1):
                        pass
                        # print(match.group(1), match2.group(1))

                    else:
                        #  entry
                        entry = line2.replace(match2.group(1), "")
                        while True:
                            line3 = f.readline()
                            match3 = re.search(regex_expense, line3)
                            entry += line3
                            if match3:
                                entry = entry.replace(match3.group(1), "")
                                key = match.group(1)

                                entry = {
                                    "euro": match3.group(1).replace("−", "-").replace(" ", ""),
                                    "comment": entry.replace("\n", " ").replace("\u20ac", "").strip(),
                                }
                                if key in expenses:
                                    expenses[key].append(entry)
                                else:
                                    expenses[key] = [entry]
                                break

            # if line is empty
            # end of file is reached
            if not line:
                break

    for key in expenses:
        _str = f"{key}: {expenses[key]}"
        # for _entry in expenses[key]:
        #    _str += f"\n {_entry}: {expenses[key][_entry]}"
        # .encode('utf8')
        print(_str)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "merge":
            merge_pdf(sys.argv[2])
        elif sys.argv[1] == "dump":
            dump_pdf(sys.argv[2])
        elif sys.argv[1] == "parse":
            parse_dump(sys.argv[2])
