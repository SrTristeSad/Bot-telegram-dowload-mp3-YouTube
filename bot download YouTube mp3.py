import asyncio
import os
import subprocess
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT_TOKEN_HERE'


import logging
logging.basicConfig(level=logging.INFO)


bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Digite /download para iniciar o download de um vídeo.")

@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await message.answer("Este é o meu assistente de download de vídeo do YouTube. Envie uma URL de vídeo do YouTube e eu vou baixá-lo e converter para MP3. Em seguida, enviarei o arquivo MP3 de volta para você. Use o comando '/download' para iniciar.")

@dp.message_handler(commands='download')
async def cmd_download(message: types.Message):
    await message.answer("Envie a URL do vídeo que você deseja baixar.")
    await bot.register_next_step_handler(message, process_url)

async def process_url(message: types.Message):
    url = message.text
    await bot.send_message(chat_id=message.chat.id, text="Baixando...")

   
    process = await asyncio.create_subprocess_exec(
        'youtube-dl', '-o', 'video.%(ext)s', url,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()

    if stderr:
        await bot.send_message(chat_id=message.chat.id, text="Ocorreu um erro ao baixar o vídeo.")
        return

    await bot.send_message(chat_id=message.chat.id, text="Convertendo para MP3...")

    
    process = await asyncio.create_subprocess_exec(
        'ffmpeg', '-i', 'video.mp4', 'audio.mp3',
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()

    if stderr:
        await bot.send_message(chat_id=message.chat.id, text="Ocorreu um erro ao converter o vídeo para MP3.")
        return

    await bot.send_message(chat_id=message.chat.id, text="Enviando MP3...")

    
    with open("audio.mp3", "rb") as f:
        await bot.send_audio(chat_id=message.chat.id, audio=f)

    
    os.remove("video.mp4")
    os.remove("audio.mp3")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

