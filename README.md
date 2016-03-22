## Personal-Assistant
Zenbot is a query based Personal-Assistant which responds to the user query after the required computation.

## Purpose
 - The main purpose for this application is to bridge gap between the citizens and the government. This is mainly focused on providing the real time feedback by the citizens by which the officials can track the progress of all the contracts in the city.
 Secondly, this also tells user about the nearby hotels, hospitals; apart from that it also helps user to get their train info as well as the pnr status of their pnr and they can do all these things using Whats'app.

## How to use
 It's fairly simple to use zenbot.
 - Add a number give by us to your contact list.
 - Create a whats'app group with that number in it.
 - That's it you are done. To list out all the actions type #info.

## Different actions it provide
 - #info : this lists out all the actions provided by the bot.
 - #projects : list out all the projects in user's neighbourhood when location is provided. This is a data which is provided by a NGO called "Janagraha" so basically this is a real data.
 - #complaintsNearby : this lists out the complaints that are registered in user's locality. User will have to provide his location information.
 - #complaints <complaint-id> : In this request complaint-id is the unique id which can be seen when complaintsNearby is called and user can keep a track of the status of their complaints.
 - #feedback <Seriol No.> : User can give a real time feedback to the government using this. He only need to have the serial id of the project going on and then he can upload the image of with the current location of the user.
 - #hotels : list out all the hotels in user's locality.
 - #hospitals : list out all the hospitals in user's locality.
 - #pnr <pnr-number> : tells user all the pnr status of the pnr-number. pnr-number should be working as for now we have not handled the corner cases.
 - #trainStatus <train number> <doj yearmonthday> : this is something cool which helps user to keep a track of the status of the train in which he has to give train number and doj in the "yearmonthday" format for eg: 201603221

## Things user need to keep in mind:
 - We are trying to make things more and more easy for the user so make sure you have typed the current action name.
 - There are various other scripts running for that you will need your api key which you will have to use for api calls.
 - There are other scripts which you can use without api keys.
 - The real time data used was provided by iChangeMyCity
