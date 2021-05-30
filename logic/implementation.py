# -*- coding: utf-8 -*-
import logic.config as cfg
from time import time

def is_admin(m):
	admin = cfg.get('ADMIN_USERS')
    cid = m.chat.id
    if cid > 0:
        if str(m.chat.username) in admin_username:
            return True
        else:
            return False
    else:
        if str(m.from_user.username) in admin_username:
            return True
        else:
            return False

def init_msg(bot, admin_cid, msg='Bot started'):
    for cid in admin_cid:
    	time.sleep(1)
        bot.send_message(cid, msg)