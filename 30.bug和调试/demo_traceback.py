#traceback模块：可以打印错误信息
import traceback
try:
    print('--------')
    print(1/0)
except:#这里错误类型可以不写
    traceback.print_exc()
