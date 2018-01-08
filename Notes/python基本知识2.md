

### Python基本知识2

学习链接：http://www.cnblogs.com/alex3714/articles/5717620.html

#### 1.列表和元组

- 列表

  - 定义：**使用中括号[]** 

    比如定义一个列表：name = ['A','B','C']

  - 列表的操作：切片，追加，插入，修改，删除，扩展，拷贝，统计，排序，翻转，获取下标。

  - 切片：

    1.取多个元素（**注意这是一个半开半闭的，左闭右开区间** ）

    2.从后往回数，可以用-1，-2这样子表示最后一个和倒数第二个

    3.如果从0开始取，0可以省略，可以写成[:3]（表示从零开始的三个）

    4.注意每隔N个取一个元素的时候，比如`[0:-1:2]` ,代表从第0位开始每隔1位就取一个。第三个数字2是代表隔位的，这里是2，是把每一位自己也算进去了当一位，所以每隔两个，第三个数字就应该为3

    （就是比惯性思维的要加1）

    ```python
    name = ['A','B','C','D','E','F']

    #取下标1-4之间的数字，不包括4，但包括1
    print(name[1:4])

    #取下标1-最后一个，不包括最后一个
    print(name[1:-1])

    #从头开始取，0可以忽略
    print(name[:3])

    #想取到最后一个，不能写-1，只能是省略掉后面的
    print(name[2:])

    #隔一定的元素取,从第0个开始，每隔一个元素就取一个
    print(name[0::2])
    #输出为：['A', 'C', 'E']

    #从第0个开始，每隔2个就取一个
    print(name[0::3])
    #输出为：['A', 'D']
    ```

  - 追加：使用函数**append** 

    ```python
    name.append("Append")
    ```

  - 插入：使用函数**insert** 

    ```python
    name.insert(2,"Insert")
    ```

  - 修改：直接用下标再赋值一次

    ```python 
    name[2] = 'b'
    ```

  - 删除：使用**del** 或者指定元素删除，使用**remove** 

    1.删除列表最后一个：**pop函数** （如果没有输入下标就默认删除最后一个）

    ```python
    del name[2]

    name.remove("Append")

    name.pop()

    name.pop(2)
    ```

  - 扩展：使用**extend** 

    >注意：extend与append的区别
    >
    >1.列表可以包含任何数据类型的元素
    >
    >2.append()方法向列表的尾部添加一个新的元素，只接受一个参数
    >
    >3.extend()方法只**接受一个列表作为参数** 

    ```python 
    b = [1,2,3]
    names.extend(b)

    name.extend("extend")
    print(name)
    #输出结果为：
    ['A', 'B', 'C', 'D', 'E', 1, 2, 3, 'e', 'x', 't', 'e', 'n', 'd']
    ```

  - 拷贝：使用**copy函数** (浅copy)

    > 浅copy与重copy
    >
    > 1.浅copy几乎没用到，总共有三种方式
    >
    > (1)使用copy模块的copy方法：name1 = copy.copy(name)
    >
    > (2)name2 = name[:]
    >
    > (3)name2 = list(name)	

    ```python
    name1 = name.copy()
    print(name1)
    ```

  - 统计：使用**count函数** （统计出现的个数）

    ```python
    name.count("A")
    ```

  - 排序：

    1.使用**sort函数** 

    2.使用**sorted函数** 

    > 两者的区别是：sorted返回的是一个新的list，新的list的元素是基于小于运算符来排序的。
    >
    > sort是list内置的方法，而且sort会将list本身将被修改。

    ```python
    name.sort()
    print(name)
    ```

  - 翻转：使用**reverse()函数**

    ```python
    name.reverse()
    print(name)
    ```

  - 获取下标：使用**index函数** 

    ```python
    name.index("C")
    print(name)
    ```

- 元组

  元组和列表其实差不多，只是元组一旦创建就不能再修改，所以又叫只读列表。

  **它只有两个方法：count和index** 

#### 2.字符串

特点：不可修改。

主要是方法的使用：

- 首字母大写：*capitalize()*

  ```python
  name = 'zhangzhanye'

  print(name.capitalize())
  ```



- 大写全部变小写：*casefold()* 

  ```python
  name = 'zhangZHANYe'
  print(name.casefold())
  ```

- 统计xx出现的次数：*count()* 

  ```python
  name = 'zhangZHANYe'
  print(name.count('zha'))
  ```

- 将字符串编码成byte格式：*encode()* 

  ```python
  name = 'zhangZHANYe'
  print(name.encode())
  ```

- 判断字符串是否以xx结尾：*endswith()*

  ```python
  name = 'zhangZHANYe'
  #判断字符串是否以Ye结尾
  print(name.endswith('Ye'))
  ```

