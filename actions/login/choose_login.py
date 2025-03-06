from actions.login.use_phone import use_phone
from configs.config import config


def choose_login():
    if config.login_type.lower() == "phone":
        use_phone()



