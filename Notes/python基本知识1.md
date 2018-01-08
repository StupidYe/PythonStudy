#### Python基本知识1

学习链接：https://www.cnblogs.com/alex3714/articles/5465198.html

#### 1.终端输入函数

- input函数

从终端获取输入可以调用**input** 或者**raw_input**。

```python
name = input("my name is:");
print(name)
```

运行报错：(原因如下)

```python
root@ubuntu:~/python-3.6/python# python test1.py 
my name is:zzy
Traceback (most recent call last):
  File "test1.py", line 4, in <module>
    name = input("my name is:")
  File "<string>", line 1, in <module>
NameError: name 'zzy' is not defined
```

>注意：(摘抄自http://www.runoob.com/python/python-func-input.html)
>
>1.input() 和 raw_input() 这两个函数均能接收 字符串 。
>
>2.raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你**输入字符串的时候必须使用引号将它括起来** ，否则它会引发一个 SyntaxError 
>
>除非对 input() 有特别需要，否则一般情况下我们都是**推荐使用 raw_input() 来与用户交互**。
>
>3.python3 里 input() 默认接收到的是 str 类型。

最终结果应为：

```python
root@ubuntu:~/python-3.6/python# python test1.py 
my name is:"zzy"
zzy
```

#### 2.密码不可见的实现

使用**getpass模块中的getpass方法** 。（该方法不会回显，感觉就像没有输入一样~）

```python 
import getpass

password = getpass.getpass("Pleas Input Password: ")

print("You Input Password is " + password)
```

#### 3.中文注释问题

Python中：

- 单行注释使用：#
- 多行注释：“”“  （三个双引号）或者 ’‘’（三个单引号）

注释中文会报以下错误：

`SyntaxError: Non-ASCII character '\xe7' in file test1.py on line 30, but no encoding declared; ` 

解决方法就是：告知Python编码方式，在文件的顶层添加以下一句

`-*- coding: utf-8 -*` 

> 注意：这个格式还必须是这样子，不能不同，编码方式为utf-8，这个可以改为相应的编码方式！





























