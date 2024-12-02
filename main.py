"""
从scale_factor.basic_quantity导入基础量纲之后就可以构建自己的物理量了
"""
from scale_factor.basic_quantity import (Length, CustomTime, Mass)

# 设置缩尺比为1:10
scale_factor = 10
length = Length(10, scale_factor)  # 长度的值为10
time = CustomTime(5, scale_factor)  # 时间的值为5
velocity = length/time  # 通过数学运算得到速度类
value = velocity

print(rf"{value.scale_value}= {value.value} * {1/value.scale_factor}")
# print(length.scale_factor, time.scale_factor, mass.scale_factor)
