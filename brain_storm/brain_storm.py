'''
微信头脑王者辅助

mitmproxy -p 手机代理端口 -s brain_storm.py
'''

from mitmproxy import ctx
import json
import requests
from urllib.parse import quote
import string

def response(flow):
	path = flow.request.path 
	if path == "/question/bat/findQuiz":
		data = json.loads(flow.response.text)
		question = data["data"]["quiz"]
		options = data["data"]["options"]
		ctx.log.info("question: {},options: {}".format(question,options))
		options = get_answer(question,options)
		data["data"]["options"] = options
		flow.response.text = json.dumps(data)


def get_answer(question,options):
	url = quote("https://www.baidu.com/s?wd=" + question,safe=string.printable)
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
	r = requests.get(url,headers=headers)
	content = r.text

	answer = []
	for option in options:
		count = content.count(option)
		answer.append(option+"("+str(count)+")")

	return answer