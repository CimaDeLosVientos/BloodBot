import urllib

from modules.util.telegram_command import TelegramCommand
from modules.util.telegram_methods import make_request


class SendMessageCommand(TelegramCommand):
    def __init__(self, text: str, chat_id: str, reply_markup=None):
        self.text = text
        self.chat_id = chat_id
        self.reply_markup = reply_markup
        TelegramCommand.__init__(self)

    def get_url_command(self) -> str:
        """
        Sends a message to a single chat.

        :param      text:          The message text
        :type       text:          String
        :param      chat_id:       The chat identifier
        :type       chat_id:       Integer
        :param      reply_markup:  The reply markup, like a keyboard
        :type       reply_markup:  ReplyMarkup. https://core.telegram.org/type/ReplyMarkup
        """
        text = urllib.parse.quote_plus(self.text)  # https://docs.python.org/3/library/urllib.parse.html
        url = "sendMessage?text={}&chat_id={}&parse_mode=html".format(text, self.chat_id)
        if self.reply_markup:
            url += "&reply_markup={}".format(self.reply_markup)
        return url
