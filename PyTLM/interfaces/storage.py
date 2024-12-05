""" 存储层接口 """

from abc import ABC, abstractmethod
from typing import Iterable
from .message import IMessage
from .filter import IFilter
from asyncio import Future , Task

class IStorage(ABC):
    """ 存储层接口 """

    @abstractmethod
    def set_filter(self, filter: IFilter) -> None:
        """ 设置过滤器 """
        pass

    @abstractmethod
    def get_all_messages(self) -> Iterable[IMessage]:
        """ 获取所有消息 """
        pass

    @abstractmethod
    async def get_all_messages_async(self) -> Future[Iterable[IMessage]]:
        """ 异步获取所有消息 """
        pass

    @abstractmethod
    def get_message_by_filter(self, filter: IFilter) -> Iterable[IMessage]:
        """ 根据过滤器获取消息 """
        pass

    @abstractmethod
    async def get_message_by_filter_async(self, filter: IFilter) -> Future[Iterable[IMessage]]:
        """ 异步根据过滤器获取消息 """
        pass

    @abstractmethod
    def add_message(self, message: IMessage) -> None:
        """ 添加消息 """
        pass

    @abstractmethod
    async def add_message_async(self, message: IMessage) -> Task:
        """ 异步添加消息 """
        pass

    @abstractmethod
    def update(self, message: IMessage) -> None:
        """ 更新消息 """
        pass

    @abstractmethod
    async def update_async(self, message: IMessage) -> Task:
        """ 异步更新消息 """
        pass