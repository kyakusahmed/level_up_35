
class SignUp:
    
    def __init__(self):
        self.user_bio = []



    def add_user(self,name,email,password):
        
        user = {
            "name": name,
            "email": email,
            "password": password
        }

        self.user_bio.append(user)
        return self.user_bio

    
    def get_user(self,name):
        for user in self.user_bio:
            if user['name'] == name:
                return user
        return None

    def remove_user(self,password):
        for user in self.user_bio:
            if user['password'] == password:
                self.user_bio.remove(user)

   
                
        

       