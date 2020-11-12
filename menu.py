from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input('Enter your name: ')
        self.user_blog = None
        if self._user_has_account():
            print('Welcome back {}'.format(self.user))
        else:
            self._prompt_user_for_account()

    def user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user}) is not None
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input('Enter blog desription:' )
        description = input('Enter blog desccription: ')
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input('Do you want to read (R) or write (W) blogs?: ')
        if read_or_write == 'R':
        #       list blogs in database
        #       allow user to pick one
        #       display post
        elif read_or_write == 'W':
        #       if not, prompt to write new blog
        else:
            print('Thank you, blog again!')
