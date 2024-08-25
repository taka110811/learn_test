import pytest
import calculation

class TestCalTest():
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert cal.add_num_and_double(1,1) == 4    

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = calculation.Cal()
            cal.add_num_and_double('1','1')

if __name__ == '__main__':
    pytest.main()

# release_name = 'lesson'

# class CalTest(unittest.TestCase):
#     def setUp(self):
#         print('setup')
#         self.cal = calculation.Cal()

#     def tearDown(self):
#         print('clean up')
#         del self.cal

#     # @unittest.skip('skip')
#     @unittest.skipIf(release_name=='lesson', 'skip!!')
#     def test_add_num_and_double(self):
#         self.assertEqual(self.cal.add_num_and_double(1,1), 4)

#     def test_add_and_num_double_raise(self):
#         with self.assertRaises(ValueError):
#             self.cal.add_num_and_double('1', '1')

# if __name__ == '__main__':
#     unittest.main()