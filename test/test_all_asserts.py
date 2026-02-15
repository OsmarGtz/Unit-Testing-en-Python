import unittest

SERVER = 'server_b'

class AllAssertsTest(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola mundo", "Hola mundo")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no soy un numero")

    def test_assert_in_and_not_in(self):
        self.assertIn(3, [1, 4, 5, 2, 53, 3])
        self.assertNotIn(4, [1, 2, 3, 5, 6, 44])

    def test_assert_dicts(self):
        user =  {"First_name" : "Luis", "Last_name" : "Camacho"}
        self.assertDictEqual(
            {"First_name" : "Luis", "Last_name" : "Camacho"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3, 4},
            {1, 2, 3, 4}
        )

    @unittest.skip('Trabajo en progreso, sera habilitada nuevamente')
    def test_skip(self):
        self.assertEqual('hola', 'chao')

    @unittest.skipIf(SERVER == 'server_b', 'saltamos por que no estamos en el servidor correspondiente')
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)