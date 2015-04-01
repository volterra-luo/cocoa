# -*- coding: utf-8 -*-
import AlipayCore

# 支付宝消息验证地址
HTTPS_VERIFY_URL = 'https://mapi.alipay.com/gateway.do?service=notify_verify&'

'''
	验证消息是否是支付宝发出的合法消息
	param params 通知返回来的参数数组({})
    return 验证结果
'''

def verify(params):

	# 判断responsetTxt是否为true，isSign是否为true
	# responsetTxt的结果不是true，与服务器设置问题、合作身份者ID、notify_id一分钟失效有关
	# isSign不是true，与安全校验码、请求时的参数格式（如：带自定义参数等）、编码格式有关
	responseTxt = 'true'

	if params.get('notify_id') != None:
		notify_id = params.get('notify_id')
		responseTxt = verifyResponse(notify_id)

	sign = ''
	if params.get('sign') != None:
		sign = params.get('sign')
		isSign = getSignVeryfy(params, sign)

	# 写日志记录（若要调试，请取消下面两行注释）
	# sWord = u'responseTxt=%s\nisSign=%s\n返回回来的参数：%s' % (responseTxt, isSign, AlipayCore.createLinkString(params))
	# AlipayCore.logResult(sWord)

	if isSign and responseTxt == 'true':
		return True

	return False
