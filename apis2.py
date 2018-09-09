

from flask import Flask, jsonify, request, json

from oop2 import Guestlist


app2 = Flask(__name__)
users =Guestlist()


@app2.route('/users',methods = ['GET'])
def return_all( ):
   return jsonify({'users': users.return_all_users()}),200

   
    
@app2.route('/users',methods = ['POST'])
def addone():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    return jsonify({'users' : users.add_user(username, email, password)}),201



        
@app2.route('/users/<username>', methods = ['DELETE'])
def remove_one(username):
    return jsonify({'users':users.remove_user(username)}),404
    
         
if __name__ =="__main__":
    app2.run(debug=True,port = 8080)
    
