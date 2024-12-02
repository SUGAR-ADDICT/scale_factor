"""
元量纲类模块, 定义了量纲之间的运算

:author: SUGAR-ADDICT
:date: 2024-12-02
"""


class MateQuantity:
    """
    元量纲类, 在此处重载了量纲之间的数学运算

    :param value: 物理量的值
    :param scale_factor: 缩尺比的分母
    :param scale_value: 经过缩放后的值,scale_value=value*(1/scale_factor)

    :raises ValueError: 如果 `scale_factor` 为0, 则抛出异常
    """

    def __init__(self, value: float, scale_factor: float) -> None:
        if scale_factor == 0:
            raise ValueError("Scale factor must be non-zero.")
        self.value = value
        self.scale_factor = scale_factor
        self.scale_value = value * (1 / scale_factor)

    def __repr__(self):
        return f"MateQuantity(value={self.value}, scale_factor={self.scale_factor}, scale_value={self.scale_value})"

    def __mul__(self, other):
        """
        重载基础量纲类的乘法

        :param other: 可以是另一个 MateQuantity 对象，或一个数字 (int/float)
        :type other: MateQuantity, int, float

        :return: 乘法结果，一个新的 MateQuantity 对象

        :raises TypeError: 当 `other` 既不是MateQuantity, 也不是数字类型
        """
        if isinstance(other, MateQuantity):
            return MateQuantity(self.value*other.value, self.scale_factor*other.scale_factor)
        elif isinstance(other, (int, float)):
            return MateQuantity(self.value*other, self.scale_factor)
        else:
            return TypeError("Multiplication only supports numeric types or MateQuantity instances.")

    def __truediv__(self, other):
        """
        重载基础量纲类的除法运算符。

        :param other: 可以是另一个 MateQuantity 对象，或一个数字 (int/float)。
        :type other: MateQuantity, int, float

        :return: 除法结果，一个新的 MateQuantity 对象。
        :rtype: MateQuantity

        :raises ValueError: 当试图以值为 0 的量纲或数字除法时。
        :raises TypeError: 当 `other` 既不是 MateQuantity，也不是数字类型时。
        """
        if isinstance(other, MateQuantity):
            if other.value == 0:
                raise ValueError(
                    "Cannot divide by a MateQuantity with value 0.")
            return MateQuantity(self.value/other.value, self.scale_factor/other.scale_factor)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ValueError(
                    "Cannot divide by a MateQuantity with value 0.")
            return MateQuantity(self.value/other, self.scale_factor)
        else:
            return TypeError("Division only supports numeric types or MateQuantity instances.")

    def __pow__(self, other):
        """
        重载基础量纲类的幂运算符

        :param other: 一个数字 (int/float)
        :type other: int, float

        :return: 幂运算结果，一个新的 MateQuantity 对象

        :raises TypeError: 当 `other` 不是数字类型时
        """
        if isinstance(other, (int, float)):  # 支持整数或浮动幂
            return MateQuantity(self.value**other, self.scale_factor ** other)
        else:
            return TypeError("Exponentiation only supports numeric types")
