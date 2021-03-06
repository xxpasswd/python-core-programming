## python cookbook的一些总结

### 第一章 数据结构和算法

1. 解压序列赋值给多个变量
2. 查找最大或最小的n个元素，使用heapq模块的nlargest()和nsmallest()函数
3. 字典中键映射多个值，可以使用collections模块中的defaultdict解决
4. 字典排序，zip函数交换键和值的顺序后进行处理
5. 查找两个字典的相同点，通过集合运算
6. 切片命名，代码意义更加清晰
7. 找出一个序列中出现次数最多的元素，使用collections模块的Counter
8. 通过某个关键字排序一个字典列表，sort函数中，key使用operator的itemgetter函数传值，也可以使用lambda表达式
9. 根据关键字排序列表对象，sort函数中，key使用operator的attrgetter函数传值，也可以使用lambda表达式
10. 过滤列表元素使用列表推导式或者filter函数
11. 提取字典的子集，使用字典推导式
12. 命名元祖，提高代码的可读性 使用collections里的nametuple

### 第二章 字符串和文本

1. 使用多个界定符分割字符串，使用re模块的split函数
2. 检查字符串开头和结尾的字符，使用startwith和endwith
3. 字符串匹配和搜索，对于简单的字符串，使用字符串的startwith，endwith和find函数，复杂的字符串可以使用re模块的match，search，findall和finditer函数
4. 字符串的搜索和替换，简单的使用字符串的replace函数，复杂的使用re模块的sub函数
5. 贪婪匹配和非贪婪匹配，使用？来尽可能短的匹配
6. 多行匹配模式，使用(?:)非捕获分组来进行匹配，或者使用flag（re.DOTALL）
7. 删除字符串中不需要的字符，使用strip，replace和re模块的sub函数
8. 对齐字符串使用ljust，rjust，center，format函数
9. 字符串拼接，使用join和+
10. 以指定列宽格式化字符串，使用textwrap的fill函数
11. 字符串令牌解析，使用scanner函数

### 第三章 数字与日期

1. 数字的四舍五入，使用round函数
2. 浮点数的精确运算使用decimal模块的Decimal类
3. 数字的格式化输出，使用format函数
4. 数字间的进制转换，bin，oct，hex，或者format(5,'b'),format(5,'o'),format(5,'x'),转换为10进制int(5,2)
5. 随机选择，random模块的choice，randint
6. 时间计算模块datatime模块

## 第四章 迭代器和生成器

1. 如何手动迭代？
2. 如何让创建的对象能够实现迭代？
3. 如何通过函数的方式定制迭代器？
4. 如何反向迭代和对对象实现反向迭代？
5. 如何对可迭代对象进行切片？
6. 如何进行排列组合？
7. 如何知道迭代对象的索引值？
8. 如何同时迭代多个迭代对象？
9. 如何让多个序列连续迭代？
10. 序列迭代停止，可以给iter传入截止的参数

## 第五章 文件与IO

1. 如何读取一个文件？打开方式的区别？
2. 如何将print的内容定向到文件中？
3. 如何判断当文件不存在时，才可以写入？
4. 如何创建一个类文件对象？
5. 如何迭代固定大小的文件内容？
5. 路径文件名操作，os.path.basename,os.path.dirname,os.path.join
6. 测试文件是否存在，os.path.exists,os.path.isfile,os.path.isdir
7. 使用临时文件from tempfile import *

## 第六章 数据编码和文件处理

1. 读写json数据使用，将字符串转为json，json.loads()，反之，json.dumps()，输出漂亮化，print(json_data,indent=4)，或者from pprint import pprint
2. 解析xml数据和base64数据

## 第七章 函数

1. *args接受任意数量的位置参数， **kwargs接受任意数量的关键字参数， *出现在最后一个参数后面， **出现在 *后面
2. 函数的强制参数，比如 recv(maxsize,*,block=None)
3. 不要这样做fun(a,b=[]),正确的做法fun(a,b=None)
```
def fun(a,b=None):
    # if not b是错误的，有可能b是'',False
    if b is None:
        b = []
```
4. 匿名函数lambda，其中的变量值x是调用的时候获取的，不是定义的时候获取的
```
a = lambda y: x+y
x = 10
a(10) # 结果 20
x = 20
a(10) # 结果 30
```
4. 减少函数参数的个数，使用functiontools的partial函数
5. 想使用额外的环境变量时，可以使用闭包的方法来解决
6. 回调函数，感觉很有趣，后面可以仔细看一下

### 第九章 元编程
1. 给函数添加装饰器，并保留函数的元信息
2. 解除装饰器 fun.__wrappped__ 访问原函数
3. 带参数的装饰器（可以理解为一个产生装饰器的装饰器）
4. 带可选参数的装饰器（要理解装饰器的调用原理，传进来的参数）
5. 类中定义装饰器，可以很方便的保存额外的信息状态
6. 使用装饰器，给被包装的函数增加额外的参数
7. 使用装饰器扩充类的功能

### 第十二章 并发编程
1. 启动和停止线程，1通过给Thread的传值。2继承Thread类
2. 线程间通信，使用threading.Condition, Queue，**使用消息队列的方式可以看一看书，线程通信类似与分布式通信**
3. 线程同步，使用加锁解锁
4. 本地线程存储对象threading.local
5. 使用线程池，控制线程数量
6. 使用进程池，利用多核CPU的优势
7. actor发送任务，让程序处理（AMQP，ZMQ）
8. 发布/订阅者（交换机）

