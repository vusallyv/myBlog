from flask import render_template, redirect, request, url_for
from app import app
from models import Blog
from forms import Blog_info


active = True

@app.route("/blogs")
def blogs():
    blogs = Blog.query.all()
    return render_template('blog1.html', blogs=blogs, a=active)


@app.route("/", methods=['GET', 'POST'])
def blog():
    post_data=request.form
    form = Blog_info()
    form = Blog_info(data=post_data)
    if request.method=='POST':
        if form.validate_on_submit():
            user = Blog(title=form.title.data, description=form.description.data)
            user.save()
            return redirect(url_for("blogs"))

    return render_template('blog.html', form=form, a=active)


@app.route("/blogs/<int:book_id>")
def blog_ids(book_id):
    blogs = Blog.query.get(book_id)
    return render_template('blog2.html', blogs=blogs, a=active)