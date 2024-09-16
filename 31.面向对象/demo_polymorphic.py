#多态
class Animal(object):
    def eat(self):
        print('动物都会吃')
class Dog(Animal):
    def eat(self):#这本质上是一个方法重写
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person(object):
    def eat(self):
        print('人啥都吃')


#先定义一个函数
def fun(obj):
    obj.eat()

fun(Dog())
fun(Cat())
fun(Person())
#当我们创建一个Animal对象并调用eat()方法时，Python会调用Animal类的默认实现，当我们创建一个Dog或Cat对象并调用eat()方法时，Python会调用它们自己的实现
#这就是多态的表现形式
