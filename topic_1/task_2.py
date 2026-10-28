import unittest
 
 
class TestStringMethods(unittest.TestCase):
    def test_strip(self):
        self.assertEqual("   hello world  ".strip(), "hello world")
        self.assertEqual("\n\t text \t\n".strip(), "text")
        self.assertEqual("xxhixx".strip("x"), "hi")
        self.assertEqual("".strip(), "")
 
    def test_capitalize(self):
        self.assertEqual("hello world".capitalize(), "Hello world")
        self.assertEqual("HELLO".capitalize(), "Hello")
        self.assertEqual("123abc".capitalize(), "123abc")
        self.assertEqual("".capitalize(), "")
 
    def test_title(self):
        self.assertEqual("hello world".title(), "Hello World")
        self.assertEqual("hELLO wORLD".title(), "Hello World")
        self.assertEqual("python is fun".title(), "Python Is Fun")
        self.assertEqual("".title(), "")
 
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")
        self.assertEqual("Hello World 123".upper(), "HELLO WORLD 123")
        self.assertEqual("привіт".upper(), "ПРИВІТ")
        self.assertEqual("".upper(), "")
 
    def test_lower(self):
        self.assertEqual("HELLO".lower(), "hello")
        self.assertEqual("Hello World 123".lower(), "hello world 123")
        self.assertEqual("ПРИВІТ".lower(), "привіт")
        self.assertEqual("".lower(), "")
 
 
if __name__ == "__main__":
    unittest.main(verbosity=2)