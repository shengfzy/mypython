import random,os
secret = random.randint(1,10)
print(os.getcwd())
print('--------------我爱鱼C工作室-----------------')
cnt = 3
guess = 0
while guess != secret and cnt != 0:
    cnt -= 1
    
    if cnt == 2:
        temp = input('不妨猜一下小甲鱼现在心里想的是哪个数字：')
    else:
        temp = input('诶呀，猜错了，请重新输入吧：')
        
    guess = int(temp)
    
    if  guess == secret:
        print("哇操，你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励")
    else:
        if guess > secret:
            print("哥，大了大了~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^-^")
