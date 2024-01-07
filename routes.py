# app/routes.py

from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    video_names = ["bubbleshooter", "minesweeper"]
    
    return render_template('index.html', title="Home", video_names=video_names)

@bp.route('/about')
def about():
    return render_template('about.html', title="About")

@bp.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@bp.route('/projects')
def projects():

    posts = [
        {
        "name" : "minesweeper",
        "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "personal_overview" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "video" : {"name" : "minesweeper.mp4",
                   "type" : "video/mp4"}
    },  {
        "name" : "minesweeper",
        "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "personal_overview" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "video" : {"name" : "bubbleshooter.mp4",
                   "type" : "video/mp4"}
    }]  


    return render_template('projects.html', title="Projects", posts=posts)


@bp.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")





@bp.route('/minesweeper')
def minesweeper():
    return render_template('projects/minesweeper.html', title="Minesweeper", post="minesweeper")

@bp.route('/bubbleshooter')
def bubbleshooter():
    return render_template('projects/bubbleshooter.html', title="Bubbleshooter", post="bubbleshooter")


# More route definitions...
