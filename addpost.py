from database import Database
from models.post import Post

Database.initialize()
post1 = Post(
    blog_id="123",
    title="blog title",
    content="sample content",
    author="richard"
    )

post1.save_to_mongo()