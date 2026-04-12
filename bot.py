import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# ========== НАСТРОЙКИ (ЗАМЕНИ ЭТИ ДВЕ СТРОКИ) ==========
BOT_TOKEN = "8681289057:AAHw_jtLDwZUr2cpTnFDxObcSA1G8PySz7Y"
GAME_URL = "https://enejrj.github.io/asfasf/"

# ========== ОСТАЛЬНОЕ НЕ ТРОГАЙ ==========
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 ИГРАТЬ 💎", web_app=WebAppInfo(url=GAME_URL))],
        [InlineKeyboardButton(text="👥 Топ донатеров", callback_data="top")],
        [InlineKeyboardButton(text="📋 Реферальная ссылка", callback_data="referral")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")]
    ])
    await message.answer(
        f"🔥 <b>NO LIFE, JUST TAP</b> 🔥\n\n"
        f"Тапай по кристаллу, пока не сотрёшь палец.\n"
        f"Секретарша Лилу будет хвалить тебя.\n"
        f"🏆 Цель: 30 миллиардов = 200 TON (~140,000₽)\n\n"
        f"👇 Нажми на кнопку, чтобы начать!",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

@dp.message(Command("top"))
async def top(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 ИГРАТЬ", web_app=WebAppInfo(url=GAME_URL))]
    ])
    await message.answer(
        "🏆 <b>ТОП ДОНАТЕРОВ</b> 🏆\n\n1. @player1 — 50 TON\n2. @player2 — 30 TON\n3. @player3 — 20 TON\n\n👉 Зайди в игру, чтобы попасть в топ!",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

@dp.message(Command("referral"))
async def referral(message: types.Message):
    user_id = message.from_user.id
    bot_username = (await bot.get_me()).username
    ref_link = f"https://t.me/{bot_username}?start=ref_{user_id}"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 ИГРАТЬ", web_app=WebAppInfo(url=GAME_URL))],
        [InlineKeyboardButton(text="📤 ПОДЕЛИТЬСЯ", url=f"https://t.me/share/url?url={ref_link}&text=Тапай со мной в NO LIFE, JUST TAP!")]
    ])
    await message.answer(
        f"👥 <b>ТВОЯ РЕФЕРАЛЬНАЯ ССЫЛКА</b>\n\n📋 <code>{ref_link}</code>\n\n💡 За каждого друга ты получишь 500💎 и Колбу x2!",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "❓ <b>ПОМОЩЬ</b>\n\n💎 Тапай по кристаллу → получай алмазы.\n🔋 Энергия восстанавливается каждые 15 секунд.\n⚡ Бусты: сила тапа, энергия, автокликер, крит x3.\n👥 Приглашай друзей → получай бонусы.\n💰 Донаты за TON → эксклюзивные бусты.\n🏆 30 миллиардов алмазов → 200 TON (~140,000₽)!",
        parse_mode="HTML"
    )

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    if callback.data == "top":
        await top(callback.message)
    elif callback.data == "referral":
        await referral(callback.message)
    elif callback.data == "help":
        await help_cmd(callback.message)
    await callback.answer()

async def main():
    print("🚀 Бот NO LIFE, JUST TAP запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())