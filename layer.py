from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity

from api import nearbypubs
from api import nearbyhospitals
from api import complaint
from api import search_complaint
from api import tender
from api import uploadComment
from api import pnr_status
from api import live_status


class EchoLayer(YowInterfaceLayer):
    status = "continue"
    url = ""
    caption = ""
    problem = ""
    destination = ""
    tender_no = ""

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

                    message = ""

                    if inputMessage == "#info":
                        message = "#complaints <complaint-id>: to get complaint with the complaint ID\n#projects: to get details about the projects in the neighbourhood \n#feedback <Serial No.> : to get feedback of that particular tender number\n#hospitals: to get list of nearby hospitals \n#complaintsNearby: to get complaints of the neighbourhood\n#hotels: to get list of nearby hotels \n#pnr <pnr number> to get PNR details\n#status <train no> <date in yyyymmdd> to get running train status\n#lodgeComplaint <type> to register a complaint"

                    elif inputMessage == "#hotels" and len(inputList) == 1:
                        self.status = "hotels_origin"
                        message = "Please send your location"

                    elif inputMessage == "#pnr" and len(inputList) == 2:
                        message = pnr_status.PNR(inputList[1])
                        print message

                    elif inputMessage == "#trainStatus" and len(inputList) == 3:
                        print inputList[1], inputList[2]
                        message = live_status.live_status(inputList[1],inputList[2])
                        #message = ""
                        print message

                    elif inputMessage == "#hospitals" and len(inputList) == 1:
                        self.status = "hospital_origin"
                        message = "Please send your location"

                    elif inputMessage == "#complaints" and len(inputList) == 2:
                        inputId = inputList[1]
                        message += search_complaint.search(inputId)

                    elif inputMessage == "#lodgeComplaint" and len(inputList) == 2:
                        self.status = "lodgeComplaint_image"
                        message = "Please Upload the image"

                    elif inputMessage == "#complaintsNearby" and len(inputList) == 1:
                        self.status = "complaintNearby_location"
                        message = "Please send your location"

                    elif inputMessage == "#projects" and len(inputList) == 1:
                        self.status = "project_origin"
                        message = "Please send your location"

                    elif inputMessage == "#feedback" and len(inputList) == 2:
                        self.tender_no = inputList[1]
                        self.status = "feedback_image"
                        message = "Please upload the image"

                    else:
                        message = ""

                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        message,
                        to=messageProtocolEntity.getFrom())

                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)
                elif messageProtocolEntity.getType() == "media":
                    message = ""
                    if messageProtocolEntity.getMediaType() == "location":

                        if self.status == "hotels_origin":
                            ans = nearbypubs.waypoints(
                                [messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()])
                            print len(ans)
                            k = 1
                            for i in ans:
                                message += str(k) + ". " + i[0].encode('utf-8') + "\n"
                                k += 1
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                        elif self.status == "hospital_origin":
                            ans = nearbyhospitals.waypoints(
                                [messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()])
                            print len(ans)
                            k = 1
                            for i in ans:
                                message += str(k) + ". " + i.encode('utf-8') + "\n"
                                k += 1
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()

                        elif self.status == "project_origin":
                            lat = messageProtocolEntity.getLatitude()
                            lng = messageProtocolEntity.getLongitude()
                            temp = tender.getWard([lat, lng])
                            message = tender.getTenders(temp)
                            self.status = "continue"

                        elif self.status == "feedback_location":
                            lat = messageProtocolEntity.getLatitude()
                            lng = messageProtocolEntity.getLongitude()
                            # uploadComment.uploadComment(messageProtocolEntity.getFrom()[2:12], self.caption,
                            #                             self.tender_no, self.url)
                            self.status = "continue"
                            message = "Complaint received. Thank You"

                        elif self.status == "complaintNearby_location":
                            print "enter"
                            lat = messageProtocolEntity.getLatitude()
                            lng = messageProtocolEntity.getLongitude()
                            temp = tender.getWard([lat, lng])
                            message = tender.getComplains(temp)
                            print "done"
                            self.status = "continue"

                        elif self.status == "lodgeComplaint_location":
                            #complaint.complaintLodge(self.problem,messageProtocolEntity.getLatitude(),messageProtocolEntity.getLongitude(), self.url,self.caption)
                            self.status = "continue"
                            print messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude()
                            message = "Complaint received. Thanks"

                    elif messageProtocolEntity.getMediaType() == "image":
                        if self.status == "complaint_image":
                            self.url = messageProtocolEntity.getMediaUrl()
                            self.caption = messageProtocolEntity.getCaption()
                            self.status = "complaint_location"
                            message = "Image received. Please send your location"

                        elif self.status == "feedback_image":
                            self.url = messageProtocolEntity.getMediaUrl()
                            self.caption = messageProtocolEntity.getCaption()
                            self.status = "feedback_location"
                            message = "Please send your location"

                        elif self.status == "lodgeComplaint_image":
                            self.url = messageProtocolEntity.getMediaUrl()
                            self.caption = messageProtocolEntity.getCaption()
                            self.status = "lodgeComplaint_location"
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
