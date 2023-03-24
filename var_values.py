#2.WAP that displays values of different variables used in the program.
import pandas as pd
var1=32
var2=21.35
var3="sapna"
var4='S'
var5=6542.3215488
var6=[2,3,4,5,6]
var7=(3,5,7,8)
var8=False
var9=pd.Series(var6)
df=[[2,3,4,5,6],[3,3,7,5,4],[2,3,4,5,6]]
var10=pd.DataFrame(df)
var11={'a':"abc",'b':"def",'c':"ghi"}
print(type(var1)," ",var1)
print(type(var2)," ",var2)
print(type(var3)," ",var3)
print(type(var4)," ",var4)
print(type(var5)," ",var5)
print(type(var6)," ",var6)
print(type(var7)," ",var7)
print(type(var8)," ",var8)
print(type(var9),"\n",var9)
print(type(var10),"\n",var10)
print(type(var11)," ",var11)