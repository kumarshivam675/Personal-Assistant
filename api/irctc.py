
import urllib2
import hmac
from hashlib import sha1
import json


def MyPnrTestFn():
 #Setting Credentials
 apiCreds = {}
 apiCreds["Key"] = "Your public key"
 apiCreds["Secret"] = "Your api secret/private key"

 pnr = "1234567890" #Test Pnr
 requestUrlTemplate =
"http://railpnrapi.com/api/check_pnr/pnr/"+pnr+"/format/json/pbapikey/" +
apiCreds["Key"] + "/pbapisign/"

 #Get all the request parameter
 paramset = {}
 paramset["pnr"] = pnr
 paramset["format"] = "json"
 paramset["pbapikey"] = apiCreds["Key"]

 #Sort the keys and concat their values
 keylist = sorted(paramset.keys())
 inputString = ''
 for item in keylist:
 item1 = paramset[item]
 inputString = inputString + str(paramset[item])

 #Compute hash
 signature = GenerateHmac(inputString, apiCreds["Secret"])


 requestUrl = requestUrlTemplate + str(signature)
 response = urllib2.urlopen(requestUrl).read()

 #Parse Json response
 jsonOut = json.loads(response)


 #display response
 print "Response Code:" , jsonOut["response_code"]
 print "PNR: " , jsonOut["pnr"]
 print "Train No.: ", jsonOut["train_num"]
 print "Train Name: ", jsonOut["train_name"]
 print "DOJ: ", jsonOut["doj"]
 print "From Station (Code/Name): " + jsonOut["from_station"]["code"] + "/"
+ jsonOut["from_station"]["name"]
 print "To Station (Code/Name): " + jsonOut["to_station"]["code"] + "/" +
jsonOut["to_station"]["name"]
 print "Reservation Upto (Code/Name): "+ jsonOut["reservation_upto"]["code"]
+ "/" + jsonOut["reservation_upto"]["name"]
 print "Boarding Point (Code/Name): " + jsonOut["boarding_point"]["code"] +
"/" + jsonOut["boarding_point"]["name"]

 print "Class: ", jsonOut["class"]
 print "No. of Passengers: ", jsonOut["no_of_passengers"]
 print "Chart Status: ", jsonOut["chart_prepared"]
 print
 print "Passengers: "
 print "********************************"
 for passenger in jsonOut["passengers"]:
 print "Passenger #:" + str(passenger["sr"]) + ", Booking Status:" +
passenger["booking_status"] + ", Current Status:" +
passenger["current_status"]

 print
 print "********************************"



def GenerateHmac(input, bytekey):
 myHmacSha1 = hmac.new(bytekey, input, sha1)
 return myHmacSha1.hexdigest()

MyPnrTestFn()
