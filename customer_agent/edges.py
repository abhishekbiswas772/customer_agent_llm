
def should_continue(state):
    messages = state['messages']
    if len(messages) > 15:
        return "end"
    elif messages[-1] == "FINISHED":
        return "end"
    else:
        return "continue"

