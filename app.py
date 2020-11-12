from blog import Blog
from database import Database

Database.initialize()

blog = Blog(author='rick',
            title='i\'m not easily impressed',
            description='woah a blue car!')

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
