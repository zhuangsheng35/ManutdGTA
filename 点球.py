def dianqiu(num1,num2,num3,num4):

   if num1!=num2:
      print("Goal")
      num3 += 1
   else:
      print("shit")
   return num3,num4

from random import randint

score_you=0
score_com=0
for round in range(1,6):
   print("第%d轮点球，小数字键盘是射门方向，1-9输入数字"%round)
   shoot=int(input())
   if shoot>=10:
      print("必须小于9")
      
   else:
      num=randint(1,9)
      score_you,score_com=dianqiu(shoot,num,score_you,score_com)
   print("门将扑的是%s"%num)
   print("总比分：%d-%d"%(score_you,score_com))
   print("第%d轮点球，小数字键盘是扑球方向，1-9输入数字"%round)
   block=int(input())
   if shoot>=10:
      print("必须小于9")
      
   else:
      num=randint(1,9)
      score_com,score_you=dianqiu(shoot,num,score_com,score_you)
   print("对面踢的是%s"%num)
   print("总比分：%d-%d"%(score_you,score_com))
if score_you>score_com:
   print("你赢了，总比分：%d-%d"%(score_you,score_com))
elif score_you<score_com:
   print("你输了，总比分：%d-%d"%(score_you,score_com))
else:
   print("打平，总比分：%d-%d"%(score_you,score_com))
   
   
