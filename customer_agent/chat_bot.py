from langchain_core.messages import BaseMessage
from langchain_core.runnables import RunnableSerializable
from .resources import llm
from typing import Dict, List
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

system_message : Dict = {
    "role" : "system",
    "content" : "You are an customer support agent for food delivery service"
}

user_system_prompt : ChatPromptTemplate = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a customer of an food delivery company."
        "You are interacting with a user who is a customer support person."
        "{instructions}"
        "When you are finished with the conversation, respond with a single word 'FINISHED'"
    ),
    MessagesPlaceholder(variable_name="messages")
])


def build_simulated_user() -> RunnableSerializable[dict, BaseMessage]:
    final_prompt = user_system_prompt.partial(
        name = "Abhishek",
        instructions = ("Your name is Abhishek. You are trying to get a refund for the Biryani you ordered "
                        "You want them to give you ALL the money back."
                        "This order happened 1 day ago.")
    )
    user_simulation = final_prompt | llm
    return user_simulation



def build_chat_bot(messages: List[Dict]) -> Dict:
    final_messages = [system_message] + messages
    docs = llm.invoke(final_messages)
    docs_json = docs.to_json()
    content_docs = dict(docs_json.get("kwargs", ""))
    return content_docs

