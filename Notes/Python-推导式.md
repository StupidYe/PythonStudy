###  Python-推导式

----

​	推导式，是Python里的一种独有特性，我也是第一次接触这种概念。说白了，推导式就是利用一个或者多个迭代器快速的创建数据结构的方法，可以结合条件判断，循环语句，从而不用像以前那样写很长的代码，整体代码比较整洁。

​	总共有四种推导式：

- 列表推导式

- 字典推导式

- 集合推导式

- 生成器推导式

  其中生成器推导式其实和列表推导式很像，就是把[]换成了()。

#### 列表推导式

----

1.基本形式：

**[expression for item in iterable]** 

2.另一种形式：

**[expression for item in iterable if condition]** 

解释：

- expression ：列表生成的值，也可以是表达式
- for item in itreable：将item传入并迭代iterable
- if condition：条件表达式

3.举例：

```python
# 创建一个列表
my_list = [num for num in range(0,5)]
print(my_list)

# 创建一个列表，expression是表达式的情况
my_list1 = [num*2 for num in range(0,5)]
print(my_list1)

# 添加条件表达式
# 首先是生成列表：[1,2,3,4,5],然后判断是否是偶数，打印出[2,4]
my_list2 = [num+1 for num in range(0,5) if num%2 == 1]
print(my_list2)

```

#### 字典推导式

---

1.基本形式：

**{key_expression:value_expression for expression  in iterable}** 

2.同样有另一种形式：

**{key_expression:value_expression for expression  in iterabl if condition}** 

基本和列表推导式一样，不同之处是列表是中括号[]，字典是大括号{}

3.举例：

```python
str_list = ["apple","orange","banana","pear"]

dic = {key:value for key,value in enumerate(str_list)}
# enumerate是python内置函数，可以将一个可迭代或可遍历的对象组成一个索引序列，能同时获得索引和值
print(dic)

# 输出结果:{0: 'apple', 1: 'orange', 2: 'banana', 3: 'pear'}
```

#### 集合推导式

----

1.集合也有推导式，和列表，字典推导式类似：

**{expression for expression in iterable}** 或**{expression for expression in iterable if condition}** 

2.举例

```python
str_list = str_list = ["apple","orange","banana","pear"]
the_set = {len(s) for s in str_list}
print(the_set)
# 输出结果：{4,5,6} 一样长度的只会算一次，orange和banana都是6
```

#### 生成器推导式

1.其实生成器推导式和列表差不多，只是由中括号[]变成了括号()，但这并不是元组推导式，元组没有推导式。

2.生成器推导式返回的是一个生成器对象，生成器对象可以进行迭代，因为生成器对象也是一种可迭代对象。

3.关于生成器相关的留待学到生成器再记录。