- 查找xx，找到返回其索引，找不到返回-1：*find()*

- 查找xx，找到返回其索引，找不到不报错：*index()* 

  ```python
  name = 'zhangZHANYe'
  #查找H，找到返回其索引，找不到返回-1
  print(name.find('H'))
  #找不到会报错
  print(name.index('H'))
  ```

- 格式化操作：*format()*

  ```python
  temp = "my name is {},and age is {}"
  print(temp.format(name,22))

  temp = "my name is {1},and age is {0}"
  print(temp.format(name,22))

  temp = "my name is {name},and age is {age}"
  print(temp.format(name=name,age=22))
  ```

- 字典形式的格式化操作：*format_map()*

  ```python
  temp = "my name is {name},and age is {age}"
  print(temp.format_map({'name':name,'age':22}))
  ```

- 判断是否由数字和字母组成：*isalnum()*

  ```python
  str_test = "A1B2C3"
  print(str_test.isalnum())
  ```

- 判断是否是整数：*isdigit()*

- 判断是否是标题(也就是每个单词的首字母是大写的)：*istitle()*

- 判断是否**只**由空格组成：*isspace()*

- 判断是否**只**由数字组成：*isnumeric()* 

- 判断是否所有的字符都是可打印的：*isprintable()*

- 判断是否所有字母都是大写：*isupper()*

#### 3.字典

特点：键值对，无序，天生去重，key必须是唯一的。

主要操作：

- 增加：直接添加

  ```python
  info = {
      'stu1101': "TengLan Wu",
      'stu1102': "LongZe Luola",
      'stu1103': "XiaoZe Maliya",
  }
  info["stu1104"] = "苍井空"
  print(info)
  ```

- 修改：直接修改

  ```python
  info["stu1101"] = "武藤兰"
  print(info)
  ```

- 删除:有三个方式，pop(),del,popitem()

  ```python
  #标准删除姿势
  info.pop("stu1101") 
  #另一种删除方式
  del info["stu1103"] 
  #随机删除,返回删除掉的元素
  print(info.popitem()) 

  print(info)
  ```

- 查找：使用in，或者get方法

  ```python
  print("stu1102" in info)    #标准用法

  print(info.get("stu1103"))     #获取

  print(info["stu1105"])  #同上
  ```

- 其他方法

  - values():只获取字典的所有值

    ```python
    print(info.values())    #只获取字典的所有值
    ```

  - keys():只获取字典的所有key

    ```python
    print(info.keys())      #只获取字典的所有key
    ```

  - update():把另一个字典更新到字典中

    ```python
    print(info.setdefault("stu1106","Alex"))    #如果键不存在于字典中，将会添加键并且设置值为默认值，如果存在，则打印键的值
    ```

  - setdefault():如果键不存在字典中，将会添加键并且设置值为默认值，如果键存在，则会打印键的值

    ```python
    b = {1:2,3:4}
    info.update(b)  #把字典b更新到字典info中
    print(info)
    ```

  - items():以列表返回可遍历的（键，值）

    ```python
    print(info.items()) #以列表返回可遍历的(键，值)
    ```

- 循环

  - 标准方法:使用in

    ```python
    for key in info:
        print(key,info[key])
    ```

  - 不建议使用的方法：使用items()

    ```python
    #会先把dict转为list，数据量大的时候不使用
    for k,v in info.items():
        print(k,v)
    ```

#### 4.集合

特点：无序，没有重合的数据

作用：

​	1.去重，把一个列表变成集合，就自动去重了。

​	2.关系测试，测试两组数据之间的交集，差集，并集等关系

常用的操作：

```python
#创建集合
s = set([0,2,4,6,8])
t = set([1,3,5,7,9])

#s 和 t的并集
a = t | s
#测试 并集
s.union(t)

#s 和 t的交集
b = t & s
#测试 交集
s.intersection(t)

#s 和 t的差集(t中有，s中没有)
c = t - s
#测试 差集
t.difference(s)	#t中有，s中没有

#对称差集 (在t或s中有，但不是两者都有的)
d = t ^ s
#测试 对称差集
s.symmetric_difference(t) #返回一个新的set，包含s和t中不重复的元素

#基本操作
t.add(11) 		#添加一项
s.add([10,12]) 	#添加多项

#使用remove删除一项
s.remove(12)

#集合长度
print(len(t))

#测试是否s中的每一个元素都在t中 s是不是t的子集
s.issubset(t) #s<=t

#测试是否t中的每一个元素都在s中	s是不是t的父集
s.issuperset(t)
```



