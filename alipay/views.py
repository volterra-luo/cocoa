# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from util import AlipaySubmit
from config import AlipayConfig

import urllib2, logging, collections

# 目标服务地址
target_service = 'user.auth.quick.login'

# 必填，页面跳转同步通知页面路径
return_url = 'http://127.0.0.1:8000/alipay/return_url'

# 防钓鱼时间戳
anti_phishing_key = ''
# 若要使用请调用类文件submit中的query_timestamp函数

# 客户端的IP地址
exter_invoke_ip = ''
# 非局域网的外网IP地址，如：221.0.0.1

# 把请求参数打包成数组
sParaTemp = {'service':'alipay.auth.authorize'}
sParaTemp['partner'] = AlipayConfig.partner
sParaTemp['_input_charset'] = AlipayConfig.input_charset
sParaTemp['target_service'] = target_service
sParaTemp['return_url'] = return_url
sParaTemp['anti_phishing_key'] = anti_phishing_key
sParaTemp['exter_invoke_ip'] = exter_invoke_ip


def _encode_params(**kw):
	'''
    	do url-encode parameters
    	>>> _encode_params(a=1, b='R&D')
    	'a=1&b=R%26D'
    	>>> _encode_params(a=u'\u4e2d\u6587', b=['A', 'B', 123])
    	'a=%E4%B8%AD%E6%96%87&b=A&b=B&b=123'
    '''
    args = []
    for k, v in kw.iteritems():
        if isinstance(v, basestring):
            qv = v.encode('utf-8') if isinstance(v, unicode) else v
            args.append('%s=%s' % (k, urllib.quote(qv)))
        elif isinstance(v, collections.Iterable):
            for i in v:
                qv = i.encode('utf-8') if isinstance(i, unicode) else str(i)
                args.append('%s=%s' % (k, urllib.quote(qv)))
        else:
            qv = str(v)
            args.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(args)


def index(request):
	if request.method == 'POST':
		# 建立请求
		http_url = '%s_input_charset=%s' % (AlipaySubmit.ALIPAY_GATEWAY_NEW, AlipayConfig.input_charset)
		http_body = None
		sPara = AlipaySubmit.buildRequestPara(sParaTemp)
        params = _encode_params(sPara)
		req = urllib2.Request(http_url, data=http_body)
	return render(request, 'alipay/index.html', {})
