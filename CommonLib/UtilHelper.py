import random
import string
import datetime


class UtilHelper:

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def get_current_time_stamp():
        now = datetime.now()
        return datetime.timestamp(now)

    @staticmethod
    def get_base_header():
        base_header = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive'
        }
        return base_header
