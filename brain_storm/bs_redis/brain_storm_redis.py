'''
微信头脑王者辅助(全自动)

mitmproxy -p 手机代理端口 -s brain_storm.py
'''

from mitmproxy import ctx
import json
import requests
from urllib.parse import quote
import string
from redis import Redis
from rq import Queue
import time
from job import auto_touch,next_cycle

# 消息队列，异步处理
q = Queue(connection=Redis())



def response(flow):
	'''
	捕获服务器reponse，抓取问题和选项，并处理
	'''
	path = flow.request.path 
	if path == "/question/bat/findQuiz":
		data = json.loads(flow.response.text)
		question = data["data"]["quiz"]
		options = data["data"]["options"]
		ctx.log.info("question: {},options: {}".format(question,options))
		options,ans_count = get_answer(question,options)
		data["data"]["options"] = options
		flow.response.text = json.dumps(data)
		job = q.enqueue(auto_touch,ans_count)
	# elif path == "/question/bat/fightResult":
	# 	q.enqueue(next_cycle)
		



def get_answer(question,options):
	'''
	搜寻答案
	'''
	url = quote("https://www.baidu.com/s?wd=" + question,safe=string.printable)
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
	r = requests.get(url,headers=headers)
	content = r.text

	answer = []
	ans_count = []
	for option in options:
		count = content.count(option)
		answer.append(option+"("+str(count)+")")
		ans_count.append(int(count))
	return answer,ans_count
