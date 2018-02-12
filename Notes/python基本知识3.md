### Python基本知识3

学习链接：http://www.cnblogs.com/alex3714/articles/5717620.html

#### 5.文件

基本操作：

- 打开文件

  ```python
  f = open('lyrics')

  ```

  >打开文件模式：
  >
  >- r：只读模式(默认)
  >- w：只写模式(不可读，不存在则创建，存在则删除内容)
  >- a：追加模式(可读，不存在则创建，存在则追加内容)
  >
  >'+' 表示可以同时操作文件：
  >
  >- r+：可读写（可读，可写，可追加）
  >- w+：写读
  >- a+：和a一样
  >
  >‘U'表示在**读取**时候，自动将\r\n转换为\n，其他都一样
  >
  >- rU
  >- r+U
  >
  >'b'表示处理二进制文件
  >
  >- rb
  >- wb
  >- ab

  - 关闭文件

    `f.close()` 

  - 设置文件当前位置

    `f.seek(offset)`

  - 返回文件当前位置

    `f.tell()`

  - 截取文件，截取的字节为size

    `f.truncate(size)`

  **with**语句

  ​	为了避免打开文件后忘记关闭，可以使用管理上下文，也就是with，如：

  ​	`with open('test',r) as f: `

  ​	这样的话，with代码块执行完毕后，会自动关闭并释放文件资源。

  ​	Python2.7之后支持同时对多个文件的上下文管理，用逗号分隔：

  ​	`with open('a',r) as f1,open('b',r) as f2:`

  #### 6.函数

  - 函数参数

    函数参数有：默认参数，可变参数

    **默认参数**： 

    ```python
    def message(name,age,country):
        print("name:",name)
        print("age":age)
        print("country",country)

    message("zhangsan",23,"CHINA")
    message("lisi",22,"CHINA")
    message("moumou",24,"CHINA")
    ```

    默认参数就是你不赋值就取默认值，要将参数变成默认参数，只需要在定义时候给定默认值就可以了。

    **需要注意是，默认参数必须放在必选参数的后面** 

    **默认参数必须指向不变对象！** 

    比如：`def func(name,arg,country="CHINA")`

    **可变参数**：

    - \*args  会把传入的多的参数作为一个**元组** （前面是星号，后面的变量名可以自定义）

      比如计算a²+b²+c²....

      ```python
      def calc(*number):
      	sum = 0
          for i in number:
            sum = sum + i * i
          return sum
      #调用方式 也可以不给参数，直接calc(),结果当然是0
      calc(1,2,3,4) #元组[1,2,3,4]的形式
      #如果已经存在一个元组,可以这样传递参数
      data = [1,2,3]
      calc(data[0],data[1],data[2])	#比较繁琐
      #可以直接这样，加个星号
      calc(*data)
      ```

    - \**kwargs 会吧传入的多的参数作为一个**字典** （前面两个是星号，后面的变量名可以自定义）

      这种又叫关键字参数：

      ```python
      def people(name,age,**kwargs):
      	print("name:",name)
      	print("age:",age)
      	print("other:"kwargs)
      #在调用时候，可以传入0个或任意个参数，除了接受name和age参数外，还接受关键字参数kwargs
      #可以不传入关键字参数
      people("ZZY",22)
      #也可以传入关键字参数
      people("zzy",22,city="ShenZhen")
      #可以把dict作为参数传进去
      kw = {'city':'shanghai','job':'Coder'}
      people("zzy",22,**kw)
      ```

      ​

    ​

    ​

  ​

  ​

  ​