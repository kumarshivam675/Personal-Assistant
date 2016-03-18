import urllib2
import json
import sys

#pnr = 4627941857
def PNR(pnr):
    print pnr
    ans = ""
    new_ans = ""
    base = "http://api.railwayapi.com/pnr_status/pnr/"
    pnr_val = str(pnr)
    apikey = "/apikey/icoyi9743"
    url = base+pnr_val+apikey
    response = urllib2.urlopen(url)
    data = json.load(response)
    #print url
    ans += "Date of journey : " + data["doj"] + "\n"
    ans += "Total passengers : " + str(data["total_passengers"]) + "\n"
    passengers = data["total_passengers"]
    train_name = data["train_name"] + "\n"
    boarding_point = "Boarding point : " + data["boarding_point"]["name"] + "\n"
    destination = "Destination : " + data["to_station"]["name"] + "\n"
    #print destination
    #print boarding_point
    for i in range(0, passengers):
        new_ans += str(data["passengers"][i]["current_status"]) + " " + str(data["passengers"][i]["booking_status"]) + "\n"
    #print boarding_point + destination + ans + "Booking Status:" + "\n" + new_ans
    return boarding_point + destination + ans + "Booking Status:" + "\n" + new_ans


#PNR(sys.argv[1])
