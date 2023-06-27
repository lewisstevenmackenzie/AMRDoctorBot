# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionTellUseCaseExample(Action):
    def name(self) -> Text:
        return "action_tell_use_case_example"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        import random as rnd

        UseCase1 = "Hi Doctor, I’m not feeling 100% today. I think I might have a cold. I’ve got a runny nose, my throat is also a bit red and sore, and I’ve had a dry cough for a couple of days. Can I have some antibiotics, please?"

        UseCase2 = "Hello Doctor, I feel terrible today and  think I've got a chest infection. I've had a persistent cough for a couple of days, I've been coughing up yellow phlegm and I've got a temperature. I'm also feeling quite breathless. Can I have antibiotics, please? "

        rnd_num = rnd.random()

        if rnd_num < 0.5:
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

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        import random as rnd
        from datetime import datetime

        chatbotID = tracker.slots.get("conversationID")

        if chatbotID is None:
            # Getting the current date and time
            dt = datetime.now()

            # getting the timestamp
            ts = datetime.timestamp(dt)

            print("Timestamp is:", ts)

            rnd_num = rnd.random()
            msg = "Right, I'm going to give you a number, could you please type this into the MTurk response so that we can match this conversation to your survey inorder to assure you are paid appropriatly \n"

            msg = msg + f"Your unique chatbot number is: {ts}\n"

            # msg = msg + f"Hi, my name is sarah, I'm 40 years old and I've got a bacterial infection that is causing swelling in my throat etc.\n"

            # msg = msg + f"Would you recommend an antibiotic to treat me?\n"

            dispatcher.utter_message(text=msg)

            return [SlotSet("conversationID", ts)]
        else:
            msg = "Your unique chatbot number is: " + str(chatbotID)

            dispatcher.utter_message(text=msg)

        return []


class ActionRepeatSymptoms(Action):
    def name(self) -> Text:
        return "action_repeat_symptoms"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        symptoms1 = "I’ve got a runny nose, my throat is also a bit red and sore, and I’ve had a dry cough for a couple of days. Do you think that antibiotics will help me feel better?"
        msg = f"{symptoms1}\n"

        # msg = msg + f"Hi, my name is sarah, I'm 40 years old and I've got a bacterial infection that is causing swelling in my throat etc.\n"

        # msg = msg + f"Would you recommend an antibiotic to treat me?\n"

        dispatcher.utter_message(text=msg)

        return []


class ActionRandomQuestion(Action):
    def name(self) -> Text:
        return "action_ask_random_question"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        import random as rnd

        flag = 0
        counter = 0

        questions = [
            "Thanks, I also saw on an information poster somthing about antimicrobial resistance. What's that?",
            "Okay, thanks for helping me. I was also curious as to when would you normally prescribe antibiotics?",
            "I've got a bit of a random question but what happens if i stop taking antibiotics when I feel better but before the end of my cycle?",
            "What sort of medication would you suggest I take if not antibiotics?",
        ]

        Q1 = tracker.slots.get("question1")
        Q2 = tracker.slots.get("question2")
        Q3 = tracker.slots.get("question3")

        if Q1 == "True":
            del questions[0]
            counter += 1
        if Q2 == "True":
            del questions[1]
            counter += 1
        if Q3 == "True":
            del questions[2]
            counter += 1
        if Q1 is not None:
            print("Q1: " + Q1)
        if Q2 is not None:
            print("Q2: " + Q2)
        if Q3 is not None:
            print("Q3: " + Q3)

        print("This is the length of questions: " + str(len(questions)))
        print("THis is the counter value: " + str(counter))

        if len(questions) == 0:
            flag = 1

        while flag == 0 and counter < 2:
            qNumber = rnd.randint(0, len(questions) - 1)
            print("this is Qnumber:" + str(qNumber))
            print("this is Questions length before deleting:" + str(len(questions)))
            msg = questions[qNumber]

            # questions.remove(qNumber)

            del questions[qNumber]

            print("this is Questions length after deleting:" + str(len(questions)))

            print(questions)

            counter += 1
            dispatcher.utter_message(text=msg)
            slotToBeSet = "question" + str(qNumber + 1)
            return [SlotSet(slotToBeSet, "True")]

        msg = "I think that's all the questions i have for you."

        dispatcher.utter_message(text=msg)

        return [FollowupAction("action_final_question")]


class ActionFinalQuestion(Action):
    def name(self) -> Text:
        return "action_final_question"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        msg = "Is there anything else I should know about antibiotics?"

        dispatcher.utter_message(text=msg)

        return []


class ActionEndConversation(Action):
    def name(self) -> Text:
        return "action_end_conversation"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        msg = "okay, thanks for chatting to me. I'll take on board the information you've given me when I come for future consultations."

        dispatcher.utter_message(text=msg)

        return [FollowupAction("action_generate_chatbot_number")]
