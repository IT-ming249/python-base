#首先自定义模块
def Add(a,b):
    return a+b
def div(a,b):
    return a/b
#如何导入自定义模块：见demo_imp_self
if __name__ == '__main__':#这表示下面的语句将只在点击运行clc.py的时候执行
    print(Add(10,20))#没有main操作，这句代码将在导这个包的程序里面运行