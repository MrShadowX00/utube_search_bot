from telegram.ext import *
import telegram 
from telegram import *
import ytubebot as res
import api_key as keys
import asyncio

bot = telegram.Bot(keys.API)

def start_command(update, context):
    update.message.reply_text('Type keys to search from YouTube')



def help_command(update,context):
    update.message.reply_text('Fast searching bot from YouTube. Hit start command to search!')



def result_from_search(update, context):
    response = res.ubot_result(update.message.text)
    for i in range(10):
        keyboard = [[InlineKeyboardButton("⬇️ video",callback_data=response[i]+"videofrombotmk",),InlineKeyboardButton("⬇️ mp3",callback_data=response[i])]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(response[i],reply_markup = reply_markup)



def button(update,CallbackQueryHandler):
    print(update.callback_query.data)
    update.callback_query.answer()
    if "videofrombotmk" in update.callback_query.data :
        link = update.callback_query.data.replace("videofrombotmk","")
        res.get_video_info(update.callback_query.data)
        bot.send_video(chat_id=str(update.callback_query.message.chat.id), video=open('out.mp4', 'rb'), supports_streaming=True)
    else:
        res.get_video_info(update.callback_query.data)
        bot.sendAudio(chat_id=str(update.callback_query.message.chat.id), audio =open('out.mp3', 'rb'))
        
    print("start sending")
   



def error(update, context):
    print(f"Update  caused error {context.error}")



def main():
    updater = Updater(keys.API,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    # updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text,result_from_search))
    dp.add_error_handler(error)
    dp.add_handler(CallbackQueryHandler(button))
    # dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

main()


