from langchain_community.adapters.openai import convert_message_to_dict
from langchain_core.messages import AIMessage, HumanMessage
from .chat_bot import build_chat_bot, build_simulated_user

def build_chat_node(state):
    messages = state["messages"]
    message = [convert_message_to_dict(message) for message in messages]
    chat_bot_response = build_chat_bot(message)
    return {
        "messages" : [AIMessage(content=chat_bot_response.get("content", ""))],
    }


def _swap_roles(messages):
    new_messages = []
    for message in messages:
        if isinstance(message, AIMessage):
            new_messages.append(HumanMessage(content=message.content))
        else:
            new_messages.append(AIMessage(content=message.content))
    return new_messages


def build_simulated_user_node(state):
    messages = state["messages"]
    new_messages = _swap_roles(messages)
    response_from_simulated_user = build_simulated_user()
    response_from_simulated_user = response_from_simulated_user.invoke({
        "messages": new_messages
    })
    return {
        "messages" : [HumanMessage(content=response_from_simulated_user.content)],
    }
