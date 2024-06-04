import random

from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram import F, Router
from config import text_otvet,text_error,command_event,command_text


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!')



@router.message(Command(commands=command_text))
async def text_command(message: Message):
    try:
        print(message.text)
        await command_event[message.text]()
    except KeyError:
        await message.answer('Нет такой команды обраитесь к администратору')



@router.message(F.text)
async def TextF(message: Message):
    try:
        await message.answer(text_otvet[message.text])
    except KeyError:
        await message.answer(text_error[random.randint(0,len(text_error)-1)])
