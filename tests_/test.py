


import unittest
from signup import SignUp



class SignUpTest(unittest.TestCase):
     
     
    def setUp(self):
        self.signup = SignUp()
        self.signup.add_user("ahmad","kyakusahmed@outlook.com","12345")



    def test_SignUp_class(self):
        self.assertIsInstance(self.signup, SignUp)


    def test_add_user(self):
        
        self.assertEqual(self.signup.add_user("jon","kyakusahmed@gmail.com","4321"),[{"name": 'ahmad',"email": 'kyakusahmed@outlook.com',"password": '12345'},
        {"name": 'jon',"email": 'kyakusahmed@gmail.com',"password": '4321'}])
        self.assertEqual(len(self.signup.user_bio), 2)

    def test_get_user(self):
        self.assertEqual(self.signup.get_user('ahmad'),{'name':"ahmad",'email':"kyakusahmed@outlook.com",'password':"12345"})

    def test_remove_user(self):
        self.signup.remove_user('12345')
        self.assertEqual(len(self.signup.user_bio),0)

    def test_user_not_found(self):
        self.assertIsNone(self.signup.get_user("james@gmail.com"))

    def test_length_of_user_bio(self):
        self.assertEqual(len(self.signup.user_bio),1) 

    def tearDown(self):
        self.signup.user_bio = []


    
        



        

           



