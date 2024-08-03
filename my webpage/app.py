from flask import Flask,request,render_template,redirect, url_for ,flash
from sqlalchemy.orm import sessionmaker
from create_db import  User , engine 
from blog import Blog , blog_engine 
app = Flask(__name__)

app.secret_key='3913265aada78f2803c1071898e50055'
Session = sessionmaker(bind=engine)
session = Session()

Blog_Session2 = sessionmaker(bind=blog_engine)
session2 = Blog_Session2()

@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="POST":
        username = request.form["username2"]
        email = request.form["email2"]
        password = request.form["password2"]
        password2 = request.form["verify_password"]
        new_user = User(name=username,email=email,password=password)
        user = session.query(User).filter_by(name=username).first()
        
        
        if user is None:
            if password == password2:
                session.add(new_user)
                session.commit()
                return render_template("login.html")
                
                
            else:
                flash("Password Do not match")
                return redirect(url_for("index"))
        else:
            flash("Account already exist")
            return redirect(url_for("index"))
        
        
    return render_template("create_account.html")


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        user = session.query(User).filter_by(name=username,email=email,password=password).first()
        
        if user is None:
            flash("Invalid login Check Your details")
            flash("Or Create an account")
            return redirect(url_for("login"))
        else:
            return render_template("home.html")
        
    return render_template("login.html")

@app.route("/home")
def home():
    posts = session2.query(Blog).all()
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method == "POST":
        flash("Feedback successfully sent :)")
        return redirect(url_for("contact"))
    return render_template("contact.html")
@app.route("/blog" , methods = ["GET","POST"])
def blog():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_post = Blog(title=title,content=content)
        
        session2.add(new_post)
        session2.commit()
        return redirect(url_for("home"))
    return render_template("blog.html")

@app.route("/delete/<int:id>")
def delete(id):
    
    content_to_delete = session2.query(Blog).get(id)
    
    try:
        session2.delete(content_to_delete)
        session2.commit()
        return redirect("/home")
    except:
        return "There was a problem deleting that task"
    
    
    
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    update = session2.query(Blog).get(id)
    if request.method == "POST":
        update.title = request.form["title"]
        update.content = request.form["content"]
        
        session2.commit()
        return redirect("/home")
    else:
        return render_template("update.html",update=update)
if __name__ == "__main__":
    app.run(debug=True)


session.rollback()