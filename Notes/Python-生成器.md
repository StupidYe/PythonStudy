### Python-生成器

---

​	前面已经学习过迭代器了，也知道生成器本质上也是一个迭代器，生成器是用来创建Python序列的一个对象，可以迭代很大的队列，但不需要在内存中存储这整个序列，而是通过迭代来生成数据的，所以这就要介绍下生成器的几个特点了：

- 不会直接生成保存在内存，通过迭代，需要的时候才生成。(通过推算出来)
- 只保留当前位置
- 通过next()向后迭代

#### 生成器

----

要创建一个生成器有很多种方法，最简单的就是推导式了，比如：

```python
# 使用生成器推导式 创建一个生成器
g = (x+x for x in range(1,5))

print(type(g)) # <class 'generator'>
# 通过next()获取下一个值
print(next(g)) # 输出 2
print(next(g)) # 输出 4
print(next(g)) # 输出 6
print(next(g)) # 输出 8

# 再调用next(g),已经没有更多的元素时
print(next(g)) 	# 报错
'''
Traceback (most recent call last):
  File "test3.py", line 105, in <module>
    print(next(g))
StopIteration
'''
```

当到了没有更多元素的时候，Python会抛出一个StopIteration错误，严格来说这个也不算错误，只是获取不到更多的数据了，我们只需要去捕获这个错误进行处理就可以了。

当然，一般我们不会傻傻的一直用next()去获取值，那也太可怕了，万一数据有一百万个呢。通常情况下正确的方式是使用**for循环** ,因为生成器也是可迭代对象，而且使用for我们不需要去管StopIteration

```python
g = (x+x for x in range(1,5))

for i in g:
    print(i)
```

#### 生成器函数 

----

​	如果推导的算法太过复杂了，用生成器推导式的for循环比较难实现，我们可以用生成器函数来实现，我们知道普通函数都是用return来返回需要的值，python中的函数也一样，但是在python中还有一种函数不是用return来返回值的，而是用**yield** ，这种函数就叫生成器函数。生成器函数在调用的时候返回的是一个生成器对象，该对象可以被迭代。

比如著名的斐波拉契数列：除了第一个和第二个数外，其他的都是由前面两个数相加所得

1,1,2,3,5,8,13....

```python
def fib(count): #count是个数，整个数列的个数
    n = 0
    a = 0
    b = 1
    while n < count:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'OK'
x = fib(10)
print(type(x))  # <class 'generator'>
for i in x:
    print(i)
```

> 注意上面的赋值语句：
>
> a,b = b,a+b
>
> 这里不是a=b,b=a+b的赋值的意思
>
> 而是：右值部分为一个元组假设为x=(b,a+b),x[0] = b = 1,x[1] = a+b = 0+1 = 1
>
> 然后左边部分则对应起来，a = x[1],b = x[1],所以 a = b = 1,b = a+b = 0+1 = 1

- 关于return和yield：

​	普通函数是顺序运行的，直到程序运行完或者遇到了return才返回，而yield则不是，yield是遇到了就返回，下次从上次返回的位置继续执行。

- 关于next()和send(msg):

  next()和send()在一定意义上是意义的，区别就是send是可以传递yield表达式的值进去，而next不能传递值

  ```python
  def test():
      print "Hello"
      a = yield 1
      print a
      b = yield 2
      print "Hi"
   
  g = test()
  g.__next__() # 相当于执行了c.send(None)  
  g.send("abc")	# 输出 abc
  ```

  > 注意：
  >
  > **第一次调用生成器的时候，需要使用\_\_next()\_\_或者send(None),不可以直接使用send发送一个非None的值，因为在第一次的时候遇到yield就已经返回了，并没有yield来接收这个值** ，

