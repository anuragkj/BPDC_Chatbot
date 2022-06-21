   
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import xlrd
import pandas as pd




#locally queries the database for clubs info
class ActionTellClubInfo(Action):

    def name(self) -> Text:
        return "action_tell_club_info"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        club_name = next(tracker.get_latest_entity_values("club_name"), None)
        
        loc = ("C:\\Users\\jhaas\\Downloads\\Chatbot_demo_Telegram-20220620T052034Z-001\\Chatbot_demo_Telegram\\actions\\DB.xlsx")
        data = pd.read_excel(loc, sheet_name="Clubs")  
        data = pd.DataFrame(data)
        result_data = data.query("Name == @club_name")
        if not result_data.empty:
            msg = "Club Name : "+club_name+"\nClub Lead : "+result_data["Club_Lead"].iloc[0]+ "\nClub President : "+result_data["Club_President"].iloc[0]+"\nClub Description : "+result_data["Club_Description"].iloc[0]+"\nInstagram Handle : "+result_data["Insta_handle"].iloc[0]
        else:
            msg = f"The club you are looking for doesn't seem to exist. Could you please check again"
          
        dispatcher.utter_message(text=msg)
        
        return []

# class ActionButtonForClubInfo(Action):

#     def name(self) -> Text:
#         return "action_button_for_club_info"

#     def run(self, dispatcher, 
#             tracker: Tracker, 
#             domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        
#         buttons = [
#             {"payload":"/yes_club_info[club_info_choice](yes)", "title":"I want to know about existing clubs"},
#             {"payload":"/no_club_info[club_info_choice](no)", "title":"Not needed"},
#         ]
#         dispatcher.utter_message("Would you like to know more about the clubs already present at BPDC?", buttons = buttons)
        
#         return []