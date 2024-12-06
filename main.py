"""
从scale_factor.basic_quantity导入基础量纲之后就可以构建自己的物理量了
"""
from scale_factor.basic_quantity import (
    Length, CustomTime, Mass, custom_quantity)

# 设置缩尺比为1:10
scale_factor = 10
length = Length(10, scale_factor)  # 长度的值为10
time = CustomTime(5, scale_factor)  # 时间的值为5
velocity = length/time  # 通过数学运算得到速度类
value = velocity

print(rf"{value.scale_value}= {value.value} * {1/value.scale_factor}")

# 对于不能直接通过值计算的单位，比如转动惯量，可以同过custom_quantity创建MateQuantity实例
mate_length = Length(1, scale_factor)
mate_mass = Mass(1, scale_factor)

rotational_inertia_x = custom_quantity(1000, mate_mass*mate_length**2)

value = rotational_inertia_x

print(rf"{value.scale_value}= {value.value} * {1/value.scale_factor}")
