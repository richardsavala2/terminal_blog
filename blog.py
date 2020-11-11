from models.post import Post
import uuid
import datetime


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input('Enter post content')
        content = input('Enter post content')
        data = input('Enter post data, or leave blank for today (format DDMMYYYY):')
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date, '%d%m%Y'))
        post.save_to_mongo()

    def get_posts(self):
        pass
    def save_to_mongo(self):
        pass
    def json(self):
        pass
    def get_from_mongo(self):
        pass