import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "9193177259:AAFWtk_zz0D72AumxSourRDVAkhTdSLb6N0"
WEB_APP_URL = "https://github.io"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer("Привет! Отправь мне комикс в формате .cbz или .zip, и я открою его в читалке.")

@dp.message(F.document)
async def handle_comic(message: types.Message):
    doc = message.document
    if not (doc.file_name.endswith('.cbz') or doc.file_name.endswith('.zip') or doc.file_name.endswith('.cbr')):
        await message.answer("Пожалуйста, отправьте файл в формате .cbz или .zip")
        return
        
    status = await message.answer("Генерирую ссылку для чтения...")
    file_info = await bot.get_file(doc.file_id)
    direct_link = f"https://telegram.org{BOT_TOKEN}/{file_info.file_path}"
    
    web_app_link = f"{WEB_APP_URL}?file={direct_link}"
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📖 Читать комикс", webApp=WebAppInfo(url=web_app_link))]
    ])
    
    await status.delete()
    await message.answer(f"Комикс «{doc.file_name}» готов к чтению!", reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
