import numpy as np
print("\n\n"+"-"*50)
print("MAX A, at 5mV input")
print("\nAmplitude at 100 ohm")

ch1 = 4.7142
ch2 = 1547.6
print(ch2/ch1)

print("\nRMS at 100 ohm")
ch1 = 3.5716
ch2 = 1104.2
print(ch2/ch1)
print("-"*10)
print("\nAmplitude at 100k ohm")
ch1 = 4.7142
ch2 = 1773.5
print(ch2/ch1)


print("\nRMS at 100k ohm")
ch1 = 3.5602
ch2 = 1099.7
print(ch2/ch1)




def Ri (v_plus,Vin,R):
  return  v_plus/(Vin-v_plus)*R

def Ro (VL1,VL2,RL1,RL2):
  return (VL2-VL1)*RL1*RL2/(VL1*RL1-VL2*RL2)
print("-"*10)

print("\nRi at 100k ohm")
print(Ri(3.4207,3.6313,99_600))


print("\nRo")
print(Ro(1104.2,1099.7,100,100_000))
print("-"*50)
# ---------------------------------------------------------A10------------------
print("A=10, at 100mV input")
print("\nAmplitude at 100 ohm")

ch1 =   99.335
ch2 =   972.87
print(ch2/ch1)

print("\nRMS at 100 ohm")
ch1 =   70.839
ch2 =   689.48
print(ch2/ch1)
print("-"*10)
print("\nAmplitude at 100k ohm")

ch1 =    99.840
ch2 =    975.59
print(ch2/ch1)


print("\nRMS at 100k ohm")
ch1 =    70.552
ch2 =    689.78
print(ch2/ch1)


print("-"*50)
# ---------------------------------------------------------A10------------------5mA
print("A=10, at 5mV input")
print("\nAmplitude at 100 ohm")

ch1 =     4.7142
ch2 =     45.606
print(ch2/ch1)

print("\nRMS at 100 ohm")
ch1 =     3.5352
ch2 =     34.604
print(ch2/ch1)
print("-"*10)
print("\nAmplitude at 100k ohm")

ch1 =      4.7142
ch2 =      46.967
print(ch2/ch1)

print("\nRMS at 100k ohm")
ch1 =      3.5914
ch2 =      34.904
print(ch2/ch1)

print("-"*10)
print("\n\nRi with R'= 100k ohm  & 100mV input signal amplitude")

listRi = []
listRi.append(Ri( 64.405, 70.572,99_600))
listRi.append(Ri( 64.427, 70.585,99_600))
listRi.append(Ri( 64.405, 70.576,99_600))
listRi.append(Ri( 64.410, 70.586,99_600))
listRi.append(Ri( 64.384, 70.539,99_600))
averageRi=sum(listRi)/len(listRi)

def varians(list):
  avrg=sum(list)/len(list)
  err = 0
  for i in list:
    err+=(i-avrg)**2
  return err/len(list)

def std(list):
  return np.sqrt(varians(list))
print(f"Average: {round(averageRi/1_000_000,3)}M ohm, std: {round(std(listRi)/averageRi*100,3) } %")


print("\nRi with R'= 100k ohm  & 5mV input signal amplitude")
listRi2 = []
listRi2.append(Ri(  3.4311,  3.6248,99_600))
listRi2.append(Ri(   3.3996,   3.5831,99_600))
listRi2.append(Ri(    3.3790 ,    3.5759 ,99_600))
listRi2.append(Ri(   3.3989    ,    3.5798   ,99_600))
listRi2.append(Ri(    3.4270    ,     3.6032    ,99_600))
averageRi2=sum(listRi2)/len(listRi2)

print(f"Average: {round(averageRi2/1_000_000,3)}M ohm, std: {round(std(listRi2)/averageRi2*100,3) } %")



print("\nRo")
print(f"{round(Ro(689.78,689.48,100,100_000)*1000,3)}m ohm")
print(f"{round(Ro(34.904,34.604,100,100_000)*1000,3)}m ohm")



print("-"*50)
