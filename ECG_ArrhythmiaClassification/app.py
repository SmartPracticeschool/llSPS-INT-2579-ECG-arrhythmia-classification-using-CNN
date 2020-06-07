

from flask import Flask , render_template,request
app=Flask(__name__)
import pickle
fom sklearn.preprocessing import StandardScaler
model=pickle.load(open('profit.pkl','rb'))
@app.route('/')
def helloworld():
    return render_template("index.html")
@app.route('/login',methods=['POST'])
def admin():
    p=request.form["ms"]
    q=request.form["ad"]
    r=request.form["rd"]
    s=request.form["s"]
    if(s=="California"):
        s1,s2,s3=1,0,0
    if(s=="Florida"):
        s1,s2,s3=0,1,0
    if(s=="New York"):
        s1,s2,s3=0,0,1
        
    t=[[int(s1),int(s2),int(s3),int(r),int(q),int(p)]]
    y=model.predict((t))
    return render_template("index.html",y ="the profit would be:"+str(y[0])[0]))

@app.route('/user')
def user():
    return "hieee user"

if __name__ == '__main__':
    app.run(debug = True)
