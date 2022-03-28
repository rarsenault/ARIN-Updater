import csv
import ipaddress
import requests
from requests.structures import CaseInsensitiveDict
import sys

#Get your API key from ARIN Online and populate the apikey variable
apikey = ""

#Defaults to the ARIN OTE envrionment, change to "https://reg.arin.net" to push to public ARIN IRR
target_url = "https://reg.ote.arin.net"

#read in conf/prefixes.txt, using the file's headers to index the array
#ex: each prefix in a given row is referenced by p['prefix']
with open('conf/prefixes.txt', 'r') as f:
    prefix_list = csv.DictReader(f)
    for p in prefix_list:
        
        try:
            #set default to "route" object
            irr_object = "route" 
                    
            #adjust to "route6" object if IPv6 prefix detected
            irr_prefix = ipaddress.ip_network(p['prefix'])
            if (irr_prefix.version == 6):
                irr_object = "route6"
        
            irr_origin = p['origin']
            irr_mnt = 'MNT-' + p['mnt-by'] 
            irr_techc = p['tech-c']
            irr_adminc = p['admin-c']
            irr_descr = p['descr']
        
        except:
            print("Something went wrong. Likely bad/missing data in conf/prefixes.txt. Exiting program...")
            sys.exit(1)
        
        #ARIN API requires that you post to a URL in a specific format containing the network/mask/asn and API key
        #Search ARIN IRR RESTful API for more info
        url = "{}/rest/irr/route/{}/{}/AS{}/?apikey={}".format(
          target_url,
          irr_prefix.network_address,
          irr_prefix.prefixlen,
          irr_origin,
          apikey
        )
        
        #generate an add/update payload for a given route/route6 object with given prefix/mask/origin
        payload = "{}: {}\ndescr: {}.\norigin: AS{}\nmnt-by: {}\ntech-c: {}\nadmin-c: {}\nsource: ARIN".format(
            irr_object,
            irr_prefix,
            irr_descr,
            irr_origin,
            irr_mnt,
            irr_techc,
            irr_adminc,
        )

        payload = str.encode(payload)
    
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/rpsl"
        headers["Content-Type"] = "application/rpsl"
    
        #if next operation returns HTTP status code 200, it exists and we should update
        #it any other HTTP status code, it does not exist and we should create
        object_get = requests.get(url, headers = headers)

        if object_get.status_code != 200:
            response = requests.post(url, headers = headers, data = payload)
        else:
            response = requests.put(url, headers = headers, data = payload)
      
        print("HTTP Status Code: " + str(response.status_code))
        print(response.text)
