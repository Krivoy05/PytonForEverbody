import test_module
import arithmetic_arranger as aa
import unittest

loader = unittest.TestLoader()
start_dir = '/Users/iservice/PycharmProjects/PytonForEverbody/!course final exam!/arithmetic formatter/'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)

result = aa.arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True)
print(result)

