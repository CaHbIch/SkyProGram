from flask import Blueprint, render_template, redirect

from implemented import bookmarks_services

bookmarks = Blueprint('bookmarks', __name__, template_folder="templates")


@bookmarks.route("/bookmarks/")
def all_bookmark():
    """Выводит все добавленые закладки"""
    bookmark = bookmarks_services.get_all_bookmarks()  # Возращает все добавленые закладки
    return render_template("bookmarks.html", all_bookmarks=bookmark)


@bookmarks.route("/bookmarks/add/<post_id>/")
def bookmarks_add_post(post_id):
    """ Добавляет посты в закладки."""
    bookmarks_services.add_bookmarks(post_id)
    return redirect("/", code=302)


@bookmarks.route('/bookmarks/delete/<int:post_id>')
def page_bookmarks_delete(post_id):
    """  Удаляет посты из закладок"""
    bookmarks_services.del_bookmark(post_id)
    return redirect("/", code=302)
