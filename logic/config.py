# -*- coding: utf-8 -*-

def get(key):
	return {
		'LOG_PATH' : '/tmp'
		'ADMIN_USERS' : []
		'ADMIN_CIDS' : []
		'SOMETHING' : ''
	}.get(key)