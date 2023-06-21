from flask import Flask, render_template
import sqlite3

from werkzeug.exceptions import abort

app = Flask(__name__)


def get_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


def get_all_posts():
    connection = get_connection()
    posts = connection.execute("SELECT * FROM posts").fetchall()
    connection.close()
    return posts


def get_post_by_id(post_id):
    connection = get_connection()
    post = connection.execute("SELECT * FROM posts WHERE id=?", (post_id,)).fetchone()
    connection.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def main_page():
    posts = get_all_posts()
    return render_template("main_page.html", posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post_by_id(post_id)
    return render_template("post.htm", post=post)


app.run()