### Python-函数

​	函数是一种可以复用代码，把大型代码拆分成多段代码，实现功能分离，达到模块化的效果。

​	对于函数主要有两个操作：**定义函数和调用函数** 

#### 函数定义 

----

​	使用关键字**def** ,函数名，圆括号，圆括号内可以有参数，最后再跟一个冒号:。函数的命名和变量的命名一样。

​	回顾下变量命名的规范：只能用字母或者下划线开头，名字中只能包含字母，数字和下划线。

​	定义一个函数可以这样子：

```python 
# def 函数名 (参数)：
# 	执行语句
#	return 返回值

# 定义一个不执行任何语句的函数(无参数，无返回值)
def main():
  pass

# 定义一个无参数，有返回值的函数
def main1():
  return True

# 定义一个有参数，有返回值的函数
def main2(name):
  print("My name is %s" %name)
```

> 注意：
>
> 1.函数的返回值，如果没有用return指定返回值，默认是返回**None** 。None作为布尔值的时候和False一样，但是两者是有区别的。Python中不含任何值得空数据结构都等价于False，但不等于None，可以用is操作符判断: if xxx is None 

#### 函数调用

---

​	函数的调用很简单，只需要在函数名字后面加上(),就是调用函数了，当然有参数的要给予参数。比如上面定义了函数后，要调用，只需要这样：`main() main1() main2("West")` 

​	注意只使用了函数名，不带()的不是调用，返回的是函数对象，函数也是对象的一种，函数名也可以当做变量一样赋值给另一个，比如：`test = main  test()` 就等价于调用了函数main

#### 函数参数

---

​	函数参数有几种类型：位置参数，关键字参数，默认参数，可变参数。

- 位置参数

  传入的参数是按照位置顺序依次传递的。(坏处是需要记住每个位置的参数的意义，容易记混而出错)

  ```python 
  # 定义一个函数sum，计算x和y的和
  # x和y称为参数，具体的说是形参
  def sum(x,y):
    return x+y
  # 调用的时候，依次传递参数给x和y
  sum(3,4)
  # 可以把返回值赋值给一个变量
  data = sum(3,4) #依次把3复制给x，4复制给y
  print(data)  #data = 7
  ```

- 关键字参数

  关键字参数可以在调用的时候指定参数的名字，这样就避免了位置参数所带来的坏处了。

  关键字参数也可以不按顺序的调用，**也可以和位置参数混合调用，但是位置参数必须要在关键字参数的前面调用**

  ```python
  # 定义函数
  def sum(x,y):
    return x+y

  # 使用关键字参数调用函数
  print(sum(x=2,y=4))

  # 不按顺序的关键字参数调用
  print(sum(y=3,x=2))

  # 和位置参数混合使用
  print(sum(1,y=7))
  # 这种方式是不对的
  # print(sum(x=1,7)) 位置参数在关键参数后面了。
  ```

- 默认参数

  函数定义时候指定的默认参数，在调用时候，如果没有提供对应的参数，则用默认参数替代，否则就用提供的参数。

  注意：**默认参数必须在位置参数之后** 

  ```python
  # 定义函数
  def sum(x=4,y=5): 
    return x+y
  # def sum(x=4,y): 这种是不行的，默认参数必须在位置参数之后
  # 试想下这种定义函数，调用时候 sum(3),那这个3是给默认参数呢，还是给位置参数的，分不清了。

  # 两个参数都提供
  print(sum())	#输出： 9

  # 提供一个参数，默认是给第一个参数
  print(sum(3)) 	#输出： 8

  # 提供一个参数，在赋值时候指定
  print(sum(y=2)) #输出： 6

  # 提供两个参数
  print(sum(2,3)) #输出： 5
  ```

  > 默认参数需要注意的一点是：默认参数的值在函数定义的时候就已经计算出来了，而不是函数运行时候生成，当参数值为可变的数据类型时候，很容易犯错（涉及到传值还是传引用的问题，下面会讲)，比如：
  >
  > def main(a,b=[]):  # b为空列表，列表为可变的数据类型
  >
  > ​	b.append(a)
  >
  > ​	print(b)
  >
  > main(1)  # 执行第一次，输出为：[1]
  >
  > main(2) # 第二次执行，输出为：[1,2],而不是[2]
  >
  > 要想列表每次只输出一个，可以在函数定义的时候对b是否为None做个判断，如下：
  >
  > def main(a,b=None):
  >
  > ​	if b is None:
  >
  > ​		b = []
  >
  > ​	b.append(a)
  >
  > ​	print(b)
  >
  > 最终输出为[1]和[2]

