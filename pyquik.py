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

import fileutils
import fmt


class Order(object):
    def __init__(self, **kwargs):
        super(Order, self).__init__()
        self.__dict__ = kwargs
        self.trans_id = 0

    def __str__(self):
        return self.get_order_string()

    def get_order_string(self):
        return fmt.dict_to_str(self.__dict__)


class Quik(object):
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.trans_id = self.get_trans_id_of_last_order()

    def get_trans_id_of_last_order(self):
        last_line = next(fileutils.read_from_end(self.input_file))
        if last_line == '':
            return 0
        last_order = fmt.get_dict_from_params_str(last_line)
        return int(last_order["TRANS_ID"])

    def register(self, order):
        self.trans_id += 1
        order.trans_id = self.trans_id
        fileutils.append_line(self.input_file, order.get_order_string())
        return order.trans_id

    def get_order_info(self, order_id):
        if int(order_id) <= 0:
            raise Exception("order_id can't be equal or less than 0.")
        order_info_line = next(fileutils.read_from_end(self.output_file))
        order_dict = fmt.get_dict_from_params_str(order_info_line)
        if len(order_dict) == 0:
            return
        if int(order_dict["TRANS_ID"]) < int(order_id):
            return
        for order_line in fileutils.read_from_end(self.output_file):
            order_dict = fmt.get_dict_from_params_str(order_line)
            if order_dict["TRANS_ID"] == str(order_id):
                return order_dict
