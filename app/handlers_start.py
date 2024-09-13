# import os
from dotenv import load_dotenv
from aiogram import Router
from aiogram.types import Message
from utils import views

router = Router()


# load_dotenv()

# ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")
# NEED_KEY = os.getenv("NEED_KEY")
# FOR_KEY = os.getenv("FOR_KEY")

async def start_command(message: Message) -> None:
    await message.answer(text=views.start_message())


