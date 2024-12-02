import unittest
from scale_factor.basic_quantity import Length, Mass, CustomTime


class TestScaleFactor(unittest.TestCase):
    def setUp(self):
        # 设置缩尺因子
        self.scale_factor = 10

        # 实例化各个类
        self.length = Length(self.scale_factor)
        self.mass = Mass(self.scale_factor)
        self.time = CustomTime(self.scale_factor)

    def test_length_multiplication(self):
        # 测试长度乘法
        result = self.length * self.length
        self.assertEqual(result.scale_factor, self.scale_factor ** 2)

    def test_length_division(self):
        # 测试长度除法
        result = self.length / self.length
        self.assertEqual(result.scale_factor, 1)


if __name__ == '__main__':
    unittest.main()
