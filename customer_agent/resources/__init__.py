from .resources import ResourcesManager

resources = ResourcesManager()

llm = resources.get_chat_llm()

__all__ = [
    'llm',
]
