
from enum import StrEnum

class MessageType(StrEnum):
    """ 消息类型 """
    TEXT = "text"
    IMAGE = "image"
    VOICE = "voice"
    VIDEO = "video"
    FILE = "file"
    LOCATION = "location"
    EVENT = "event"

class MessageStatus(StrEnum):
    """ 消息状态 """
    UNREAD = "unread"
    READ = "read"
    DELETED = "deleted"