- 可变参数

  可变参数的意思就是，提供给函数的参数是不确定的，可能是一个，也可以是多个，也可以没有参数，有两种可变参数，分别是*args和**kwargs。

  - *args

    会把传入的多的参数作为一个**元组** （前面是星号，后面的变量名可以自定义）,收集的是位置参数。

    ```python 
    # 比如计算 a²+b²+c²...
    def calc(*number):
        sum = 0
        for i in number:
            sum = sum + i * i
        return sum
    # 调用方式 也可以不给参数，直接calc(),结果当然是0
    print(calc())
    # 元组(1,2,3,4)的形式
    print(calc(1,2,3,4))
    # 如果已经存在一个元组,可以这样传递参数
    data = (1,2,3)
    print(calc(data[0],data[1],data[2])) #比较繁琐
    # 可以直接这样，加个星号
    print(calc(*data))
    ```

  - **kwargs

    会把传入的多的参数作为一个**字典** （前面两个是星号，后面的变量名可以自定义），收集的是关键字参数。

    ```python
    def people(name,age,**kwargs):
    	print("name:",name)
    	print("age:",age)
    	print("other:",kwargs)
    # 可以传入0个或任意个参数，除了接受name和age参数外，还接受任意个参数kwargs(关键字参数)

    # 可以不传入关键字参数
    people("ZZY",22)
    # 也可以传入关键字参数
    people("zzy",22,city="ShenZhen")
    # 可以把dict作为参数传进去
    kw = {'city':'shanghai','job':'Coder'}
    people("zzy",22,**kw)
    ```


#### 函数参数传递

---

​	前面说到，在默认参数是可变数据类型时容易犯错，这里涉及到Python函数参数的传递问题，这里先给出结论：**Python函数参数传递，既不是传值，也不是传引用**。

​	首先要清楚知道的是，在python中，**一切都是对象**，python的变量是没有类型的，只有对象才有类型，变量是可以指向任何的对象的，可以指向列表，元组，函数，变量也可以看做是对象的一种引用(也可以看成是一个标签，贴在对象上)。

进一步理解：

```python
# 变量a 相当于是给一个有三个元素的列表贴上标签a
a = [1,2,3]
print(type(a))
print(id(a))
# 把标签a贴到元组上
a = (4,5,6)
print(type(a))
print(id(a))
# 输出：
# <class 'list'>
# 140094689003912
# <class 'tuple'>
# 140094689336776
```

从上面的程序可以看出：变量a是没有类型的，它既可以执行列表，也可以指向元组。

再到函数的传参上，其实就是**变量指向的对象的内存地址的传递（可以理解为传递的是对象）** ，这里就牵扯到python中可变对象和不可变对象的概念了：

可变对象：字典，列表，集合...

不可变对象：整形，字符串，元组...

正是由于存在可变对象和不可变对象，python函数的参数传递看起来有时候是传值，有时候是传引用，可以这样子去理解(仅仅限于理解)

**参数是可变对象的传递，类似于c/c++中的引用传递**

**参数是不可变对象的传递，类似于c/c++中的值传递** 

举例说明：

```python
# 不可变对象
def show(data):
    data = 10
    print(data)
# 变量a，指向内存中保存5的内存地址
a = 5
show(a)		# 输出10 
print(a)	# 输出5
'''
解释：
首先a = 5,相当于给内存中的5贴上一个标签a
然后调用show(a)，将data = a，等于给内存中的5再贴一个标签 data
接着执行data = 10,等于把5的标签data撕掉，贴到了10上面
所以这时候，a还是指向了5，而data已经指向了10，所以print(data) = 10,print(a) = 5,类似是传值。
'''
```

```python
# 可变对象 还是这个列子
def add(data,b=[]):
    b.append(data)
    print(b)
add(1)	# 输出 [1]
add(2)  # 输出 [1,2]
'''
解释：
首先调用了add(1),默认参数为一个空列表b，第一次调用b.append(data)，因为列表是可变的，所以在列表内存中添加一个1，第二调用add(1),默认参数还是b，默认参数在函数定义的时候就生成，b指向的还是列表的内存地址，这时候的列表中已经有了一个元素1，再执行b.append(data)，就变成了[1,2]了。
'''
```

网上看到的个人觉得讲的比较好的，也参考学习过的博客：

[Python 函数中，参数是传值，还是传引用？](https://foofish.net/python-function-args.html)

#### 内部函数

​	内部函数，我觉得也是嵌套函数，也就是在函数内部定义的函数。当一个函数内部需要多次执行比较复杂的任务的时候，内部函数作用还是很大的，可以避免代码的堆叠

```python
def out(a,b):
  def _in(c,d):
    return c+d
  return _in(a,b)
print(out(3,2)) # 输出 5
```

#### 闭包

​	闭包其实就是一个内部函数，但是这个内部函数对外部作用域的变量进行了引用，并且外部函数的返回值为内部函数，那么这个内部函数就称为闭包。

比如：

```python
def test(x):
  def _in(y):
    return x+y
  return _in
a = test(2)
print(a(3)) # 输出 5
'''
外部函数为test，内部函数为_in，但是_in调用了外部函数的变量x，并且函数的返回值为_in函数
'''
```

注意点：

- 闭包只能引用外部函数的局部变量，不能修改。

更多的知识暂时没接触到，有接触了再更新这个笔记吧~~

#### 匿名函数--lambda()函数

​	匿名函数是指一类不需要使用def去定义，只需要表达式的函数，能够替代一些小的函数。

​	lambda语法为：`lambda [arg1,arg2...argn] : expression` 

​	比如`print((lambda a,b:a+b)(3,4)` 就是一个匿名函数，输出为7.其实就等同于以下代码：

```python
def func(a,b):
	return a+b
print(func(3,4))
```

​	通常，匿名函数都是用在，定义了匿名函数，作为参数传递给另一个函数，再调用。

​	一般来说，定义实际的函数会比匿名函数清晰的多，但是在一些场合需要定义很多的小函数的时候，要记住它们的名字有时有些繁琐，比如在图形界面中，回调函数就可以用匿名函数来定义了。

























































