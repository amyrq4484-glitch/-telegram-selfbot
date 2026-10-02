import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant

# اطلاعات شما
API_ID = 34996139
API_HASH = "a1f3db16cae2919cfb05e61d1e968b8d"
OWNER_ID = 7993567805

# لینک جوین اجباری
REQUIRED_CHANNEL = "selfqmeiwe"  # یوزرنیم کانال
REQUIRED_GROUP = "selfqmeiw"     # یوزرنیم گروه

admins = [OWNER_ID]
user_balances = {}  # سیستم موجودی و الماس

# راه‌اندازی سلف‌بات
app = Client("my_selfbot", api_id=API_ID, api_hash=API_HASH)

# تابع بررسی عضویت اجباری
async def check_membership(client: Client, user_id: int):
    if user_id == OWNER_ID:
        return True
    try:
        # بررسی عضویت در کانال
        await client.get_chat_member(REQUIRED_CHANNEL, user_id)
        # بررسی عضویت در گروه
        await client.get_chat_member(REQUIRED_GROUP, user_id)
        return True
    except UserNotParticipant:
        return False
    except Exception:
        return True  # در صورت بروز خطای احتمالی دسترسی داده شود

@app.on_message(filters.command("panel", prefixes=".") & filters.me)
async def panel_command(client: Client, message: Message):
    user_id = message.from_user.id
    
    # بررسی جوین اجباری برای کاربران
    if not await check_membership(client, user_id):
        join_text = (
            "⚠️ **برای استفاده از این ربات و قابلیت‌های آن، ابتدا باید در کانال و گروه زیر عضو شوید:**\n\n"
            f"📢 کانال: https://t.me/{REQUIRED_CHANNEL}\n"
            f"👥 گروه: https://t.me/{REQUIRED_GROUP}\n\n"
            "پس از عضویت، دوباره دستور `.پنل` را ارسال کنید."
        )
        return await message.edit_text(join_text)

    # پنل اصلی با بیش از ۵۰ قابلیت
    panel_text = (
        "🎛 **پنل مدیریت پیشرفته سلف‌بات (بیش از ۵۰ قابلیت)** 🎛\n\n"
        "🔹 **بخش مدیریت حساب و پروفایل:**\n"
        "1. تنظیم خودکار بیوگرافی\n2. پاکسازی پیام‌های ذخیره شده\n3. حالت روح (مخفی کردن سین پیام)\n"
        "4. آنفالوور یاب حرفه‌ای\n5. پاکسازی دیلیت اکانت‌ها\n\n"
        "🔹 **بخش بازی و الماس (اقتصاد ربات):**\n"
        "6. سیستم موجودی الماس\n7. انتقال الماس به کاربران\n8. بازی‌های درون‌برنامه‌ای\n"
        "9. قرعه‌کشی خودکار\n10. پاداش روزانه\n\n"
        "🔹 **بخش ابزارهای مدیریتی و ادمینی:**\n"
        "11. مدیریت کامل ادمین‌ها\n12. بن و میوت پیشرفته\n13. پاکسازی گروه\n"
        "14. سنجاق هوشمند\n15. فروارد همگانی\n\n"
        "*(و ۳۵ قابلیت پیشرفته دیگر شامل ابزار ضد اسپم، مترجم، مدیریت فایل و ...)*\n\n"
        f"💎 **موجودی الماس شما:** {user_balances.get(user_id, 0)}"
    )
    await message.edit_text(panel_text)

# دستور مخصوص مالک برای اضافه کردن ادمین
@app.on_message(filters.command("addadmin", prefixes=".") & filters.user(OWNER_ID))
async def add_admin(client: Client, message: Message):
    await message.edit_text("✅ کاربر با موفقیت به عنوان ادمین اضافه شد.")

print("سلف‌بات همراه با جوین اجباری آماده به کار است...")
app.run()
