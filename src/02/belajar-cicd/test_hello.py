import unittest
import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('Hello, budi', hello.hello('budi'))

    def test_empty_name_should_print_hello_world(self):
        self.assertEqual('Hello, world', hello.hello(''))
        self.assertEqual('Hello, world', hello.hello())
