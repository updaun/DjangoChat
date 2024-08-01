import os
import django
import asyncio

from channels.layers import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


async def main():
    channel_layer = get_channel_layer()

    message_dict = {
        "content": "world",
    }

    await channel_layer.send("hello", message_dict)
    response_dict = await channel_layer.receive("hello")
    is_equal = message_dict == response_dict
    print(is_equal)


asyncio.run(main())
