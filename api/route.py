import urllib2
import json
import sys


def getDestinationLatLong(destination):
    destination = destination.replace(' ', '+')
    base = "https://maps.googleapis.com/maps/api/geocode/json?"
    location = "address=" + destination + "+bus+station"
    components = "&components=country:IN|locality:Bengaluru"
    key = "&key=" + "AIzaSyCAGcovWLp6hyzLzB9JAIbsaKV-6sjC1HQ"
    url = base + location + components + key
    # print url
    response = urllib2.urlopen(url)
    data = json.load(response)
    destination = str(data["results"][0]["geometry"]["location"]["lat"])
    destination += ',' + str(data["results"][0]["geometry"]["location"]["lng"])
    # print destination
    return destination


def waypoints(origin, dest):
    destination = getDestinationLatLong(dest)


    origin = origin.replace(' ', '+')
    destination = destination.replace(' ', '+')
    base = "https://maps.googleapis.com/maps/api/directions/json?"
    location = "origin=" + origin + "&destination=" + destination + "&mode=transit"
    key = "&key=" + "AIzaSyCAGcovWLp6hyzLzB9JAIbsaKV-6sjC1HQ"
    url = base + location + key
    # print url
    response = urllib2.urlopen(url)
    data = json.load(response)
    result = ""
    result = "Time: " + data["routes"][0]["legs"][0]["duration"]["text"]
    result += "\n" + "Distance " + data["routes"][0]["legs"][0]["distance"]["text"]
    # print data["routes"][0]["legs"][0]["distance"]["text"]
    # print data["routes"][0]["legs"][0]["duration"]["text"]
    result += "\n" + "Route:"
    limit = len(data["routes"][0]["legs"][0]["steps"])
    for i in range(0, limit):
        if data["routes"][0]["legs"][0]["steps"][i]["travel_mode"] == "TRANSIT":
            result += "\n" + "Take Bus from " + \
                      data["routes"][0]["legs"][0]["steps"][i]["transit_details"]["departure_stop"]["name"]
            result += "\n" + "to " + data["routes"][0]["legs"][0]["steps"][i]["transit_details"]["arrival_stop"]["name"]
            # print "Take Bus from "+data["routes"][0]["legs"][0]["steps"][i]["transit_details"]["departure_stop"]["name"]
            # print "to "+data["routes"][0]["legs"][0]["steps"][i]["transit_details"]["arrival_stop"]["name"]
        else:
            result += "\n" + data["routes"][0]["legs"][0]["steps"][i]["html_instructions"]
            # print data["routes"][0]["legs"][0]["steps"][i]["html_instructions"]
    return result  # destLatLong=getDestinationLatLong("forum")
# print destLatLong

# waypoints("12.959905, 77.647617","12.8446784,77.6610528")
# print waypoints(latlong,getDestinationLatLong(dest))

# , [12.9899747663903,77.572098665973])
# whitefield:   
# silk board: 12.917630, 77.623379
# iiitb: 12.8446784,77.6610528
# majestic: 12.9773452,77.566781
# https://maps.googleapis.com/maps/api/geocode/json?address=forum%20bus%20station&components=country:IN|locality:Bengaluru&key=AIzaSyCAGcovWLp6hyzLzB9JAIbsaKV-6sjC1HQ
