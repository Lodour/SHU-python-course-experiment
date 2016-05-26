# coding=utf-8
class Food:  # 食物类

    def __init__(self, name):
        self.name = name


class Employee:  # 商家类

    def __init__(self, namenumber):
        if namenumber == 1:
            self.name = '肯德基'
            self.menu = ['吮指原味鸡', '超级鸡腿堡', '薯条', '老北京鸡肉卷']
        elif namenumber == 2:
            self.name = '麦当劳'
            self.menu = ['麦辣鸡块', '麦辣鸡翅', '薯条', '汉堡']
        elif namenumber == 3:
            self.name = '必胜客'
            self.menu = ['12寸海鲜披萨', '12寸经典披萨', '12寸芝士披萨', '12寸牛肉披萨']
        else:
            self.name = '德克士'
            self.menu = ['德克士鸡块', '超级鸡腿堡', '手枪鸡排', '鸡腿']

    def takeOrder(self, ordernumber):
        nowfood = Food(self.menu[ordernumber - 1])
        return nowfood


class Customer:  # 顾客类

    def __init__(self, name):
        self.name = name
        self.nowchoices = {}

    def PlaceOrder(self, Employee, ordernumber, orderhowmany):
        food = Employee.takeOrder(ordernumber)
        self.nowchoices[food.name] = orderhowmany
        return food


class Lunch:  # 订餐系统类

    def __init__(self):
        self.employees = ['肯德基', '麦当劳', '必胜客', '德克士']

    def creatcustomer(self, name):
        nowcustomer = Customer(name)
        return nowcustomer

    def chooseEmployee(self, namenumber):
        nowemployee = Employee(namenumber)
        return nowemployee

    def printemployee(self):
        k = 1
        for i in self.employees:
            print k,
            print '.',
            print i
            k += 1

    def printfmenu(self, employee):
        k = 1
        for i in employee.menu:
            print k,
            print '.',
            print i
            k += 1

    def order(self, customer, employee, ordernumber, orderhowmany):
        return customer.PlaceOrder(employee, ordernumber, orderhowmany)

    def result(self, customer):
        k = 1
        for i in customer.nowchoices.keys():
            print k,
            print '.',
            print customer.nowchoices[i], '份', i
            k += 1


if __name__ == '__main__':  # 主程序
    nowLunch = Lunch()
    print '欢迎使用订餐系统，请输入顾客昵称：'
    customername = raw_input()
    nowcustomer = nowLunch.creatcustomer(customername)
    print '本订餐系统支持四个商家，如下：'
    nowLunch.printemployee()
    print '请选择需要订餐的商家：'
    employeenumber = int(raw_input())
    # print employeenumber
    nowemployee = Employee(employeenumber)
    print '此商家支持菜品有：'
    nowLunch.printfmenu(nowemployee)

    while 1:
        print '请输入需要订购的菜品序号(一次输入一种，按回车确认，输入0表示结束)：'
        a = int(raw_input())
        if a == 0:
            break
        elif a < 1 or a > 4:
            print '输入有误，请重新输入'
            continue
        else:
            print '请输入要订购的数量：'
            b = int(raw_input())
            nowfood = nowLunch.order(nowcustomer, nowemployee, a, b)
            print '订购', b, '份', nowfood.name, '成功'
    print '已点菜单如下：'
    nowLunch.result(nowcustomer)
