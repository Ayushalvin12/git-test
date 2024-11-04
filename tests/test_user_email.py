import unittest

from user_email import User

# user1=User("Ram","Bdr",20000)
user1=User("Sam","Bdr",10000)


class TestEmail(unittest.TestCase):
    def test_email(self):
        self.assertEqual(user1.email(),'sam.bdr@gmail.com')

    def test_name(self):
        self.assertEqual(user1.full_name(),'Sam Bdr')
        