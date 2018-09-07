

class Person:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        

    

    def description(self):
         info = {
            "name": username,
            "email": email,
            
        }
            
       


class User(Person):

    def __init__(self, username, email, password):
        super().__init__(username, email)
        self.username = username
        self.email = email
        self.password = password
        

    def description(self):
        info = {
            "username": username,
            "email": email,
            "password": password
        }
        

    




class Guestlist(User):
    def __init__(self, users = []):
        self.users = users
       
        
        
        
    def add_user(self,username,email,password):
        users = {
            "username": username,
            "email": email,
            "password": password
        }
        self.users.append(users)
        return self.users
     
        
    def get_user(self,username):
        for user in self.users:
            if user['username'] == username:
                return user
            return None
        
        
    def remove_user(self,username):
        for user in self.users:
            if user['username'] == username:
                return self.users.remove(user)
            else:
                return ({'message':'list empty'})


        
        
    def return_all_users(self):
        return self.users

        
    def search_user(self, username):
        user = [user for user in self.users if user['usernamename'] == usernamename]
        if user:
            return user
        return None
                 

    
