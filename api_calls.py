import requests
import pandas as pd
import ast
import csv
import json

output = []


def test_standard_authentication(api_key_id, api_key):
    headers = {
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key
    }
    parameters = {}
    res = requests.post(url="https://api-habana.xdr.eu.paloaltonetworks.com/public_api/v1/endpoints/get_endpoints",
						headers=headers,
						json=parameters)

    return res


res=test_standard_authentication("9", "6hidtrHC7OwgIW7JFH1CnRTkeSdxCa67ICGmEEMCR49IVICw0v7lSSUY8arzZAvKq2g1Z3iaSPIOf5Lp4nKtUZcbW43tBWHIy8Hv1P31GpIJhGgO7LhlmNYdQgN7pr8t")


data = res.json()

print(list(data.values('host_name')))

