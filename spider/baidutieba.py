import requests
import time
from bs4 import BeautifulSoup as b

'''
标题和标题链接
<a rel="noreferrer" href="/p/5513330904" title="刚整理的2018全新Python学习资料，直接进来拿走！" target="_blank" class="j_th_tit ">刚整理的2018全新Python学习资料，直接进来拿走！</a>
作者
<a rel="noreferrer" data-field="{&quot;un&quot;:&quot;wu4fo0&quot;}" class="frs-author-name j_user_card " href="/home/main/?un=wu4fo0&amp;ie=utf-8&amp;fr=frs" target="_blank">wu4fo0</a>
回复数量
<div class="col2_left j_threadlist_li_left">
    <span class="threadlist_rep_num center_text" title="回复">0</span>
</div>

'''

# 链接入口
URL = "http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="


def get_url_html(url):
    '''
    获取网页的html
    '''

    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return "ERROR"

def get_content(url):
    '''分析网页内容'''


    # 存储帖子信息的字典
    comments = []

    html = get_url_html(url)
    soup = b(html,'lxml')

    li_tags = soup.find_all('li',class_=" j_thread_list clearfix")
    for li in li_tags:
        # 初始化一个字典，存储文章信息
        comment = {}
        # 使用try，防止爬虫出错而停止运行
        try:
            # 获取网页内容
            comment['title'] = li.find('a',attrs={'class':'j_th_tit '}).text.strip()
            comment['link'] = URL + li.find('a',class_="j_th_tit ")['href']
            comment['author'] = li.find('span',attrs={'class':'frs-author-name-wrap'}).text.strip()
            comment['reply'] = li.find('div',attrs={'class':'col2_left j_threadlist_li_left'}).text.strip()
            comments.append(comment)
        except:
            print("get_content,error")
    return comments

def write2file(dict):
    '''
    将网页内容保存到本地
    '''

    with open('aa.html','a+') as f:
        f.write("<table>\n<tbody>\n")
        f.write("<tr><td>title</td><td>link</td><td>author</td><td>reply</td></tr>\n")
        for comment in dict:
            f.write("<tr>\n<td>{}</td> <td>{}</td> <td>{}</td> <td>{}</td>\n</tr>\n".format(\
            comment['title'],comment['link'],comment['author'],comment['reply']))
        f.write("</tbody>\n</table>")
        print("当前页面已爬取完bi",end='\t')

def main(url,deep):
    # 添加所有要爬取的url
    url_list = []
    for i in range(deep):
        url = URL+str(i*50)
        url_list.append(url)
    print('所有url添加完毕')

    # 开始爬取页面
    for i in url_list:
        contents = get_content(url)
        write2file(contents)
        print("{}".format(int(i[47:])/50))


if __name__ == '__main__':
    main(URL,3)