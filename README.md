# Python-Flask-Code---Sample1
This the my first sample project about flask. You can get idea here about how flask runs on our brower, some functions and how does it work. 
On this program,we have 3 functions, first is to display our greetings, the other 2 is to display employees and specific employee data stored in our local database inside the pyrhon code.

## SET UP
### TO RUN THIS PROGRAM:

1. go to your cmd and then enter this command : 'pip install flask' in your directory
   #### note: if you are using an IDE, just go the the terminal and enter the command


## RUN

### TO RUN THIS PROGRAM:

1 You can just run it directly to your IDE or

2. Go to your cmd and enter the command: 'python main.py' make sure that you are in the right directory on when you save the main.py

#### OUTPUT OF THE PROGRAM:
* Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## RUN

### TO SEE THE RUNNING OUTPUT IN THE BROWSER:

1. Click or paste the linke provided by your code --> #### http://127.0.0.1:5000/ 
 
2. you will be redirected on the on our first page where our first function located

#### web browser output:
![](https://github.com/RupertCaingal/Python-Flask-Code---Sample1/blob/main/pf1.png)

### Now that our code is running, you will notice on our code that we have 2 other  url :'/empDB/employee/'(2), '/empDB/employee/<empId>'(3). all you need to do is extend our local url with these 2 urls separately

Here is the example : http://127.0.0.1:5000/empDB/employee/
#### We are getting all the employees data here.For your reference here's uour local databse inside the python code : 

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




#### web browser output:
![](https://github.com/RupertCaingal/Python-Flask-Code---Sample1/blob/main/pf2.png)




Another example  : http://127.0.0.1:5000/empDB/employee/101
#### 101 is the id of the data we want to fetch
#### So, just type the id to get those specific record 


#### web browser output:
![](https://github.com/RupertCaingal/Python-Flask-Code---Sample1/blob/main/pf3.png)








## ALL DONE

That's it, I hope this sample flask program will help you to have an idea on how python flask and basic functions of it works.
Kepp on motivating yourself, keep on practicising, keep on learning. 

### See you around on my next sample projects, peace!!

