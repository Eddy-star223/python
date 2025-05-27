import to_do_list
from unittest import TestCase


class bank_app_test(TestCase):
	def test_to_do_list(self):
		to_do_list.get_to_do_list()

	def test_that_get_cube_function_return_correct_answer(self):
		actual = to_do_list.get_to_do_list()
		expected = task added
		self.assertEqual(actual, expected)

		
	def test_that_get_function_work(self):
		self.assertEqual(to_do_list.get_to_do_list())