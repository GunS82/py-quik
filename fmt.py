"""
Copyright 2012, 2016 Denis Lebedev
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


def glue_item(key, value):
    return str.format("{}={};", key.upper(), value)


def dict_to_str(obj: dict):
    temp = [glue_item(key, value) for key, value in obj.items()]
    temp = sorted(temp)
    return ''.join(temp)


def remove_spaces_from_start(line: str):
    if line.startswith(' ') is False:
        return line
    while True:
        if line.startswith(' '):
            line = line[1:]
        else:
            return line


def get_dict_from_params_str(params: str):
    params = params.split(";")
    result = {}
    for i in params:
        if i != '':
            s = i.split("=")
            result[remove_spaces_from_start(s[0])] = s[1]
    return result
