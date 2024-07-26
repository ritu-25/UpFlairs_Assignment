from flask import Flask,render_template,url_for,request
import sqlite3
#conn =  sqlite3.connect("userdata.db")



app = Flask(__name__)  #  object 

@app.route('/')   # http://127.0.0.1:5000/
def home():
    return render_template('home.html')



@app.route('/about')  # http://127.0.0.1:5000/about
def about():
    return render_template('about.html')



@app.route('/services')  # http://127.0.0.1:5000/about
def services():
    return render_template('services.html')



# @app.route('/contact')  # http://127.0.0.1:5000/about
# def contact():
#     return render_template('contact.html')



@app.route('/query')  # http://127.0.0.1:5000/about
def query():
    return render_template('query.html')




@app.route('/user_query',methods=['GET','POST'])
def user_query():
    if request.method == "POST": 
        #conn =  sqlite3.connect("userdata.db")

        name = request.form['name']
        age = int(request.form['age'])
        address = request.form['address']
        college = request.form['college']
        branch = request.form['branch']
        roll_no = int(request.form['roll_no'])
        query_sub = request.form['query_sub']

        user_data = (name,age,address,college,branch,roll_no,query_sub)
        ## database 
        conn =  sqlite3.connect("userdata.db")

        insert_data_query = """
        insert into userecord values(?,?,?,?,?,?,?)
        """
        cur = conn.cursor()
        cur.execute(insert_data_query,user_data)
        print("You have successfully inserted your data into table : ",user_data)
        conn.commit()
        cur.close()
        conn.close()

        return  "Your data is Submitted into the data base!"





if __name__ == "__main__":
    app.run(host="0.0.0.0",debug= True)