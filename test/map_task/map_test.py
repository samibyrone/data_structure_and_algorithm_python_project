import unittest

from DSA.map_task.map import Map

class TestMap(unittest.TestCase):

    def test_that_map_is_empty(self):
        map = Map()
        self.assertEqual(map.size(),0)
        self.assertTrue(map.isEmpty())

    def test_that_map_is_not_empty(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        self.assertEqual(5, map.size())
        self.assertFalse(map.isEmpty())

    def test_that_map_can_add_element_and_get_element_on_the_map_list(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        self.assertEqual(4, map.get("Fantastic"))
        self.assertEqual(1, map.get("Samibyrone"))
        self.assertEqual(5, map.get("Exceptional"))
        self.assertEqual(5, map.size())
        self.assertFalse(map.isEmpty())

    def test_that_map_can_compute_element_from_map_list(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        map.compute("pass-over", lambda x: 1 if x is None else x + 1)
        self.assertEqual(1, map.get("pass-over"))
        map.compute("pass-over", lambda x: 1 if x is None else x + 1)
        self.assertEqual(2, map.get("pass-over"))
        self.assertEqual(6,map.size())
        self.assertFalse(map.isEmpty())

    def test_that_map_can_compute_ifAbsent_element_from_map_list(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        map.compute_if_absent("Semicolon22", lambda: "value6")
        self.assertEqual("value6", map.get("Semicolon22"))
        map.compute_if_absent("Samibyrone78", lambda: "value7")
        self.assertEqual("value7", map.get("Samibyrone78"))
        self.assertEqual(7, map.size())
        self.assertFalse(map.isEmpty())

    def test_that_map_can_compute_ifPresent_element_from_map_list(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        map.compute_if_present("Semicolon22", lambda y: y.upper())
        self.assertEqual("VALUE6", map.get("Semicolon22"))
        map.compute_if_present("Samibyrone78", lambda y: y.upper())
        self.assertEqual("VALUE7", map.get("Samibyrone78"))
        self.assertEqual(7, map.size())
        self.assertFalse(map.isEmpty())

    def test_that_map_containsKey_in_element_on_map_list(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        self.assertEqual(map.contains_key("Semicolon"), True)
        self.assertEqual(map.contains_key("Fantastic"), True)
        self.assertEqual(5, map.size())
        self.assertFalse(map.isEmpty())

    def test_that_map_containsValue_in_element_on_map_list(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        self.assertEqual(map.contains_value("Semicolon"), True)
        self.assertEqual(map.contains_value("Expendable"), True)
        self.assertEqual(map.contains_value("Exceptional"), True)
        self.assertEqual(map.contains_value("Orimolade"), False)
        self.assertEqual(5, map.size())
        self.assertFalse(map.isEmpty())

    def test_that_map_for_hash_code_from_map_list(self):
        map = Map()
        map.put("Samibyrone", 1)
        map.put("Semicolon", 2)
        map.put("Expendable", 3)
        map.put("Fantastic", 4)
        map.put("Exceptional", 5)
        ash = map.hash(frozenset(hash))
        self.assertEqual(ash, map.hashCode())
        self.assertEqual(5, map.size())
        self.assertFalse(map.isEmpty())