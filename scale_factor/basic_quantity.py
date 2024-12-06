"""
基础量纲类, 通过元量纲构建了常用的三个基础量纲，长度、质量、时间

:author: SUGAR-ADDICT
:date: 2024-12-02
"""
from scale_factor.mate_quantity import MateQuantity


class Length(MateQuantity):
    def __init__(self, value, scale_factor: float) -> None:
        super().__init__(value, scale_factor)


class Mass(MateQuantity):
    def __init__(self, value, scale_factor: float) -> None:
        super().__init__(value, scale_factor**3)


class CustomTime(MateQuantity):
    def __init__(self, value, scale_factor: float) -> None:
        super().__init__(value, scale_factor**0.5)


def custom_quantity(value, custom_dimension: MateQuantity):
    """
    通过值和单位，获取自定量纲的MateQuantity对象

    Args:
        value (float): 单位的数量值
        custom_dimension (MateQuantity): 包含缩尺比的MateQuantity对象，值为1

    Returns:
        MateQuantity: 自定义量纲
    """
    return MateQuantity(value, custom_dimension.scale_factor)
