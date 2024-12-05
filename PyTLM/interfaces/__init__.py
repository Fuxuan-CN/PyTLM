""" 接口模块 """

from .message import IMessage
from .storage import IStorage
from .filter import IFilter

__all__ = [
    "IMessage",
    "IStorage",
    "IFilter"
]