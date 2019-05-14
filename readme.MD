Big JSON Array Splitter (Python)
================================

Description
-----------

Simple python script for splitting big json array like :
```json
[{"id":"1","desc":"foo"},{"id":"2","desc":"bar"},{...
```

I had to find some specific data into a 500 MB minify json file. No (standard) editor could handle the file so i decided to create this script.

Requirement
-----------

Python version 3.x

Usage
-----

```bash
python big_json_array_splitter.py <json_file> <id_key> <filter>
```

With :
+ <json_filter> : the json file to split
+ <id_key> : the unique key of each json object (used for the filename of splitted json object)
+ \<filter> (optional) : filter to retrieve only specific data

*Be carefull with the filter. The script compare the filter with the output of json.dumps() method so there is always a space after "," and ":", etc.. Please refer to [the documentation of json.dumps()](https://docs.python.org/3.7/library/json.html#json.dumps)*

