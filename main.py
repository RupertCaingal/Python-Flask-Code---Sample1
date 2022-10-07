from flask import Flask,jsonify,request


app = Flask(__name__)

empDB = [
    {
        'id' : '101',
        'name' : 'Dory Britz',
        'title' : 'Technical Leader'
    },
    {
        'id' : '102',
        'name' : 'Barbie Gurl',
        'title' : 'Software Engineer'


    }
]

@app.route("/")
def greetings():
    return "HELLO PYTHON WORLD!!!"

@app.route('/empDB/employee/', methods = ['GET'])
def getAllEmp():
    return jsonify({'emp' : empDB})


@app.route('/empDB/employee/<empId>', methods = ['GET'])
def getEmp(empId):
    usr = [emp for emp in empDB if(emp['id'] == empId)]
    return jsonify({'emp' : usr})

if __name__ == '__main__':
    app.run()
