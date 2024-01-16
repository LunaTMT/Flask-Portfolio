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
    return render_template('projects.html', title="Projects")


@bp.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")


@bp.route('/load_project/<project_name>')
def load_project(project_name):
    projects = {"pacman" :  {
                                "video_name"  : "pacman",
                                "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam hendrerit, ante eget tempor luctus, est ligula pretium sem, eu rhoncus elit tortor non quam. Vestibulum tristique lacus ac enim interdum, auctor convallis justo aliquam. Integer auctor odio id nulla varius, non ullamcorper velit tempus.",
                                "overview"    : "Morbi nec congue sapien. Vivamus eleifend odio et lacus pellentesque fermentum. Quisque id accumsan leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut sit amet eleifend odio.",
                                "devlog"      :  False,
                                "tutorial"    :  False},
                "bubbleshooter" : {
                                "video_name"  : "bubbleshooter",
                                "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam hendrerit, ante eget tempor luctus, est ligula pretium sem, eu rhoncus elit tortor non quam. Vestibulum tristique lacus ac enim interdum, auctor convallis justo aliquam. Integer auctor odio id nulla varius, non ullamcorper velit tempus.",
                                "overview"    : "Morbi nec congue sapien. Vivamus eleifend odio et lacus pellentesque fermentum. Quisque id accumsan leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut sit amet eleifend odio.",
                                "devlog"      :  False,
                                "tutorial"    :  True},

                "knights tour": {
                                "video_name"  : "knights tour",
                                "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam hendrerit, ante eget tempor luctus, est ligula pretium sem, eu rhoncus elit tortor non quam. Vestibulum tristique lacus ac enim interdum, auctor convallis justo aliquam. Integer auctor odio id nulla varius, non ullamcorper velit tempus.",
                                "overview"    : "Morbi nec congue sapien. Vivamus eleifend odio et lacus pellentesque fermentum. Quisque id accumsan leo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut sit amet eleifend odio.",
                                "devlog"      :  True,
                                "tutorial"    :  True}
                }

 

    return render_template('load_project.html', title=project_name.title() , content=projects[project_name])
    


