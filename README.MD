
# PyTLM (Python TimeLine Message)

## 介绍

时序消息库，再群聊系统中经常有应用，目的是为了确保消息的顺序性，因为async是无序的,所以可以使用此库来实现消息的异步排序。

## 使用

在开发时候，可以使用此库来实现消息的异步排序，使用方法如下：
你可以从PyTLM.core中导入示例的MessageBase和MemoryStorage类来使用

## 示例

```python

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

```
