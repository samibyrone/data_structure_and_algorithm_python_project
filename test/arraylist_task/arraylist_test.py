import unittest

from DSA.arraylist_task.arraylist import ArrayList

class TestArrayList(unittest.TestCase):

    def test_that_array_list_is_empty(self):
        array_list = ArrayList()
        self.assertEqual(0, array_list.total_size())
        self.assertTrue(array_list.is_empty(), "Array list should is empty")

    def test_that_arrayList_can_add_element_to_arrayList(self):
        array_list = ArrayList()
        array_list.add("Samibyrone")
        array_list.add("Semicolon")
        array_list.add("Europe")
        self.assertEqual(3, array_list.total_size())
        self.assertEqual(False, array_list.is_empty(), "Array list should definitely not be empty")

    def test_that_arrayList_can_remove_element_from_arrayList(self):
        array_list = ArrayList()
        array_list.add("Samibyrone")
        array_list.add("Semicolon")
        array_list.add("Europe")
        array_list.add(500000)
        array_list.add("Chibuzor")
        array_list.remove("Chibuzor")
        array_list.remove("Europe")
        self.assertEqual(3, array_list.total_size())
        self.assertEqual(False, array_list.is_empty(), "Array list should definitely not be empty")

    def test_that_arrayList_can_get_element_from_index_position(self):
        array_list = ArrayList()
        array_list.add("Samibyrone")
        array_list.add("Semicolon")
        array_list.add("Europe")
        array_list.add(500000)
        array_list.add("Fantastic")
        self.assertEqual(array_list.get(3), 500000)
        self.assertEqual(5, array_list.total_size())
        self.assertEqual(False, array_list.is_empty(), "Array list should definitely not be empty")

    def test_that_arrayList_can_get_element_of_index_not_on_the_list(self):
        array_list = ArrayList()
        array_list.add("Samibyrone")
        array_list.add("Semicolon")
        array_list.add("Europe")
        array_list.add(500000)
        array_list.add("Fantastic")
        array_list.add("Chibuzor")
        self.assertFalse(array_list.get(10))
        self.assertEqual(6, array_list.total_size())
        self.assertEqual(False, array_list.is_empty(), "Array list should definitely not be empty")

    def test_that_arrayList_can_resize_element_in_the_array_position(self):
        array_list = ArrayList()
        array_list.add("Samibyrone")
        array_list.add("Semicolon")
        array_list.add("Europe")
        array_list.add(500000)
        array_list.add("Fantastic")
        array_list.add("Chibuzor")
        array_list.resize()
        for index in range(10):
            array_list.add(str(f"Encyclopedia[{index}]"))
        self.assertEqual(110, array_list.total_size())
        self.assertEqual(False, array_list.is_empty(), "Array list should definitely not be empty")
        