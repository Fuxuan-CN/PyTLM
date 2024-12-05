""" 消息层接口 """

from abc import ABC, abstractmethod
from typing import Union
from ..models import Message , MessageStatus , MessageType

class IMessage(ABC):
    """ 消息层接口 """

    @abstractmethod
    def set_message(self, message: Message) -> None:
        """ 设置消息 """
        pass

    @abstractmethod
    def get_sequence_id(self) -> int:
        """ 获取消息序列号 """
        pass

    @abstractmethod
    def get_content(self) -> Union[str, bytes]:
        """ 获取消息内容 """
        pass

    @abstractmethod
    def get_timestamp(self) -> int:
        """ 获取消息时间戳 """
        pass

    @abstractmethod
    def get_message_type(self) -> MessageType:
        """ 获取消息类型 """
        pass

    @abstractmethod
    def get_message_meta(self) -> dict:
        """ 获取消息元数据 """
        pass

    @abstractmethod
    def get_message_status(self) -> MessageStatus:
        """ 获取消息状态 """
        pass