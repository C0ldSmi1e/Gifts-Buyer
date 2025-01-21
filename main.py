import asyncio
import traceback
from typing import Set

from pyrogram import Client
from pyrogram.errors.exceptions import RPCError
from pytz import timezone as _timezone

import config
from src.banner import title, info, cmd, get_locale
from src.callbacks import update_callback, new_callback
from utils.common import get_time, send_notification, format_number
from utils.detector import detector
from utils.utils import buyer

sent_gift_ids: Set[int] = set()
timezone = _timezone(config.TIMEZONE)
app_info = info()
language, _ = get_locale(config.LANGUAGE)


async def send_greeting(client: Client, chat_id: int) -> bool:
    """
    Send a greeting message to a specified chat.
    
    Args:
        client (Client): Pyrogram client instance
        chat_id (int): Telegram chat ID to send message to
        
    Returns:
        bool: True if message sent successfully, False if failed
    """
    try:
        await client.send_message(
            chat_id,
            "👋 Just a quick check-in! Feel free to ignore this message.\n\n"
            "⭐Sent via <a href='https://github.com/bohd4nx/TGgifts-buyer'>Gifts Buyer</a>\n"
            "🧑‍💻Developed by @B7XX7B (@GiftsTracker)",
            disable_web_page_preview=True
        )
        await client.get_users(chat_id)
        return True
    except RPCError:
        return False


async def send_start_message(client: Client) -> None:
    """Send start message to configured channel with current settings."""
    ranges_info = "\n".join([
        f"💰 {min_price}-{max_price} | 🎁 {num_gifts}x | ⚡️ Supply: {format_number(supply)}"
        for min_price, max_price, supply, num_gifts in config.GIFT_RANGES
    ])

    message = f"{config.locale.start_message.format(ranges_info=ranges_info)}\n\n"
    await send_notification(client, message)


async def process_gifts(client: Client) -> None:
    """
    Process gift sending for all configured users and gift IDs.
    Handles sending gifts to each user with error handling and delay between sends.
    
    Args:
        client (Client): Pyrogram client instance
    """
    locale = config.locale
    for gift_id in config.GIFT_IDS:
        if gift_id in sent_gift_ids:
            continue

        for chat_id in config.USER_ID:
            try:
                if await send_greeting(client, chat_id):
                    await buyer(client, chat_id, int(gift_id))
                    await asyncio.sleep(5)
            except RPCError as ex:
                print(
                    f"\n\033[91m[ ERROR ]\033[0m {locale.purchase_error.format(gift_id, chat_id)}\n{str(ex)}\n"
                )

        sent_gift_ids.add(gift_id)


async def main() -> None:
    """
    Main application entry point.
    Initializes the Telegram client and orchestrates the gift sending process.
    Handles client lifecycle and detector setup.
    """
    cmd(app_info)
    title(app_info, language)

    async with Client(
            name=config.SESSION,
            api_id=config.API_ID,
            api_hash=config.API_HASH
    ) as client:
        await send_start_message(client)
        await process_gifts(client)
        await detector(client, new_callback, update_callback)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        current_time = get_time(timezone)
        print(f"\n\n\033[91m[ INFO ]\033[0m \033[1m{config.locale.terminated}\033[0m - {current_time}")
    except Exception as ex:
        print(f"\n\n\033[91m[ ERROR ]\033[0m {config.locale.unexpected_error}")
        traceback.print_exc()
