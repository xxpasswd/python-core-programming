程序结构
```
   -wxbot
      |--api 第三发api
      |    |--- __init__.py
      |    |--- tuling.py
      |    |--- resource.py
      |
      |-- wxbot 微信消息处理
      |    |--- __init__.py
      |    |--- bot.py 总的消息处理
      |    |--- get_content.py 获取内容的封装函数
      |
      |-- run.py 主程序
```


api/resource 里面的video数据库结构设计

url：视频地址
tags：视频标签
relate：相关联的视频
