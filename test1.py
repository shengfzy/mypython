def discounts(price,rate):
    global old_price
    final_price = price * rate
    old_price = 88 #这里试图修改全局变量
    print('修改后old_price的值是1：', old_price)
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)
print('修改后old_price的值是2：', old_price)
print('折扣后价格是：',new_price)
