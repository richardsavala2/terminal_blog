from database import Database
from models.post import Post

Database.initialize()

post = Post.from_mongo('9fcf707e9ed640ed9b8eaab18fbb363e')

print(post)