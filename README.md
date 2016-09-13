# py-quik

```python

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

```