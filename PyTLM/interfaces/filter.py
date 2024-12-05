""" 过滤器接口 """

from abc import ABC, abstractmethod
from typing import Callable
from .message import IMessage

class IFilter(ABC):
    """ 过滤器接口 """

    def set_filter(self, filter: Callable[[IMessage], bool]) -> None:
        """ 设置过滤器 """
        pass

    @abstractmethod
    def __call__(self, message: IMessage, *args, **kwargs) -> bool:
        """ 应用过滤器到消息上，并返回是否通过过滤 """
        pass

    @abstractmethod
    def apply(self, message: IMessage) -> bool:
        """ 应用过滤器到消息上，并返回是否通过过滤 """
        pass