

from turtle import pos
import pandas as pd
import numpy as np
import math


n = 5
p = 0
price = []
price_list = [[0.1,1.2,12.2,140.1,32],[0.2,2.2,222,11,32],[142,3.2,32.2,140.3,32],[0.4,4.2,42.2,140.4,192],[0.5,5.2,52.2,14.5,32]]

print (type(price_list))

# while n > 0:
#     for i in range (0, len(price_list)):
#         for j in range (0, len(price_list[i])):
#             if price_list[i][j] > 141:
#                 print(j)
#                 n = n - 1
#                 break
def val_return(prices):
   result = []
   for i in range (0, len(prices)):
      for j in range (0, len(prices[i])):
         if prices[i][j] >= 140:
            result.append(j)
            pass
   return result
          
val_return(price_list)
print (val_return(price_list))
print (price)

# x = 0
# while n > 0:
#     main(price_list[x])
#     x = x + 1
#     n = n - 1





