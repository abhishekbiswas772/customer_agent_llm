from langgraph.constants import END
from customer_agent.simulator import graph



if __name__ == '__main__':
    for chuck in graph.stream({
        "messages" : []
    }):
        if END not in chuck:
            print(chuck)
            print("--------------------------------------------")

