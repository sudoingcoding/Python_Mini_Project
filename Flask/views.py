from flask import Blueprint,render_template,request,jsonify,redirect,url_for

main =Blueprint("main",__name__)

@main.route("/")
def home():
    country=request.args.get("country")
    source=request.args.get("source")
    
    return render_template("index.html",country=country,source=source)

@main.route("/about")
def about():
    context={
        "username":"Suddip",
        "subject":"Python"
    }
    return render_template("about.html",context=context)

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/portfolio")
def portfolio():
    projects_list=[
        {'name':'Codebook','description':'This is the first project','endpoint':'codebook'},
        {'name':'Taskmate','description':'This is the second project','endpoint':'taskmate'}
    ]
    return render_template("portfolio.html",projects_list=projects_list)

@main.route("/portfolio/<project>")
def project(project):
    projects_lst=["taskmate","codebook"]
    if project in projects_lst:
        return render_template(f"portfolio/{project}.html")
    else:
        return redirect("/404")


@main.route("/s")
def search():
    keyword=request.args.get("k")
    return f"{keyword}"

@main.route("/portfolio/json")
def portfolio_json():
    projects = {
        "taskmate":{
            "language":"python",
            "framework":"django",
            "status":"completed"
            },
        "codebook":{
            "language":"javascript",
            "framework":"react",
            "status":"learning"
        }
    }
    return jsonify(projects)

@main.route('/404')
def not_found_404():
    return render_template("404.html"),404

@main.app_errorhandler(404)
def pg_not_found(e):
    return render_template("404.html"),404

@main.route('/about_us')
def about_us():
    return redirect(url_for("main.about"))