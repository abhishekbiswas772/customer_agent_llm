from langchain_core.messages import HumanMessage
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict
from customer_agent.edges import should_continue
from customer_agent.nodes import build_simulated_user_node, build_chat_node


class State(TypedDict):
    messages : Annotated[list, add_messages]


def build_human_input_node(state):
    user_input = input("You: ")
    return {
        "messages": [HumanMessage(content=user_input)],
    }

builder = StateGraph(State)
builder.add_node("user", build_simulated_user_node)
builder.add_node("chat_bot", build_chat_node)
builder.add_edge("chat_bot", "user")
builder.add_conditional_edges(
    "user",
    should_continue,
    {
        "end": END,
        "continue" : "chat_bot",
    }
)
builder.add_edge(START, "chat_bot")
graph = builder.compile()
graph.get_graph().draw_mermaid_png(output_file_path="flow_simulation_chat_bot.png")