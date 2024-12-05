""" 消息定义 """

from ...interfaces import IMessage
from ...models import Message , MessageStatus , MessageType
import time

class MessageBase(IMessage):
    """ 消息基类 """
    
    def __init__(self) -> None:
        self._message: Message = None

    def set_message(self,
        msg_Type: MessageType = MessageType.TEXT,
        msg_Status: MessageStatus = MessageStatus.UNREAD,
        msg_Seq: int = 0,
        msg_Time: int = int(time.time()),
        msg_Content: str | bytes = "",
        msg_Metadata: dict[str, str] | None = {}
    ) -> None:
        """ 设置消息 """
        msg = Message(Mtype=msg_Type, 
            Mstatus=msg_Status, 
            Mseq=msg_Seq, 
            Mtime=msg_Time, 
            Mcontent=msg_Content, 
            Mmeta=msg_Metadata
        )
        self._set_message(msg)
        

    def _set_message(self, message: Message) -> None:
        self._message = message

    def get_sequence_id(self) -> int:
        """ 获取消息序列ID """
        return self._message.Mseq
    
    def get_content(self) -> str | bytes:
        """ 获取消息内容 """
        return self._message.Mcontent
    
    def get_message_meta(self) -> dict:
        """ 获取消息元数据 """
        return self._message.Mmeta
    
    def get_message_type(self) -> MessageType:
        """ 获取消息类型 """
        return self._message.Mtype
    
    def get_message_status(self) -> MessageStatus:
        """ 获取消息状态 """
        return self._message.Mstatus
    
    def get_timestamp(self) -> int:
        """ 获取消息时间戳 """
        if self._message.Mtime is None:
            self._message.Mtime = int(time.time())
        return self._message.Mtime