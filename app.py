from database import Database
from models.post import Post

Database.initialize()

blog = Blog(author='rick',
            title='i\'m not easily impressed',
            description='woah a blue car!')

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts()
