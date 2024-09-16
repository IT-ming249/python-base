#with语句：上下文管理器
with open('a.txt','r') as file: #open('a.txt','r')是一个无论是否产生异常都会自动调用enter，exit方法的类，可以保证每次都自动释放系统资源
    print(file.read()) #这样就不用写close了，出with语句时会自动释放系统资源
#下面定义一个类来理解上下文管理器
class Mycontact:
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')
    def show(self):
        print('show方法被执行了')

with Mycontact() as fiil:
    fiil.show()  #可以看到enter方法和exit方法会被自动执行
#例子：使用with语句来实现图片的复制
with open('logo.PNG','rb') as scr_file:
    with open('copy2loge.PNG','wb') as traget_file:
        traget_file.write(scr_file.read())
