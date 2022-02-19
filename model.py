import time

intervals = []

for x in range(30,841,30):
    intervals.append(x)
    # print(len(intervals))

rd = 0 #rewarded days
t = 0 #temp
r = 0 #reward
value = 10000
value = value - (value * (10/100))
total_reward = 0
    
for timeVar in intervals:
    
    st = timeVar #stakedTime (days)
    wt = timeVar+1 #withdrawTime (days)
    tt = wt - st #days
    hs = st
    
    print("st: " + str(st) + "  wt: " + str(wt))

    for i in range(1,29,1):
        # print("i: " + str(i))
        mi = 30*i
        tt = tt-rd
        # print("tt: " + str(tt))
        if hs >= mi:                            
            rd = (30 + mi)-hs                   
            t = t + rd                          
            if (wt-st)-t < 0:                   
                rd = tt                         
            if rd < 0:                          
                rd = 0                          
            r = rd * value / 365
            # print ("Reward: "+str(r))                
            total_reward = total_reward + r     
            if(rd!=0):
                hs = rd                        
        # print("reward: " + str(r))
    print ("Total reward: "+str(round(total_reward,2)))
    print("APY: " + str(round((total_reward/(value/0.9))/wt*365*100,2)) +"%")
    print("wt: " + str(wt))
    print("\n")
    
    # print ("Done")