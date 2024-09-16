#类的创建
#类的组成：1.类属性 2.实例方法 3.静态方法 4.类方法
class Student: #这里Student为类的名称，由一个或者多个单词组成，要求每个单词首字母大写，其余字母小写
    native_place='深圳' #直接写在类里的变量叫类属性
    def __init__(self,name,age):#这是初始化方法
        self.name=name#self.name被称为实例属性 ，进行了一个赋值操作，将局部变量name的值赋给实例属性
        self.age=age


    #实例方法
    def eat(self): #这个self是一定要写的 def在类之外定义叫函数，在类之内定义就叫方法
         print('学生在吃饭')
    @staticmethod
    def method():#静态方法中（）不能写self,没有任何默认参数
        print('该方法使用staticmetion进行修饰，所以是静态方法')
    @classmethod
    def cm(cls):
        print('该方法使用classmethod修饰所以是类方法')

print('类的对象的创建')#注意分辨类对象和类的对象
#对象的创建：接下来创建Student类的对象
stu1=Student('张三',10)#根据类对象创建出来的对象叫做实例对象，有了实例就可以调用类中的内容
print('------------')
#print(id(stu1))
#print(type(stu1))
#print(stu1)
#print('-----------')
#print(id(Student))
#print(type(Student))
#print(Student)


print('方法的调用')
stu1.eat()  #对象名.方法名（）
print(stu1.name,stu1.age)
print('---------还可以这样调用方法---------')
Student.eat(stu1)#37与34行代码功能相同 都是调用Student中的eat方法  类名.方法名（类的对象）--->实际上就是方法定义处的self
print('----------')


print('类属性的使用方式')#类属性被该类的所有对象共享
print(Student.native_place)
stu1=Student('张三',10)
stu2=Student('李四',20)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='梅州'
print(stu1.native_place)
print(stu2.native_place)
print('----------')


print('类方法的使用方式')
Student.cm()
print('静态方法的使用方式')
Student.method()

