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
post = Post.from_mongo("68e65e96964a430b82d084c83aea4fdf")
print(post)
print(Database.DATABASE["posts"].find({"blog_id": "123"}))
print(Database.DATABASE["posts"].find_one({id: "68e65e96964a430b82d084c83aea4fdf"}))