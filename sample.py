import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='test-report', description='测试deafult报告', log_path='.')
