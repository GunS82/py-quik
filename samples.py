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

import pyquik as pq

order = pq.Order(
    action='NEW_ORDER',
    account="NL0011100043",
    seccode="SBER",
    classcode="QJSIM",
    quantity=1,
    type="M",
    operation='S',
    price=0,
    clientcode="client_code")

quik = pq.Quik(input_file="shared-files/input.tri",
               output_file="shared-files/output.tro")


order_id = quik.register(order)

input('Press INTER to get order info.')

order_info = quik.get_order_info(order_id)

print(order_info)
