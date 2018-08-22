## python cookbook的一些总结

### 第一章

1. 解压序列赋值给多个变量
2. 查找最大或最小的n个元素，使用heapq模块的nlargest()和nsmallest()函数
3. 字典中键映射多个值，可以使用collections模块中的defaultdict解决
4. 字典排序，zip函数交换键和值的顺序后进行处理
5. 查找两个字典的相同点，通过集合运算
6. 切片命名，代码意义更加清晰
7. 找出一个序列中出现次数最多的元素，使用collections模块的Counter
8. 通过某个关键字排序一个字典列表，sort函数中，key使用operator的itemgetter函数传值，也可以使用lambda表达式