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
import fmt


class TestFmt(TestCase):
    def test_glue_item(self):
        key = "SECCODE"
        value = "LKOH"
        expected = "SECCODE=LKOH;"
        result = fmt.glue_item(key, value)
        self.assertEquals(expected, result)

    def test_dict_to_str(self):
        values = {"TRANS_ID": "1", "SECCODE": "LKOH"}
        expected = "SECCODE=LKOH;TRANS_ID=1;"
        result = fmt.dict_to_str(values)
        self.assertEquals(expected, result)

    def test_get_dict_from_params_str(self):
        line = "SECCODE=LKOH;TRANS_ID=1;"
        expected = {"SECCODE": "LKOH", "TRANS_ID": "1"}
        result = fmt.get_dict_from_params_str(line)
        self.assertEquals(expected, result)

    def test_remove_spaces_from_start(self):
        seccode = " SECCODE=LKOH;"
        account = "     ACCOUNT=1298234934;"
        trans_id = "TRANS_ID=18347"
        self.assertEquals(fmt.remove_spaces_from_start(seccode), "SECCODE=LKOH;")
        self.assertEquals(fmt.remove_spaces_from_start(account), "ACCOUNT=1298234934;")
        self.assertEquals(fmt.remove_spaces_from_start(trans_id), "TRANS_ID=18347")
