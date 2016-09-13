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


def read_from_end(path):
    """
        This function skips '\n' symbols and read only full lines
        and returns line by line.
    """

    with open(path, 'a+') as file:
        tell = file.tell()
        if tell == 0:
            yield ''
            return
        file.seek(tell - 1)
        last_char = file.read(1)
        if last_char == '\n':
            tell -= 1
        while tell > -1:
            chars_list = []
            while True:
                file.seek(tell)
                char = file.read(1)
                if char is '\n':
                    break
                chars_list.append(char)
                tell -= 1
                if tell < 0:
                    break
            if len(chars_list) > 0:
                res = list(reversed(chars_list))
                line = ''.join(res)
                yield line
            tell -= 1


def append_line(path, line: str):
    if line.endswith('\n') is False:
        line += '\n'
    with open(path, 'a') as file:
        file.write(line)
