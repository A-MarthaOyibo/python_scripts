
#!/usr/bin/env python3

'''
author : Afure Martha, Oyibo
purpose: IP VALIDITY CHECKER
date   : 2019.3.03
python version: 3.5.2

To import module:
     from ip_validity_checker import verifyIpOctet
'''
#!/usr/bin/env python3

import sys


def verifyIpOctet(ip_addr):
    b = ip_addr.split(".")
    if len(b) == 4:
        for i in b:
            try:
                if int(i) < 256 and int(i) > -1:
                    pass
                else:
                    return("invalid ip octet: " + a)
                    sys.exit()
            except:
                return("invalid ip: " + a)
                sys.exit()
        return ("Success: IP is valid")
    else:
        return("Invalid no of octet:" + a)
        sys.exit()

# To add ip_extractor from json/yaml device file soon

'''

#test:
a = verifyIpOctet("192.168.1.1")
print(a)

'''
