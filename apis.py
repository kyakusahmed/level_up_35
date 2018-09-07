

from flask import Flask, jsonify, request, json

app2 = Flask(__name__)

users = [{"username":"kyakulumbyeahmad", "email":"kyakusahmed@outlook.com", "password":"1234"}, 
 {"username":"johnpaul","email":"jpeter@outlook.com","password":"54321"}, 
{"username":"simonpeter","email":"spaul@gmail.com","password":"098765"}]


@app2.route('/users',methods = ['GET'])
def returnALL():
    alternative = "list is empty"
    if users != None:
        return jsonify({'users':users}),200
    else:
        return jsonify("list empty")   
   
    
@app2.route('/users',methods = ['POST'])
def addOne():
    user1 = {'username' : request.json['username'], 'email':request.json['email'], 'password':request.json['password']}
   
    for user in users:
        if user1 in users:
            return jsonify({'message':'user exists'})
    else:
        users.append(user1)
        return jsonify({'users' : user1}),201

        
@app2.route('/users/<username>', methods = ['DELETE'])
def removeOne(username):
    user2 = [user for user in users if user['username'] == username ]
    if user2:
        users.remove(user2[0])
        return jsonify({'users':user2}),404
    else:
        return  jsonify({'message':'user not found'})
         
if __name__ =="__main__":
    app2.run(debug=True,port = 8080)
    
