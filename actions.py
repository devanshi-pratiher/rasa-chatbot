# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from datetime import date
from typing import Any, Text, Dict, List
import sqlite3
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "London": "UTC+1:00"
}


class ActionMyName(Action):

    def name(self) -> Text:
        return "utter_my_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_my_name")

        return []


class DisplayStatus(Action):

    def name(self) -> Text:
        return "user_wants_to_check_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_status_info")
        return []


class ActionAskUsn(Action):

    def name(self) -> Text:
        return "action_ask_usn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_ask_usn")

        return []


class ActionAskPassword(Action):

    def name(self) -> Text:
        return "action_ask_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_ask_password")

        return []

class ActionValidateCredentials(Action):

    def name(self) -> Text:
        return "validate_credentials_and_display_status"

    def run(self, dispatcher: CollectingDispatcher,
      tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_happy")
        return []
'''
        messages = []
        print("tracker : ", tracker)

        for event in (list(tracker.events)):
            print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        Name = messages[-2]
        Pass = str((tracker.latest_message)['text'])
        conn = sqlite3.connect('home.db')
        query = "select * from USER where Name = '{0}' and Pass = '{1}'".format(Name,Pass)           
        print("Final query : ",query)
        df = pd.read_sql(query, conn)

        if df.shape[0] == 1:
                print("Final query : ",df)
        else:
            content = "Sorry your credentials are incorrect. Please enter valid credentials next time"
'''


class ValidateCredentialsAndDisplayLights(Action):

    def name(self) -> Text:
        print("tracker ")
        return "validate_credentials_and_display_lights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_light_info")


        return []



class ValidateCredentialsAndDisplayAcs(Action):

    def name(self) -> Text:
        print("tracker ")
        return "validate_credentials_and_display_ac"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_light_info")

        return []

class ValidateCredentialsAndDisplayFans(Action):

    def name(self) -> Text:
        return "validate_credentials_and_display_fans"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_off_status")
        return []

class ValidateCredentialsAndDisplayLights(Action):

    def name(self) -> Text:
        print("tracker ")
        return "validate_credentials_and_display_lights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_light_info")        

        return []


class ActionCheckstatus(Action):

    def name(self) -> Text:
        return "my_name_is"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_my_name")

        return []




class ActionAcInfo(Action):

    def name(self) -> Text:
        return "action_ac_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_ac_info")

        return []

class ActionFanInfo(Action):

    def name(self) -> Text:
        return "action_fan_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_fan_info")

        return []

class DisplayUpcomingAlarms(Action):

    def name(self) -> Text:
        return "display_upcoming_alarms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_fallback")

        return []

class MyFallback(Action):

    def name(self) -> Text:
        return "action_my_fallback"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_fallback")

        return []

class YourResidence(Action):

    def name(self) -> Text:
        return "action_your_residence"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_residence")
        str((tracker.latest_message)['text'])
        return []

class ActionLightInfo(Action):

    def name(self) -> Text:
        return "action_light_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_light_info")        

        return []
