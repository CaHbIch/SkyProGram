from dao.models.post import Bookmark, Post


class BookmarksDAO:

    def __init__(self, session):
        self.session = session

    def get_bookmarks(self):
        """Возращает все закладки"""
        return self.session.query(Bookmark).all()

    def get_bookmark_by_post_id(self, post_id):
        """ Возвращает закладку по id"""
        return self.session.query(Bookmark).filter(Bookmark.post_id == post_id).first()

    def add_bookmark(self, post_id: int):
        """ Добавляет закладку"""
        bookmark = Bookmark(post_id=post_id)
        self.session.add(bookmark)
        self.session.commit()

    def del_bookmark(self, post_id):
        """ Удаляет закладку"""
        bookmark = self.session.query(Bookmark).filter(Bookmark.post_id == post_id).first()
        self.session.delete(bookmark)
        self.session.commit()
