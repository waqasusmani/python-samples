import time

rd = 0 #rewarded days
t = 0 #temp
st = 30 #stakedTime (days)
wt = 40 #withdrawTime (days)
tt = wt - st #days
hs = st
r = 0 #reward
value = 100
value = value - (value * (10/100))
total_reward = 0

for i in range(1,29,1):
    print("i: " + str(i))
    mi = 30*i                               #30   
    tt = tt-rd                              #10-0=10
    if hs >= mi:                            #yes (hs=st=30)
        rd = (30 + mi)-hs                   #(30+30)-30=30
        t = t + rd                          #0+30=30
        if (wt-st)-t < 0:                   #(40-30)-30=-20 i.e. < 0
            rd = tt                         #10
        else:
            continue
        if rd < 0:                          #No (rd=10)
            rd = 0                          #N/A
        r = rd * value                      #10*90=900 
        total_reward = total_reward + r     
        hs = rd                             #10
    else:
        continue
    print("reward: " + str(r))
print ("Total reward: "+str(total_reward))
print ("Done")