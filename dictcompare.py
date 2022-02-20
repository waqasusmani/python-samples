import math

d1={"aa":10,"bb":20,"cc":30,"dd":40}
d2={"aa":90,"bb":10,"cc":90,"dd":"str"}

def dictCompare(deadzone,dict1,dict2):
    dict1Keys=[]
    dict2Keys=[]
    d3={}
    for k in dict1:
        dict1Keys.append(k)
    for k in dict2:
        dict2Keys.append(k)
    print("dict1 keys: "+str(len(dict1Keys)))
    print("dict2 keys: "+str(len(dict2Keys)))
    if (len(dict1Keys)!=len(dict2Keys)):
        print("Keys not equal")
        return d3
    for k in dict1Keys:
        try:
            val=dict1[k]
            try:
                fval1=float(val)
                if (math.isnan(fval1)):
                    print("Not a number in dict1["+k+"]: "+str(val))
                    break
            except ValueError:
                print("Not a number in dict1["+k+"]: "+str(val))
                break
            val=dict2[k]
            try:
                fval2=float(val)
                if (math.isnan(fval2)):
                    print("Not a number in dict2["+k+"]: "+str(val))
                    break
            except ValueError:
                print("Not a number in dict2["+k+"]: "+str(val))
                break

            fdiff=fval2-fval1
            if (fdiff<0):
                fdiff*=-1
            if (fdiff<deadzone):
                d3[k]=0
            else:
                d3[k]=fdiff
        except KeyError:
            print("Key "+k+" not exists in dict2")
            break
    return d3
d3=dictCompare(5,d1,d2)
print(d3)