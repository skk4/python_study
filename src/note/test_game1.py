# -*- coding:utf-8 -*-
'''
游戏场景范围为x=【0,10】， y=【0,10】
有乌龟、鱼，乌龟体力初始值为100，乌龟移动一次消耗1个体力，鱼暂时不计算体力，乌龟1个，鱼10条
乌龟和鱼初始坐标随机生成，当然坐标也必须在x=【0,10】， y=【0,10】里面
乌龟最大移动距离【1,2，-1，-2】，鱼移动距离固定为【1】
当移动到场景边缘即坐标（x，y）为（x, 0），（x,10），（0， y），（10,y）自动向反方向移动
当乌龟和鱼坐标重叠时，乌龟吃掉鱼，乌龟体力增加20
当乌龟体力值为0（挂掉），或者鱼儿的数量为0，游戏结束
'''

import random
class Fish:
    def __init__(self):
        self.x = random.randrange(x_range[0], x_range[1])
        self.y = random.randrange(y_range[0], y_range[1])
        
    def move(self):
        new_x = self.x + random.choice([1, -1])
        new_y = self.y + random.choice([1, -1])
        
        print 'f_x', new_x
        print 'f_y', new_y

        if new_x < x_range[0]:
            self.x = x_range[0] - (new_x - x_range[0]) 
         
        elif new_x > x_range[1]:
            self.x = x_range[1] - (new_x - x_range[1])
            
        else:
            self.x = new_x    
            
        if new_y < y_range[0]:
            self.y =  y_range[0] - (new_y - y_range[0]) 
            
        elif new_y > y_range[1]:
            self.y =  y_range[1] - (new_y - y_range[1])
            
        else:
            self.y = new_y      
        
        return (self.x, self.y)
            
        
class Tortoise:
    def __init__(self):
        self.power = power
        self.x = random.randrange(x_range[0], x_range[1])
        self.y = random.randrange(y_range[0], y_range[1])
        
    def eat(self): 
          
        
        if self.power >100:
            self.power = 100
        
        else:
            self.power += 20
        
    def gameover(self):
        if self.power == 0:
            print 'game over'
                 
    def move(self):
        new_x = self.x + random.choice([1, -1, 2, -2])
        new_y = self.y + random.choice([1, -1, 2, -2])
        
        print 't_x:', new_x
        print 't_y:', new_y

        
        self.power -= 1
        
        if new_x < x_range[0]:
            self.x = x_range[0] - (new_x - x_range[0]) 
         
        elif new_x > x_range[1]:
            self.x = x_range[1] - (new_x - x_range[1])
            
        else:
            self.x = new_x
            
            
        if new_y < y_range[0]:
            self.y =  y_range[0] - (new_y - y_range[0]) 
            
        elif new_y > y_range[1]:
            self.y =  y_range[1] - (new_y - y_range[1])
            
        else:
            self.y = new_y
            
            
        return (self.x, self.y)     




#x,y 范围
x_range = [0, 10]
y_range = [0, 10]
power  = 100 
       
f = Fish()
t = Tortoise() 
print 'f:', f
print 't:', t      
position_fish = (f.x, f.y)  
positon_Tortoise = (t.x, t.y)
print 'fish_1:', position_fish
print 'Tortoise_1:', positon_Tortoise 
print 'power_1:', t.power
print 'fish_2:\n', f.move()
print 'Tortoise_2:\n', t.move()   
print 'power_2:', t.power
           
    