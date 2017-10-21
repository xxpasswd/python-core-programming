#coding=utf-8

class LNode(object):
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

class LlistError(ValueError):
    pass

#单链表，只含有头指针
class Llist(object):
    """
    前插入：O(1)
    后插入：O(n)
    前推出：O(1)
    后推出：O(n)
    中间插入和推出：O(n)
    """
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self,elem=1):
        self._head = LNode(elem,self._head)

    def pop(self):
        if self._head is None:
            raise LlistError("in pop")
        e = self._head.elem
        self._head=self._head.next
        return e

    def append(self,elem=2):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LlistError("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self,elem):
        p = self._head
        while p is not None:
            if p.elem==elem:
                return p
            p = p.next

        else:
            raise LlistError("in Llist1 find")

    def delete(self,elem):
        if self._head is None:
            raise LlistError("in Llist1 delete")
        p = self._head
        if p.elem == elem:
            self._head = self._head.next
        else:
            while p is not None:
                if p.next.elem == elem:
                    p.next = p.next.next

    def rev(self):
        p = None
        while self._head:
            # q 是 self._head 的值传递，若修改q的属性，则为应用传递
            q = self._head
            self._head = self._head.next
            q.next = p
            p = q
        self._head = p

    def sort(self):
        if self._head is None:
            return
        son = self._head.next
        while son is not None:
            x = son.elem
            p = self._head
            while p is not son and p.elem <= x:
                p = p.next
            while p is not son:
                y = p.elem
                p.elem = x
                x = y # 把这一节点的值保存下来，赋给下一节点
                p = p.next
            son.elem = x
            son = son.next

    def sort2(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None # self._head.next=None
        while rem is not None:
            p = self._head
            q = None   # rem之前的元素
            while p is not None and p.elem<=rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            x = rem
            rem = rem.next
            x.next = p


    def printall(self):
        p = self._head
        while p is not None:
            print p.elem
            p=p.next

#含有尾指针
class Llist2(Llist):
    """
        前插入：O(1)
        后插入：O(1)
        前推出：O(1)
        后推出：O(n)
        中间插入和推出：O(n)
    """
    def __init__(self):
        super(Llist2,self).__init__()
        self._rear = None

    def prepend(self,elem=1):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem,self._head)

    def pop_last(self):
        if self._head is None:
            raise LlistError("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.elem
        p.next = None
        self._rear = p
        return e

    def append(self,elem=2):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

#循环链表
class LClist(object):
    """
    前插入：O(1)
    后插入：O(1)
    前推出：O(1)
    后推出：O(n)
    中间插入和推出：O(n)
    """
    def __init__(self):
        self._rear = None

    def prepend(self,elem=1):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def pop(self):
        if self._rear is None:
            raise LlistError("in LClist pop")
        p = self._rear
        if p.next == p:
            e = p.elem
            self._rear=None
            return e
        else:
            e = p.next.elem
            p.next = p.next.next
            return e

    def append(self,elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
            self._rear = p

    def pop_last(self):
        if self._rear is None:
            raise LlistError("in LClsit pop_last")
        p = self._rear
        if p.next==p:
            e = p.elem
            self._rear = None
            return e
        else:
            e = p.next.elem
            while p.next!= self._rear:
                p = p.next
            p.next = self._rear.next
            self._rear = p
            return e

    def printall(self):
        if self._rear is not None:
            p = self._rear.next
        else:
            return

        while True:
            print p.elem
            if p is self._rear:
                break
            p = p.next




# 测试部分
def fun(Llist):
    print "Creat an empty linked list and dispaly it's elements"
    mylist = Llist()
    mylist.printall()

    print "add 5 elements to list"
    for i in range(5):
        mylist.append(i)
    mylist.printall()

    print "pop first elements"
    mylist.pop()
    mylist.printall()

    print "pop last elements"
    mylist.pop_last()
    mylist.printall()

    print "add an elements on first place"
    mylist.prepend(9)
    mylist.printall()

    return mylist
# print "find 3"
# print mylist.find(9)
# mylist.delete(9)
# mylist.printall()

#
# for i in (Llist,Llist2,LClist):
#     fun(i)

aa = fun(Llist)
aa.rev()
print
aa.printall()
print
aa.sort2()
aa.printall()