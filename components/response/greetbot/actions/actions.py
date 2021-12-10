# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name_value = next(tracker.get_latest_entity_values("name"), None)
        print('name_value: ', name_value)

        # 方法一 直接发送消息给用户
        dispatcher.utter_message(response='utter_greet', name=name_value)

        # 方法二 通过设置slot: name的值为name_value 然后通过utter_greet发送给用户 只有slot(name)的type为from_entity才会设置生成
        # SlotSet(key="name", value=name_value)

        return []
