
from pydantic import BaseModel
from ._enums import MessageType, MessageStatus


class Message(BaseModel):
    """ 消息模型 """
    Mtype: MessageType
    Mstatus: MessageStatus
    Mseq: int
    Mtime: int
    Mcontent: str
    Mmeta: dict[str, str]