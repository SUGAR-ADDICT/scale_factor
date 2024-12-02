"""
从scale_factor.basic_quantity导入基础量纲之后就可以构建自己的物理量了
"""
from scale_factor.basic_quantity import (Length, CustomTime, Mass)

scale_ratio = 1
length = Length(scale_ratio)
time = CustomTime(scale_ratio)
mass = Mass(scale_ratio)

print(length.scale_factor, time.scale_factor, mass.scale_factor)
