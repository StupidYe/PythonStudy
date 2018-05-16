### Python-装饰器

---

说到装饰器，很明显就是用来装饰的，既然是要装饰，那肯定是在保留原有的基础上再添加一些东西作为装饰，这就是我对装饰器最直白的理解。

那么如何去学习这个装饰器呢？这个装饰器又是咋回事？

#### 装饰器的几个特点

-----

首先我们需要先记住装饰器的几个特点：

- **装饰器本质上也是一个函数** ，而这个函数的作用就是给其他函数添加一些其他功能作为装饰。
- **装饰器不能去修改原函数的源代码**，只能是增加修饰
- **装饰器不能去修改原函数的调用方式** ，比如函数fun(),调用方式就是fun(),不能改变。

#### 怎么实现装饰器

---

装饰器如果往简单的说就是以前学习的几个知识点结合组合在一起。

**装饰器= 高阶函数+嵌套函数** 

#### 高阶函数

----

- 将函数名作为参数传递给另一个函数

  在python里，函数也是可以像变量那样直接赋值给另一个变量的，这样子就可以把函数名作为实参传给另一个函数了。(依据这个就可以保证装饰器特点之一：不修改原函数的源代码，只添加功能)

  ```python
  def func():
      print("Hello I am func")
      
  def main(var):
      print("Before var()")
      var()
      print("End var()")
      
  #把func作为参数传给main
  main(func)
  # 这样子就给func()函数执行前和执行后都添加了一句打印，是不是没有修改了源码，只添加了功能？
  ```

- 返回值包含函数名

  函数名字可以作为参数传递，那么自然函数名也可以作为返回值了。

  在上面的例子中，虽然没有修改源码就在函数执行前后添加了一句打印，但是这时候函数的调用方式变为了**main(func)** ,而原函数的调用方式应该是**func()** ,这就与装饰器的另一个特点：不能修改原函数的调用方式冲突了，解决方式就是函数名作为返回值。

  ```python
  def func():
      print("Hello I am func")
      
  def main(var):
      print(var)
      return var
  
  print(main(func)) #执行结果：会先打印func的内存地址，然后因为return的也是func，所以也会打印出func的内存地址，也就是会打印两次func的地址
  
  #也可以把返回值赋值给另一个变量
  test = main(func)  
  test()  #等同于func()
  
  #为了不改变调用方式，我可以这么做：
  func = main(func)
  func()  #这样子就跟直接调用func(),看起来一样了，调用方式没有改变
  ```

#### 嵌套函数

---

嵌套函数，就是之前讲过的内部函数，在函数内部定义另一个函数，这里就当做温习下，这里注意内部函数调用和没调用的差别，整体理解不算难。

```python
# 内部函数只定义，没有调用
def out():
    print("I am out")
    def _in():
        print("I am _in")
       
# 只调用out()
out()	# 只会执行out(),内部函数_in()不会执行，因为内部只定义并没有调用

# 内部函数即定义又调用
def out1():
    print("I am out1")
    def _in1():
        print("I am _in1")
    return _in1

func = out1();
func()
```

#### 装饰器

---

1.有了高阶函数和嵌套函数的基础，对于实现一个装饰器就显得比较好办了，从上面例子看好像高阶函数就能实现了装饰器的两个特点，但其调用方式太绕，而高阶函数又恰好能解决这个,两者结合就能实现装饰器了。

```python 
# 定义一个装饰器
def dec(func):
    # 内部定义函数
    def _in():
        print("Before func")
        func()
        print("End func")
    return _in

# 定义一个原函数
def test():
    print("I am test()")
    
test()   # 最初的调用
test = dec(test) # 把返回值赋值给test，显得调用方式并没有变化
test()
```

上面例子dec就是一个装饰器，但是我们在调用的时候总是需要把返回值赋值给原函数名的变量，这样略显麻烦，在python里，**有一个装饰器的语法糖，就是在定义需要装饰的函数前面用@ + 装饰器名字**，比如上例子中可以改为：

```python
# 定义一个装饰器
def dec(func):
    # 内部定义函数
    def _in():
        print("Before func")
        func()
        print("End func")
    return _in

# 定义一个原函数
@dec
def test():
    print("I am test()")
    
test()
```

2.有没有发现上面的例子中，原函数都是没有带参数的？下面说说带参数的原函数，装饰器怎么写。

说下思路：在装饰器里，调用原函数的地方是在内部函数里，return返回的也是内部函数的地址，那么执行的时候也是执行了内部函数，所以如果原函数有参数，那么内部函数也应该要相应跟着参数才可以，否则一定会出错，参数不匹配了。

```python
# 函数参数个数是有限的
def dec(func):
    def _in(arg):
        print("Before func")
        func(arg)
        print("End func")
    return _in

@dec
def test(a):
    print("the arg is %d" %a)
    
test(4)

# 参数个数不限 这里就需要用到 *args **kwargs 了
def dec1(func1):
    def _in1(*args,**kwargs):
        print("Before func1")
        func1(*args,**kwargs)
        print("End func1")
    return _in1

@dec1
def test1(name,arg):
    print("The name is %s,arg is %d" %(name,arg))
   
test1("Test",12)
```

> 注意，如果一个原函数中，有多个装饰器，那么装饰器的执行顺序是怎样的呢？
>
> 答案是从靠近函数头的开始执行，依次向上，比如：
>
> @dec2
>
> @dec1
>
> def func():
>
> ​	pass
>
> 执行顺序是从里到外，依次向上，等效于func = dec2(dec1(func))

3.原函数可以有参数，有没有想过装饰器也可以有参数的？很简单嘛，本文开头就说了装饰器本质就是函数，那它肯定也可以有函数啦！装饰器带参数的做法，就是再多嵌套一层函数

```python
# 不带参数的装饰器
def dec(func):
    def _in(*args,**kwargs):
        print("I am _in")
       	func(*args,**kwargs)
    return _in
   
# 带参数的装饰器
def dec1(flag = 0):
    def real_dec(func):
        def _in(*args,**kwargs):
            if flag == 0:
                print("Run func")
                func(*args,**kwargs)
            else:
                print("No Run func")
        return _in
    return real_dec

@dec
def test():
	print("I am test")
    
@dec1(1)
def test1():
    print("I am test1")

test()
print("-------------")
test1()
```

> 注意：带参数的装饰器，在装饰函数的时候要带上()，比如上面的**@dec1()** 
>
> 另外，除了函数带参数，函数还有返回值，在装饰器里也是一样的，原函数需要返回值，那么在内部函数里就需要return。

4.原函数带有return的情况

```python
def dec(func):
    def _in(*args,**kwargs):
        print("I am _in")
        ret = func(*args,**kwargs)
        print("ret = %d" %(ret))
        return ret
    return _in

@dec
def test(a,b): #两个数相加
    return a+b

test(3,4)
```









