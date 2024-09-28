from modules.util.telegram_methods import make_request


class TelegramCommand:
    def __init__(self):
        self.url_command = self.get_url_command()

    def get_url_command(self) -> str:
        raise NotImplementedError

    def run(self):
        make_request(self.url_command)
