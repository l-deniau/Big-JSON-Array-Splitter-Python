#!/usr/bin/env python3

import sys
import os
import json


def print_usage():
    print()
    print("Error: wrong number of arguments")
    print()
    print("Usage: python big_json_array_splitter.py <json_file> <id_key> "
          "<filter>")
    print()
    print("With:")
    print()
    print("    <json_filter>: the json file to split")
    print()
    print("    <id_key>: the unique key of each json object (used for the "
          "filename of splitted json object)")
    print()
    print("    <filter> (optional): filter to retrieve only specific data")
    print()


def main(argv):
    if len(argv) < 2 or len(argv) > 3:
        print_usage()
    else:
        input_file = argv[0]
        id_key = argv[1]
        if len(argv) == 3:
            input_filter = argv[2]
        else:
            input_filter = None
        directory_output = os.path.splitext(input_file)[0]
        json_file = open(input_file, "r", encoding="UTF-8")
        json_raw = json_file.read()
        json_decode = json.JSONDecoder()
        json_data = json_decode.decode(json_raw)
        try:
            os.mkdir(directory_output)
        except FileExistsError:
            pass
        for chunk in json_data:
            try:
                json_chunk_raw = json.dumps(chunk, ensure_ascii=False)
                if input_filter is None or input_filter in json_chunk_raw:
                    chunk_key = chunk.get(id_key)
                    file_name = chunk_key + ".json"
                    file_chunk = open(directory_output + "/" +
                                      file_name, "w", encoding="UTF-8")
                    file_chunk.write(json_chunk_raw)
            except:
                print(chunk)
                raise


if __name__ == "__main__":
    main(sys.argv[1:])
