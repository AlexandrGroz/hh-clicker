from actions.login.check_auth import check_auth
from actions.login.choose_login import choose_login


def login():
    if check_auth():
        return
    else:
        choose_login()
