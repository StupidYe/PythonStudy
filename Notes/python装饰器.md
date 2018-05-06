

### Python装饰器

学习链接：http://www.cnblogs.com/alex3714/articles/5765046.html

其他博客: https://foofish.net/python-decorator.html

​		https://foofish.net/decorator-with-paramter.html

​		https://foofish.net/understand-decorator.html

1.装饰器本质上是函数，就是为其他函数添加附加功能

2.原则：

- 不能修改被装饰的函数的源代码
- 不能修改被装饰的函数的调用方式

3.实现装饰器(高阶函数+嵌套函数=装饰器)

- 函数即"变量"

- 高阶函数

  - 把一个函数名当做实参传给另外一个函数(不修改函数的源代码情况下为其添加功能)

    ```python
    import time

    def bar():
      print("in the bar")

    def test1(func):
      start_time = time.time()
      func()
      stop_time = time.time()
      print("the func run time is %s" %(stop_time-start_time))
      
    test1(bar)
    ```

  - 返回值中包含函数名(不修改函数的调用方式)

    ```python
    import time

    def bar():
      print("in the bar")

    def test1(func):
      print(func)
      return func
     
    print(test1(bar))	#会先打印bar的内存地址，然后其返回值也是bar的内存地址，也会打印出来
    test2 = test1(bar)
    test2()		#其实是执行了bar()s
    ```

- 嵌套函数

  ```python
  def foo():
  	print("int the foo")
  	def bar():
  		print("in the bar")
  		
  foo()	#执行了 in the foo 不会执行in the bar,因为在函数foo里只是定义了bar()并没有调用

  def test():
    def test1():
      print("in the test1")
    return test1	#如果没有返回，执行test函数，只会定义一个函数，而不会执行其他的

  test2 = test()
  test2() #实际是执行了test1
  ```

- 装饰器=高阶函数+嵌套函数

  ```python
  # 不带参数的装饰器
  import time
  def timer(func):
      def deco():
          start_time = time.time()
          func()
          stop_time = time.time()
          print("the func run time is %s" %(stop_time-start_time))
      return deco

  @timer  #等于是调用了 tese1 = timer(test1)  test1() = deco()
  def test1():
    print("This is tets1")
    
  @timer#等于是调用了 tese2 = timer(test2)  test2() = deco()
  def test2():
    print("This is test2")
    
  test1()
  test2()
  ```

  ```python
  #带参数的装饰器
  import time

  def timer(func):
    def deco(name):
      start_time = time.time()
      func(name)
      stop_time = time.time()
      print("the func run time is %s" %(stop_time-start_time))
    return deco

  @timer
  def test(name):
    print("My name is ",name)
    
  test()

  #参数个数不限
  def timer1(func):
    def deco1(*args,**kwargs):
      start_time = time.time()
      func(args,kwargs)
      stop_time = time.time()
      printf("the func run time is %s" %(stop_time-start_time))
    return deco1

  @timer1
  def test1(name,age):
    print("My name is %s,age is %d" %name %age)
    
  test1()
  ```

- 装饰器函数添加参数

  ```python
  import time

  name = "abc"
  pwd = "123"

  def auth(func):
    def wrapper(*args,**kwargs):
      username = input("Username:").strip()
      password = input("Password:").strip()
      
      if username == name and password == pwd:
        print("login in success")
        func(*args,**kwargs)
      else:
        print("login in fail")
    return wrapper

  @auth
  def home():
    print("Welcome to home")
    
  @auth
  def bbs():
    print("Welcome to bbs")

  home()
  bbs()
  ```

  ​

