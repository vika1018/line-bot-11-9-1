#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('hmDdVp5SnY9VouuOj0x72AsaMqbTed27zRlnvL6shzvf+CZElkGgG8uwcNpuqfwk2zBfBPruIbJXy/NLopDInm3ULnWQxjtrtlcdfnFEuwDnl6v2ByeJLSh3U5rpuDimHIRZKZl5f6kgYH7Tf4I6FgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('7e2526361af1800f787f38d7de4ab065')

line_bot_api.push_message('U535ea272631c1d15ea420c3f1db6332c', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('心花開',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('主人我在,請問什麼事嗎?'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
def handle_message(event):
    message = text=event.message.text
    if re.match('你是男是女',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('主人想要我是男的,我就男的,而且可以當主人的暖男!主人要是想要我是女的,我就是女的,而且可以當主人的小甜心唷~'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))           
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)