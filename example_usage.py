from PyTLM.core import MessageBase, MemoryStorage
from PyTLM.interfaces import IFilter
from PyTLM.models import MessageType, MessageStatus
import time

# 创建 MemoryStorage 实例
storage = MemoryStorage()

# 创建消息
msg1 = MessageBase()
msg1.set_message(
    msg_Type=MessageType.TEXT,
    msg_Status=MessageStatus.UNREAD,
    msg_Seq=1,
    msg_Time=int(time.time()),
    msg_Content="Hello, PyTLM!",
    msg_Metadata={"author": "Kimi"}
)

msg2 = MessageBase()
msg2.set_message(
    msg_Type=MessageType.IMAGE,
    msg_Status=MessageStatus.UNREAD,
    msg_Seq=2,
    msg_Time=int(time.time()),
    msg_Content="image_content",
    msg_Metadata={"author": "Kimi"}
)

# 将消息添加到存储
storage.add_message(msg1)
storage.add_message(msg2)

# 检索所有消息
all_messages = storage.get_all_messages()
for msg in all_messages:
    print(f"Message ID: {msg.get_sequence_id()}, Content: {msg.get_content()}")

# 定义一个简单的过滤器，筛选出文本类型的消息
class MessageFilter(IFilter):

    def __init__(self) -> None:
        self._filter = None

    def set_filter(self, filter) -> None:
        self._filter = filter

    def apply(self, message: MessageBase) -> bool:
        return self._filter(message)
    
    def __call__(self, message: MessageBase) -> bool:
        return self.apply(message)

# 应用过滤器
text_filter = MessageFilter()
text_filter.set_filter(lambda msg: msg.get_message_type() == MessageType.TEXT)
storage.set_filter(text_filter)

filtered_messages = storage.get_message_by_filter()
for msg in filtered_messages:
    print(f"Filtered Message ID: {msg.get_sequence_id()}, Content: {msg.get_content()}")