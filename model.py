
rd = 0 #rewarded days
t = 0 #temp
st = 659 #stakedTime (days)
wt = 660 #withdrawTime (days)
tt = wt - st #days
hs = st
r = 0 #reward
value = 10000
value = value - (value * (10/100))
total_reward = 0

for i in range(1,29,1):
    print("i: " + str(i))
    mi = 30*i                   
    print("mi: " + str(mi))
    print("st: " + str(st))
    print("wt: " + str(wt))
    print("initial tt: " + str(tt))
    print("rd: " + str(rd))
    tt = tt-rd
    print("tt = tt-rd: " + str(tt))
    print("hs: " + str(hs))
    if hs >= mi:
        print("------ Comparison starts -----")                            
        if not((30 + mi)-hs < 0):
            rd = hs-mi                  
        print("rd at hs mi comparison: " + str(rd))
        t = t + rd                          
        print("t: " + str(t))
        # print("(wt-st)-t: " + str((wt-st)-t))
        # if (wt-st)-t < 0:                   
        #     rd = tt                         
        print("rd at wt-st: " + str(rd))
        if rd < 0:                          
            rd = 0                          
        print("rd at <0 comparison: " + str(rd))
        if rd > 0 and wt-st>=0:
            r = rd * value / 28 * i
            hs = rd
        print ("Reward: "+str(round(r)))                
        total_reward = total_reward + r     
        print("my rd: " + str(rd))
        print("hs at last change: " + str(hs))                        
    else:
        print("No reward")
    print("last rd: " + str(rd))
    print("----------------------------------")
print ("Total reward: "+str(round(total_reward,2)))
print("APY: " + str(round((total_reward/(value/0.9))/st*365*100,2)) +"%")
print("\n")
