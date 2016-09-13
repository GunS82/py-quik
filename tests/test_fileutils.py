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

from unittest import TestCase
import fileutils


class TestFileUtils(TestCase):
    def test_read_lines_reversed(self):
        result = list(fileutils.read_from_end("test-files/input.tri"))
        self.assertEqual(len(result), 3)
        self.assertTrue(result[0].endswith("TRANS_ID=3;") == True)
        self.assertTrue(result[2].endswith("TRANS_ID=1;") == True)

    def test_read_empty(self):
        result = list(fileutils.read_from_end("test-files/empty"))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], '')




