import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import aiohttp

import cfg

from Recognition import Recognition

from translate import translate

from OpenAI import generate_dialog

form_router = Router()
bot = Bot(token=cfg.telegramAPI_TOKEN, parse_mode="HTML")
context = "Hi, how are you today?"

async def download_voice_message(voice_message: types.Voice):
    file_info = await bot.get_file(voice_message.file_id)
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            if response.status == 200:
                file_data = await response.read()
                with open(f'voice.ogg', 'wb') as f:
                    f.write(file_data)
            else:
                print(f'Error downloading file. Status: {response.status}')

class Form(StatesGroup):
    voice = State()
@form_router.message(Command("voiceChat"))
async def command_start(message: types.message, state: FSMContext) -> None:
    await state.set_state(Form.voice)
    await message.answer('Бот перешел в состояние голосового чата')
@form_router.message(Command("exit"),Form.voice)
async def command_start(message: types.message, state: FSMContext) -> None:
    await state.clear()
    await message.answer('Вы вышли из режима VoiceChat')

@form_router.message(Form.voice)
async def command_start(message: types.message, state: FSMContext) -> None:
    global context
    try:
        voice_message = message.voice
        await download_voice_message(voice_message)

       # user_input = translate(Recognition(),"en")
        #generated_text = generate_dialog(prompt=context + " " + user_input,
                                    # model="davinci",
                                     #token_max_length=150)
       # context += " " + user_input + " " + generated_text
        #await message.answer(translate(generated_text,"ru"))
        await message.answer(Recognition())
    except:
        await message.answer('Это не голосовое! Выйдите из этого режима командой /exit чтобы общаться текстом')
async def main():
    bot = Bot(token=cfg.telegramAPI_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(form_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())