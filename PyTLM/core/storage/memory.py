
from ...interfaces import IStorage , IFilter , IMessage
from asyncio import Future
import asyncio

class MemoryStorage(IStorage):
    """ 内存存储层 """

    def __init__(self):
        self.messages: dict[int, IMessage] = {}
        self.filter = None
        
    def set_filter(self, filter: IFilter) -> None:
        self.filter = filter

    def get_all_messages(self):
        return list(self.messages.values())
    
    async def get_all_messages_async(self):
        futute = Future()
        futute.set_result(self.messages)
        return futute
    
    def get_message_by_filter(self):
        if self.filter is None:
            return list(self.messages.values())
        else:
           return [ message for _ , message in self.messages.items() if self.filter(message)]
        
    async def get_message_by_filter_async(self):
        future = Future()
        task = asyncio.create_task(asyncio.to_thread(self.get_message_by_filter))
        future.set_result(await task)
        return future

    def add_message(self, message: IMessage):
        self.messages[message.get_sequence_id()] = message

    async def add_message_async(self, message: IMessage) -> None:
        if message.get_sequence_id() in self.messages:
            return
        task = asyncio.create_task(asyncio.to_thread(self.add_message, message))
        return task
    
    def update(self, message: IMessage) -> None:
        self.messages[message.get_sequence_id()] = message

    async def update_async(self, message: IMessage) -> None:
        task = asyncio.create_task(asyncio.to_thread(self.update, message))
        return task