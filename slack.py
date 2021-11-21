import requests
from easydict import EasyDict
from util import load_config

class SlackMessage:

    def __init__(self):

        config_info = EasyDict(load_config())
        self.stock_channel_name = config_info.stock_slack_channel_name
        self.stock_bot_token = config_info.stock_slack_bot_token
 
    def post_message(self, text):

        requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer " + self.stock_bot_token},
            data={"channel": self.stock_channel_name, "text": text}
        )
