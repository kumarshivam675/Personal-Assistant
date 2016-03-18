import urllib2
import json
import sys


def waypoints(src):
    base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    location = "location=" + str(src[0]) + "," + str(src[1]) + "&radius=1000" + "&types=pub"
    key = "&key=AIzaSyDwaKYumwoHsN-wgn249eep63oHdtefl9w"
    url = base + location + key
    response = urllib2.urlopen(url)
    data = json.load(response)
    ans = []
    print url
    for i in range(2, 20):
        if (data["results"][i]["types"][0] == "lodging"):
            print data["results"][i]["name"]
            #print "ratings :" + str(data["results"][i]["rating"])

            ans.append([data["results"][i]["name"],""])
    return ans
        # print data
        # distance = data["routes"][0]["legs"][0]["distance"]["text"]
        # duration = data["routes"][0]["legs"][0]["duration"]["text"]
        # bus = data["routes"][0]["legs"][0]["steps"][0]["steps"][0]["transit_details"]["line"]["sho
        # print "distance : "+ distance
        # print "duration : "+ duration
        # tmp = data["routes"][0]["overview_polyline"]["points"]

        # print decodeGMapPolylineEncoding(tmp)


#waypoints([sys.argv[1], sys.argv[2]])
# waypoints([12.9817447954723,77.574481312945], [12.9899747663903,77.572098665973])
# whitefield: 12.971289, 77.750098
# silk board: 12.917630, 77.623379
# iiitb: 12.8446784,77.6610528
# majestic: 12.9773452,77.566781
# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=12.8446784,77.6610528&radius=1000&types=pub&key=AIzaSyDwaKYumwoHsN-wgn249eep63oHdtefl9w
