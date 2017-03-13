import random
blue_result=random.sample(range(16), 1)
red_result=random.sample(range(33), 6)
times=0
print("中奖号码：蓝球：%s,红球：%s"%(blue_result,red_result))
blue=random.sample(range(16), 1)
red=random.sample(range(33), 6)

while blue_result!=blue or red_result!=red:
        times+=1
        blue=random.sample(range(16), 1)
        red=random.sample(range(33), 6)
        print("第%s次没中：蓝球：%s,红球：%s"%(times,blue,red))
        



        if blue_result==blue and red_result==red:

                 print("第%s次中奖！：蓝球：%s,红球：%s"%(times,blue,red))
                 break
