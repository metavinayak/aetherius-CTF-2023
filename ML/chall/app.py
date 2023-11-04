import os, json
import uuid
from flask import Flask, make_response, render_template,request,redirect
import random

app = Flask(__name__)
quadrant={}
correct={}
curr_img=''
db = json.load(open('db.json'))
keys= list(db.keys())
def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False
quote="<div style='text-align:center'>Hi, I'm Chandler, I make jokes when I'm uncomfortable.<br>Can you keep guessing the quadrant(s) I am located? Ofcourse, the best way to do it is manually. No Sarcasm.<br><br>Input format: Python list(including the printed spaces)<br>Eg: [1], [2, 4], [1, 2, 3, 4], etc</div>"
@app.route('/')
def home():
    try:
        prev_url=request.referrer # eg: http://xx.yy.zz.pqr:5000/8a0e33af-712e-4e51-b88d-d676d7893430/2
        prev_fold=prev_url.split(':5000/',1)[-1].split('/',1)[0]
        quadrant.pop(prev_fold, None)
        correct[prev_fold]=0
    finally:
        folder= str(uuid.uuid4())
        return redirect('/'+folder+"/1")


@app.route('/<folder>/<int:N>',methods=['GET','POST'])
def page(folder,N):
    global quadrant, curr_img

    if(not is_valid_uuid(folder)):
        return make_response("<a href='/'><h2>No naughty!</h2></a>")
    if(N==1):
        curr_img= keys[random.randint(0,99)] # index from 0 to 99
        quadrant[folder]=db[curr_img]

        correct[folder]=0
        
        response = make_response("<title>Quadrant games</title>"+quote+"<div style='text-align:center'><form action='/"+folder+"/2' method = 'POST'><h3>Input <br> <input type = 'text' name = 'text' style='width: 20%' /></p><input type = 'submit' value = 'submit' /></h3></form><img src='"+"/static/"+curr_img+"'></div>")
        return response
    elif(request.method == "POST" and request.form['text']==str(quadrant[folder])):
        
        print('success')
        ###################
        curr_img = keys[random.randint(0,99)] # index from 0 to 99
        print(curr_img)
        filename= curr_img
        quadrant[folder]=db[curr_img]
        ###############
        # print(quadrant[folder])


        correct[folder]+=1
        # Even though there is no check of index in POST request,
        # It is ensured that quadrant[folder] has been changed to a new value, hence no repetition
        if correct[folder] > 50:
            f = open("flag.txt", 'r').read()
            quadrant.pop(folder, None)
            correct[folder]=0
            return make_response(str(f))

        p = str(int(N)+1)
        response = make_response("<title>Quadrant games</title><div style='text-align:center'><form action='/"+folder+"/"+p+"' method = 'POST'><h3>Input <br> <input type = 'text' name = 'text' style='width: 20%' /></p><input type = 'submit' value = 'submit' /></h3></form><img src='"+"/static/"+curr_img+"'></div>")
        response.headers['Refresh'] = '10; url=/' # Redirect after x seconds if no response
        return response
    else:
        # print()
        # print(quadrant[folder],' is correct!')
        # print(request.form['text'] , 'is wrong')
        # print('Image name:', curr_img)
        # print()
        correct[folder]=0
        quadrant.pop(folder, None)
        return redirect('/')

@app.route('/<path:url>/',methods=['GET','POST'])
def other_pages(url):
    return make_response("<a href='/'><h2>No naughty!</h2></a>")


app.run(port=5000,debug=False,host='0.0.0.0') 