"""
基础量纲类, 通过元量纲构建了常用的三个基础量纲，长度、质量、时间

:author: SUGAR_ADDICT
:date: 2024-12-02
"""
from scale_factor.mate_quantity import MateQuantity


class Length(MateQuantity):
    def __init__(self, scale_factor: float) -> None:
        super().__init__(scale_factor)


class Mass(MateQuantity):
    def __init__(self, scale_factor: float) -> None:
        super().__init__(scale_factor**3)


class CustomTime(MateQuantity):
    def __init__(self, scale_factor: float) -> None:
        super().__init__(scale_factor**0.5)
