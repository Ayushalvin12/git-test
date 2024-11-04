import unittest
# raise_amt=1.5

from user_email import User

class TestEmail(unittest.TestCase):
    def setUp(self):
        self.user1=User("sam","bdr",10000)

    def test_email(self):
        self.assertEqual(self.user1.email(),'sam.bdr@gmail.com')

    def test_name(self):
        self.assertEqual(self.user1.full_name(),'sam bdr')

    def test_pay(self):
        self.assertEqual(self.user1.apply_raise(),10500)
        