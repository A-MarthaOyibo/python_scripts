

#!/usr/bin/env python3

#author : Afure Martha, Oyibo maoy4508@colorado.edu
#purpose: IP VALIDITY CHECKER
#date   : 2019.3.03
#python version: 3.5.2

#Note: import as validateIP.verifyIP(device_login_file)


import json,sys
#file = "sshinfo.json"

def verifyOctet(a):
    b = a.split(".")
    if len(b) == 4:
        # print(a)
        for i in b:
            try:
                if int(i) < 256 and int(i) > -1:
                   # print("valid octet: " + a)
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

def verifyIp(x):
    #with open(x,"r")  as f:
        #jsondata = json.loads(f.read())
        #print(json.dumps(jsondata, indent=2))
        #for devices in jsondata:
            #print(jsondata[devices]["ip"])
            #a= jsondata[devices]["ip"]
            #verifyOctet(a)
    a=verifyOctet(x)
    return(a)







#verifyIp(file)
