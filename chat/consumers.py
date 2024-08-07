from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(JsonWebsocketConsumer):
    SQUARE_GROUP_NAME = "square"
    groups = [SQUARE_GROUP_NAME]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""

    def connect(self):
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.group_name = f"chat-{room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, code):
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name,
                self.channel_name,
            )

    def receive_json(self, content, **kwargs):
        _type = content["type"]

        if _type == "chat.message":
            message = content["message"]
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat.message",
                    "message": message,
                },
            )
        else:
            print(f"Invalid message type: {_type}")

    def chat_message(self, message_dict):
        self.send_json(
            {
                "type": "chat.message",
                "message": message_dict["message"],
            }
        )
