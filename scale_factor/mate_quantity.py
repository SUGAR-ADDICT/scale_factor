"""
元量纲类模块, 定义了量纲之间的运算

:author: SUGAR_ADDICT
:date: 2024-12-02
"""


class MateQuantity:
    """
    元量纲类, 在此处重载了量纲之间的数学运算

    :param scale_factor: 缩尺因子
    """

    def __init__(self, scale_factor: float) -> None:
        self.scale_factor = scale_factor

    def __mul__(self, other):
        """
        重载基础量纲类的乘法
        """
        if isinstance(other, MateQuantity):
            return MateQuantity(self.scale_factor*other.scale_factor)

    def __truediv__(self, other):
        """
        重载基础量纲类的除法
        """
        if isinstance(other, MateQuantity):
            return MateQuantity(self.scale_factor/other.scale_factor)

    def __pow__(self, other):
        """
        重载基础量纲类的幂次方
        """
        if isinstance(other, (int, float)):  # 支持整数或浮动幂
            return MateQuantity(self.scale_factor ** other)
