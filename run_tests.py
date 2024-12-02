import unittest

# 自动发现测试并运行
unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('tests'))
