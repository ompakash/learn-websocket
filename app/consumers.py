from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Websocket connected...", event)
        self.send({
            "type" : "websocket.accept"
        })
    
    def websocket_receive(self,event):
        print("Message received from client", event)
        print(event['text'])
        for i in range(50):
            self.send({
            "type" : "websocket.send",
            "text" : str(i)
            })
            sleep(1)


    def websocket_disconnect(self,event):
        print("Websocket disconnected...", event)
        raise StopConsumer()

    
class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Websocket connected async...", event)
        await self.send({
            "type" : "websocket.accept"
        })
    
    async def websocket_receive(self,event):
        print("Message received from client async", event)
        print(event['text'])
        for i in range(50):
            await self.send({
            "type" : "websocket.send",
            "text" : str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self,event):
        print("Websocket disconnected async...", event)
        raise StopConsumer()

