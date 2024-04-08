import http.client
import json

all_host_list = []
res_dict = {}

def get_data_from_api():
    conn = http.client.HTTPSConnection("api-habana.xdr.eu.paloaltonetworks.com")
    payload = "{}"
    headers = {
    "x-xdr-auth-id": str(9),
    'Authorization': '6hidtrHC7OwgIW7JFH1CnRTkeSdxCa67ICGmEEMCR49IVICw0v7lSSUY8arzZAvKq2g1Z3iaSPIOf5Lp4nKtUZcbW43tBWHIy8Hv1P31GpIJhGgO7LhlmNYdQgN7pr8t',
    'Content-Type': "application/json",
    'Accept': "application/json"
    }
    conn.request("POST", "/public_api/v1/endpoints/get_endpoints", payload, headers)
    
    res = conn.getresponse()
    data = res.read()
    if res.getcode() != 200:
            print("api call not successfull")
            exit(0)


    res_dict = json.loads(data)


"""
conn = http.client.HTTPSConnection("api-habana.xdr.eu.paloaltonetworks.com")

payload = "{}"

headers = {
    "x-xdr-auth-id": str(9),
    'Authorization': '6hidtrHC7OwgIW7JFH1CnRTkeSdxCa67ICGmEEMCR49IVICw0v7lSSUY8arzZAvKq2g1Z3iaSPIOf5Lp4nKtUZcbW43tBWHIy8Hv1P31GpIJhGgO7LhlmNYdQgN7pr8t',
    'Content-Type': "application/json",
    'Accept': "application/json"
}
conn.request("POST", "/public_api/v1/endpoints/get_endpoints", payload, headers)

#f res not equal 200:
 #   print("api call not successful")
 #   exit(0)
#res=conn.getresponse()
#print(res)   


res = conn.getresponse()
if res.getcode() != 200:
    print("api call not successfull")
    exit(0)
data = res.read()

res_dict = json.loads(data)

"""

#for i in range(0, len(res_dict['reply'])):
#    all_host_list.append(res_dict['reply'][i]['host_name'])



## this func will save all hosts in a list ##
def save_all_host():
    for i in range(0, len(res_dict['reply'])):
        all_host_list.append(res_dict['reply'][i]['host_name'])

def main():
    get_data_from_api()
    save_all_host()
    print(all_host_list)

if __name__ == '__main__':
    main()











