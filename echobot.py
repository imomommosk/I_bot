import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6819864783:AAFzAtiR0b-RydUrelmCL1GOqFSsWFMRZ18'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['botni_yoqish'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Privet JOXANI IDsi:51762532051")

    await message.reply("ImomMoskning IDsi:52006580098")

    await message.reply("NOT SHAXANING IDsi IDsi:51970145203")

    await message.reply("AZIZBEKNING IDsi:51789697969")

    await message.reply("Zeroning IDsi:61539525935")

    await message.reply("Qode Madaraning IDsi:51760335176")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Salom foydalanuvchi 'I_BOT'ga xush kelipsiz""")

@dp.message_handler(commands=['python'])
async def send_welcome(message: types.Message):
    await message.reply("""https://t.me/py_basic/4""")

    await message.reply("""https://t.me/py_basic/28""")

    await message.reply("""https://t.me/py_basic/43""")

    await message.reply("""https://t.me/py_basic/42""")

    await message.reply("""https://t.me/py_basic/49""")

    await message.reply("""https://t.me/py_basic/69""")

    await message.reply("""https://t.me/py_basic/73""")

    await message.reply("""https://t.me/py_basic/92""")

    await message.reply("""https://t.me/py_basic/93""")

    await message.reply("""https://t.me/py_basic/143""")

    await message.reply("""https://t.me/py_basic/176""")

    await message.reply("""https://t.me/py_basic/198""")#12

    await message.reply("""https://t.me/py_basic/245""")

    await message.reply("""https://t.me/py_basic/252""")

    await message.reply("""https://t.me/py_basic/264""")

    await message.reply("""https://t.me/py_basic/284""")

    await message.reply("""https://t.me/py_basic/298""")

    await message.reply("""https://t.me/py_basic/310""")

    await message.reply("""https://t.me/py_basic/324""")

    await message.reply("""https://t.me/py_basic/323""")

    await message.reply("""https://t.me/py_basic/334""")

    await message.reply("""https://t.me/py_basic/335""")

    await message.reply("""https://t.me/py_basic/342""")

    await message.reply("""https://t.me/py_basic/344""")  # 24

    await message.reply("""https://t.me/py_basic/348""")  # 25

    await message.reply("""https://t.me/py_basic/349""")  # 26

    await message.reply("""https://t.me/py_basic/360""")  # 27

    await message.reply("""https://t.me/py_basic/359""")  # 28

    await message.reply("""https://t.me/py_basic/379""")  # 29

    await message.reply("""https://t.me/py_basic/389""")  # 30

    await message.reply("""https://t.me/py_basic/395""")  # 31

    await message.reply("""https://t.me/py_basic/452""")  # 32

    await message.reply("""https://t.me/py_basic/470""")  # 33

    await message.reply("""https://t.me/py_basic/481""")  # 34

    await message.reply("""https://t.me/py_basic/516""")  # 35

    await message.reply("""https://t.me/py_basic/523""")  # 36

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("""python.exe -m pip install --upgrade pip' command.
""")

@dp.message_handler(commands=['vid'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
#