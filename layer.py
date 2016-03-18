from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity
import test
import passport
import nearbypubs
import nearbyhospitals
import complaint
import live_status
import pnr_status
import route


class EchoLayer(YowInterfaceLayer):
    status = "continue"
    url = ""
    caption = ""
    problem = ""
    destination = ""
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        # send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(),
                                                    'read', messageProtocolEntity.getParticipant())

            x = messageProtocolEntity.isGroupMessage()
            print x
            if x is True:
                if messageProtocolEntity.getType() == "text":
                    message = "Invalid Request"
                    input = messageProtocolEntity.getBody()
                    inputList = input.split(' ')
                    print inputList, len(inputList)
                    inputMessage = inputList[0]

                    message = "Invalid Command. Please type #info"

                    if inputMessage == "#passport":
                        inputId = messageProtocolEntity.getParticipant()[2:12]
                        message = passport.passportDetail(inputId)

                    if inputMessage == "#cab":
                        inputId = messageProtocolEntity.getParticipant()[2:12]
                        message = test.cabDetail(inputId)

                    elif inputMessage == "#info":
                        message = "#passport: to get passport status\n#cab: to get cab details \n#hospitals: to get list of nearby hospitals\n#hotels: to get list of nearby hotels \n#pnr <pnr number> to get PNR details\n#status <train no> <date in yyyymmdd> to get running train status\n#complaints <type> to register a complaint\n#routes <destination>"

                    elif inputMessage == "#hotels" and len(inputList) == 1:
                        self.status = "hotels_origin"
                        message = "Please send your location"

                    elif inputMessage == "#hospitals" and len(inputList) == 1:
                        self.status = "hospital_origin"
                        message = "Please send your location"

                    elif inputMessage == "#complaints" and len(inputList) == 2:
                        self.problem = inputList[1]
                        self.status = "complaint_image"
                        message = "Please Upload the image"

                    elif inputMessage == "#pnr" and len(inputList) == 2:
                        message = pnr_status.PNR(inputList[1])
                        print message

                    elif inputMessage == "#status" and len(inputList) == 3:
                        print inputList[1], inputList[2]
                        message = live_status.live_status(inputList[1],inputList[2])
                        #message = ""
                        print message

                    elif inputMessage == "#routes" and len(inputList) >= 2:
                        self.status = "bus_origins"
                        self.destination = " ".join(inputList[1:])
                        message = "Please send your current location"

                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        message,
                        to=messageProtocolEntity.getFrom())

                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)
                elif messageProtocolEntity.getType() == "media":
                    message = ""
                    if messageProtocolEntity.getMediaType() == "location":

                        if self.status == "hotels_origin":
                            ans = nearbypubs.waypoints([messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()])
                            print len(ans)
                            k = 1
                            for i in ans:
                                message += str(k) + ". " +i[0] + ", Rating: " + str(i[1]) + "\n"
                                k += 1
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                        elif self.status == "hospital_origin":
                            ans = nearbyhospitals.waypoints([messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()])
                            print len(ans)
                            k = 1
                            for i in ans:
                                message += str(k) + ". " +i + "\n"
                                k += 1
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                        elif self.status == "complaint_location":
                            complaint.complaintLodge(self.problem,messageProtocolEntity.getLatitude(),messageProtocolEntity.getLongitude(), self.url,self.caption)
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()
                            message = "Complaint received. Thanks"

                        elif self.status == "bus_origins":
                            origin = ""
                            origin += str(messageProtocolEntity.getLatitude()) + ","
                            origin += str(messageProtocolEntity.getLongitude())
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()
                            message = route.waypoints(origin, self.destination)
                            print message

                    elif messageProtocolEntity.getMediaType() == "image":
                        if self.status == "complaint_image":
                            self.url = messageProtocolEntity.getMediaUrl()
                            self.caption = messageProtocolEntity.getCaption()
                            self.status = "complaint_location"
                            message = "Image received. Please send your location"

                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                            message,
                            to=messageProtocolEntity.getFrom())

                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
