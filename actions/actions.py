# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionTellUseCaseExample(Action):

    def name(self) -> Text:
        return "action_tell_use_case_example"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import random as rnd
        
        UseCase1 = "Hi Doctor, I’m not feeling 100% today. I think I might have a cold. I’ve got a runny nose, my throat is also a bit red and sore, and I’ve had a dry cough for a couple of days. Can I have some antibiotics, please?"

                
        UseCase2 = "Hello Doctor, I feel terrible today and  think I've got a chest infection. I've had a persistent cough for  a couple of days, I've been coughing up yellow phlegm and I've got a temperature. I'm also feeling quite breathless. Can I have antibiotics, please? "
                
        rnd_num = rnd.random()

        if (rnd_num<0.5):
            print("Use case 1")
            msg = UseCase1
        else:
            print("Use Case 2")
            msg = UseCase2
            
        dispatcher.utter_message(text=msg)

        return []

class ActionGenerateChatbotNumber(Action):

    def name(self) -> Text:
        return "action_generate_chatbot_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import random as rnd
        from datetime import datetime

        # Getting the current date and time
        dt = datetime.now()

        # getting the timestamp
        ts = datetime.timestamp(dt)

        print("Timestamp is:", ts)

        rnd_num = rnd.random()
        msg = "Right, I'm going to give you a number, could you please type this into the MTurk response so that we can match this conversation to your survey inorder to assure you are paid appropriatly \n"   
         
        msg = msg + f"Your unique chatbot number is: {ts}\n"

        # msg = msg + f"Hi, my name is sarah, I'm 40 years old and I've got a bacterial infection that is causing swelling in my throat etc.\n"

        #msg = msg + f"Would you recommend an antibiotic to treat me?\n"

        dispatcher.utter_message(text=msg)

        return []

class ActionRepeatSymptoms(Action):

    def name(self) -> Text:
        return "action_repeat_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        symptoms1 = "I’ve got a runny nose, my throat is also a bit red and sore, and I’ve had a dry cough for a couple of days. Do you think that antibiotics will help me feel better?"
        msg = f"{symptoms1}\n"

        # msg = msg + f"Hi, my name is sarah, I'm 40 years old and I've got a bacterial infection that is causing swelling in my throat etc.\n"

        #msg = msg + f"Would you recommend an antibiotic to treat me?\n"

        dispatcher.utter_message(text=msg)

        return []