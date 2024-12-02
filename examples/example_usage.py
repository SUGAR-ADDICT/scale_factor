"""
缩尺比模块使用示例

这个脚本展示了如何使用 `scale_factor` 模块中的 `Length`、`Mass` 和 `CustomTime` 类来构建其他物理量
通常其他物理量都是由就基础量纲经过一些数学操作得到, 比如：
面积=长度**2
体积=长度**3
速度=长度/时间
加速度=长度/时间**2
力=质量*长度/时间**2
其他的物理量同理
"""

from scale_factor.basic_quantity import Length, Mass, CustomTime


def example_usage():
    # 创建 Length、Mass 和 CustomTime 实例
    scale_ratio = 10  # 缩尺比为10
    length = Length(5, scale_ratio)
    mass = Mass(4, scale_ratio)
    time = CustomTime(3, scale_ratio)

    # 示例：面积
    area = length * length  # or area=length**2
    print(f"area : {1/area.scale_factor}")

    # 示例：体积
    volume = length**3
    print(f"volume : {1/volume.scale_factor}")

    # 示例：速度
    velocity = length/time
    print(f"velocity : {1/velocity.scale_factor}")

    # 示例：力
    force = mass*length/time**2
    print(f"force : {1/force.scale_factor}")


if __name__ == '__main__':
    example_usage()
