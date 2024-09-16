#os.path模块
import os.path
print(os.path.abspath('demo_os.path.py')) #获取文件或目录的绝对路径
print(os.path.exists('demo1.py'),os.path.exists('demo20.py')) #用于判断文件或目录是否存在，返回类型为布尔值
print(os.path.join('E:\\Python','demo13.py'))#将目录与目录或文件名进行拼接
print(os.path.split('E:\\demo1.py'))#分离文件名和扩展名
print(os.path.splitext('demo1.py'))
#从目录当中提取文件名
print(os.path.basename('E:\\py\\py_study\\test_python\\33.文件操作\\demo1.py'))
#从一个路径中提取文件路径，不包括文件名
print(os.path.dirname('E:\\py\\py_study\\test_python\\33.文件操作\\demo1.py'))
#判断是否是路径
print(os.path.isdir('E:\\py\\py_study\\test_python\\33.文件操作\\demo1.py'))


#课程案例见demo_18
