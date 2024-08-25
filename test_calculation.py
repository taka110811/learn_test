import os
import pytest
import calculation
is_release = True

class TestCalTest():

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_file_name = 'text.txt'

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1','1')

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