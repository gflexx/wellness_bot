from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_GENDERS = ['male', 'female']
ALLOWED_AGE_CATEGORIES = ['child', 'adult']


class ValidateDiagnosisForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_diagnosis_form"
    
    def validate_gender(
            self, slot_value: Any, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: DomainDict
    ) -> Dict[Text, Any]:
        
        """ validate gender """

        if slot_value.lower() not in ALLOWED_GENDERS:
            dispatcher.utter_message(
                text="We only allow: male/female"
            )
            return {"gender": None}
        return {"gender": slot_value}
    
    def validate_age_group(
            self, slot_value: Any, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: DomainDict
    ) -> Dict[Text, Any]:
        
        """ validate age group """

        if slot_value.lower() not in ALLOWED_AGE_CATEGORIES:
            dispatcher.utter_message(
                text="We only allow: child/adult"
            )
            return {"age_group": None}
        return {"age_group": slot_value}
    
    def validate_age(
            self, slot_value: Any, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: DomainDict
    ) -> Dict[Text, Any]:
        
        """ validate age """

        value = 0
        try:
            value = int(slot_value)
        except ValueError as err:
            dispatcher.utter_message(
                text="Age has to be numeric"
            )
            return {"age": None}
        return {"age": slot_value}


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    

class ActionCheckDisease(Action):

    def name(self) -> Text:
        return "action_check_disease"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        """ get disease from symptoms """
        
        gender = tracker.get_slot("gender")
        age = tracker.get_slot("age")
        age_group = tracker.get_slot("age_group")
        

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionGetDoctor(Action):
    def name(self) -> Text:
        return "action_get_doctor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doctor = tracker.get_slot("doctor")

        dispatcher.utter_message(
            text=f"Getting doctor: {doctor}"
        )

        return []
    

class ActionGetBlog(Action):
    def name(self) -> Text:
        return "action_get_blog"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        blog = tracker.get_slot("blog")

        dispatcher.utter_message(
            text=f"Searching for blog: {blog}"
        )

        return []


class ActionGetProduct(Action):
    def name(self) -> Text:
        return "action_get_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product = tracker.get_slot("product")

        dispatcher.utter_message(
            text=f"Searching for product: {product}"
        )

        return []


class ActionGetPharmacy(Action):
    def name(self) -> Text:
        return "action_get_pharmacy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pharmacy = tracker.get_slot("pharmacy")

        dispatcher.utter_message(
            text=f"Searching for pharmacy: {pharmacy}"
        )

        return []
