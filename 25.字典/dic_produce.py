#字典生产式
#使用内置函数zip(
#语法结构：{item(键):price(值) for item,price in zip(items(键的列表名),prices(值的列表名))} for前后两部分相同
items=['Friuts','Book','Other']
prices=[98,78,85]
sorces={i.upper():p for i,p in zip(items,prices)}#upper()变大写
print(sorces)