# -*- coding: utf-8 -*-
"""Class6Module3_20241210.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GUneXrL6ZMOzW5ZliueddK_QyFySusaz
"""

raise Exception("This is exception")

num = 5
if num %2 != 0:
  raise Exception("this is not divisible by 2")

def even(x):
  try:
    if x%2==0:
      return "even"
    else:
      raise Exception
  except:
    return("odd")
  finally:
    return "integer"

print(even(5))    #A
print(even(4))    #B

print(even(10))