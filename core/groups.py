

from config import config
from core.queue import Queue
from pyrogram.types import Message
from typing import Dict, Any, Union
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import EditGroupCallTitle

GROUPS: Dict[int, Dict[str, Any]] = {}


def all_groups():
    return GROUPS.keys()


def set_default(chat_id: int) -> None:
    global GROUPS
    GROUPS[chat_id] = {}
    GROUPS[chat_id]["is_playing"] = False
    GROUPS[chat_id]["now_playing"] = None
    GROUPS[chat_id]["is_video"] = False
    GROUPS[chat_id]["loop"] = False
    GROUPS[chat_id]["lang"] = config.LANGUAGE
    GROUPS[chat_id]["queue"] = Queue()


def get_group(chat_id) -> Dict[str, Any]:
    return GROUPS[chat_id]


def set_group(chat_id: int, **kwargs) -> None:
    global GROUPS
    for key, value in kwargs.items():
        GROUPS[chat_id][key] = value


async def set_title(message_or_chat_id: Union[Message, int], title: str, **kw):
    if isinstance(message_or_chat_id, Message):
        client = message_or_chat_id._client
        chat_id = message_or_chat_id.chat.id
    elif isinstance(message_or_chat_id, int):
        client = kw.get("client")
        chat_id = message_or_chat_id
    try:
        peer = await client.resolve_peer(chat_id)
        chat = await client.send(GetFullChannel(channel=peer))
        await client.send(EditGroupCallTitle(call=chat.full_chat.call, title=title))
    except:
        pass


def get_queue(chat_id: int) -> Queue:
    return GROUPS[chat_id]["queue"]


def clear_queue(chat_id: int) -> None:
    global GROUPS
    GROUPS[chat_id]["queue"].clear()


def shuffle_queue(chat_id: int) -> Queue:
    global GROUPS
    return GROUPS[chat_id]["queue"].shuffle()
