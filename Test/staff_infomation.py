# 文件操作的模块
import os
import sys

# 查找，支持三种查询语句
# select name,age from staff_table where age > 22
# select * from staff_table where dept = IT
# select * from staff_table where enroll_date like "2013"
def select(data):
    #将输入的语句以空格为分隔符分隔,tmp_data为列表
    tmp_data = data.split(" ")
    if len(tmp_data) < 7:
        print("输入的查询语句，语法不对！！！")
        return 0
    
    #查询到的个数
    num = 0
    #第一种查询语句
    if data == ("select name,age from staff_table where age > %s" %(tmp_data[7])):
        with open("staff_table",encoding="utf-8") as f:
            for line in f:
                data_list = line.strip().split(",") #去除首尾空格，再以逗号为分隔符分隔
                name = data_list[1]
                age = data_list[2]
                if age > tmp_data[7]:
                    num += 1
                    print(line.strip())
    elif data == ("select * from staff_table where dept = %s" %(tmp_data[7])):
        with open("staff_table",encoding="utf-8") as f:
            for line in f:
                data_list = line.strip().split(",")
                dept = data_list[4]
                if dept == tmp_data[7]:
                    num += 1
                    print(line.strip())
    elif data == ("select * from staff_table where enroll_date like %s" %(tmp_data[7])):
        with open("staff_table",encoding="utf-8") as f:
            for line in f:
                data_list = line.strip().split(",")
                enroll_date = data_list[5]
                year = enroll_date.split("-")
                if year[0] == eval(tmp_data[7]):
                    num += 1
                    print(line.strip())
        
    print("查询到%d条符合的信息" %(num))
    
# 添加，以phone为唯一键，staff_id需要自增
# 语法为：name,age,phone,dept,enroll-date
def add(data):
    tmp_data = data.split(",")
    staff_id = 0
    with open("staff_table","r+",encoding="utf-8") as f:
        #先查找文件中是否已经存在这个数据
        for line in f:
            data_list = line.strip().split(",")
            #获取staff_id，用于staff_id自增
            staff_id = data_list[0]
            if data_list[3] == tmp_data[2]:
                print("添加的信息已经存在！")
                return 0
        #不存在，添加到文件中，然后staff_id自增
        staff_id = int(staff_id) + 1
        new_data = str(staff_id) + "," + data
        f.write("\n")
        f.write(new_data)

# 删除员工信息，以id为索引    
def delete(staff_id):
    delete_flag = 0
    #查找文件，找到与id相应的员工，删除
    with open("staff_table","r+",encoding="utf-8") as f:
        with open("temp_table","w+",encoding="utf-8") as f1:
            for line in f:
                data_list = line.strip().split(",")
                if data_list[0] == staff_id:
                    #找到相应员工，删除
                    print("已删除ID为%d的员工信息!" %int(staff_id))
                    delete_flag = 1
                else:
                    f1.write(line)
    if delete_flag == 1:
        #删除原文件，修改文件temp_table为staff_table
        os.remove("staff_table")
        os.rename("temp_table","staff_table")
    else:
        print("该ID的员工不存在!")

# 修改员工信息,修改部门
# 语法为：update staff_table set dept = HR where dept = IT
def change(data):
    tmp_data = data.split(" ")
    with open("staff_table","r+",encoding="utf-8") as f:
        with open("temp_table","w+",encoding="utf-8") as f1:
            for line in f:
                data_list = line.strip().split(",")
                if tmp_data[9] == data_list[4]:
                    line = line.replace(tmp_data[9],tmp_data[5])
                f1.write(line)
    os.remove("staff_table")
    os.rename("temp_table","staff_table")


def main():
    msg = \
    """
    1.查询
    2.添加
    3.删除
    4.修改
    5.退出
    """

    msg_dict = {
        "1":select,
        "2":add,
        "3":delete,
        "4":change,
        "5":exit,
    }
    while True:
        print(msg)
        choic = input("输入您的操作序号:>>")
        if choic == '0' or choic not in msg_dict:
            print("您输入的序号有误或不存在此操作，请重新输入!")
            continue
        if choic != '5':
            data = input("请输入数据:>>").strip()
            msg_dict[choic](data)
        else:
            sys.exit()

'''
find = "select name,age from staff_table where age > 22"
find1 = "select * from staff_table where dept = HR"
find2 = "select * from staff_table where enroll_date like \"2013\""
find3 = "find"

#select(find3)

new_data = "zzy zhang,24,15976785138,IT,2017-07-01"
#add(new_data)
#delete(5)

new_data = "update staff_table set dept = HR where dept = IT"
#change(new_data)
'''


main()