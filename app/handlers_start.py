import os
from dotenv import load_dotenv
from aiogram import Router, types
from aiogram.filters import CommandStart
from app.handler_text import *

router = Router()

load_dotenv()

ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")
NEED_KEY = os.getenv("NEED_KEY")
FOR_KEY = os.getenv("FOR_KEY")
