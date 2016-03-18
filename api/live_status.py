import urllib2
import json
import sys
from datetime import datetime


# pnr = 4627941857
def live_status(train, date_val):
    # base = http://api.railwayapi.com/live/train/22351/doj/20160212/apikey/yourapikey/
    # yrM=datetime.now().strftime('%Y-%m')
    # if int(date_val)<9:
        # date_val='0'+str(date_val)
    # date_val=yrM+"-"+str(date_val)
    # print date_val

    base = "http://api.railwayapi.com/live/train/"
    pnr_val = str(train)
    date = "/doj/" + str(date_val)#.replace("-","")
    apikey = "/apikey/icoyi9743"
    url = base + pnr_val + date + apikey
    # print url
    
    response = urllib2.urlopen(url)
    data = json.load(response)

    ans = "Invalid Date"
    if data["response_code"]==200:
        ans=""
        location = data["position"]
        time = data["position"].split(" ")[-2]
        value = divmod(int(time), 60)
        ans += location + " "
        in_hrs = str(value[0]) + " hrs" + " and " + str(value[1]) + " mins"
        ans += in_hrs
        print ans
        return ans
    # print ans
    return ans
    # print data["position"].split(" ")[-2]

# live_status(12295,20160214)