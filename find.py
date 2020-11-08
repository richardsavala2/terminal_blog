from database import Database
from models.post import Post

Database.initialize()

post = Post.from_mongo('68e65e96964a430b82d084c83aea4fdf')

print(post)