# try :
#     # Try this code , if error
# except:
#     # Excute me if try has some error

#example
import math
try:
    math.exp(1000) # OverflowError: math range error
except Exception as e:
    print(e)