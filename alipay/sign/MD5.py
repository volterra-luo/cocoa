#! -*- coding: utf-8 -*-
import hashlib

class MD5(object):

	def  __init__(self, text='', key='', sign='',  input_charset='utf-8'):
		this.text = text
		this.key = key
		this.sign = sign
		this.input_charset = input_charset

	def  sign(self):
		m = hashlib.md5()
		raw_str = this.text + this.key
		tmp_str = unicode(raw_str, this.input_charset)
		m.update(tmp_str)
		return m.hexdigest()

	def verify(self):
		mysign = self.sign()
		
		if mysign == this.sign:
			return True
		
		return False