""" seed.py """
from main import session
from models import Model, User, AuthorProfile, Blog, BlogAuthor, Comment


users = [
    {
        "id": 1,
        "name": "John Dillons",
        "age": 25,
    },
    {
        "id": 2,
        "name": "James Smith",
        "age": 25,
    },
    {
        "id": 3,
        "name": "Alex Shmoe",
        "age": 25,
        
    },
    {
        "id": 4,
        "name": "Rob Scramble",
        "age": 25,
        
    },
    {
        "id": 5,
        "name": "Maxwell Amadeous",
        "age": 25,
        
    }
]

authors = [
    {
        "id": 1,
        "display_name": "Ashmoe28",
        "user_id": 3
    },
    {
        "id": 2,
        "display_name": "Mamadeous7",
        "user_id": 5
    },
    {
        "id": 3,
        "display_name": "JSmith11",
        "user_id": 2,
    },
]

blogs = [
    {
        "id": 1,
        "title": "Beginner Django Tutorial",
        "tagline": "How to get started with django",
        "content": "Mollit culpa aute labore dolore quis eu pariatur esse consequat. Excepteur proident sint aliqua pariatur cupidatat exercitation non anim consectetur. Irure magna mollit irure velit sint veniam enim. Ullamco culpa laboris ullamco cillum tempor sit Lorem non. Mollit voluptate magna laborum ipsum. Adipisicing amet ipsum minim eiusmod exercitation irure duis culpa labore proident. Magna laborum id reprehenderit enim laborum exercitation eu."
    },
    {
        "id": 2,
        "title": "Beginner Flask Tutorial",
        "tagline": "How to get started with flask",
        "content": "Mollit culpa aute labore dolore quis eu pariatur esse consequat. Excepteur proident sint aliqua pariatur cupidatat exercitation non anim consectetur. Irure magna mollit irure velit sint veniam enim. Ullamco culpa laboris ullamco cillum tempor sit Lorem non. Mollit voluptate magna laborum ipsum. Adipisicing amet ipsum minim eiusmod exercitation irure duis culpa labore proident. Magna laborum id reprehenderit enim laborum exercitation eu."
    },
    {
        "id": 3,
        "title": "Machine Learning Tutorial",
        "tagline": "How to get started with machine learning with python",
        "content": "Mollit culpa aute labore dolore quis eu pariatur esse consequat. Excepteur proident sint aliqua pariatur cupidatat exercitation non anim consectetur. Irure magna mollit irure velit sint veniam enim. Ullamco culpa laboris ullamco cillum tempor sit Lorem non. Mollit voluptate magna laborum ipsum. Adipisicing amet ipsum minim eiusmod exercitation irure duis culpa labore proident. Magna laborum id reprehenderit enim laborum exercitation eu."
    },
    {
        "id": 4,
        "title": "SQL Tutorial",
        "tagline": "Querying databases with SQL",
        "content": "Mollit culpa aute labore dolore quis eu pariatur esse consequat. Excepteur proident sint aliqua pariatur cupidatat exercitation non anim consectetur. Irure magna mollit irure velit sint veniam enim. Ullamco culpa laboris ullamco cillum tempor sit Lorem non. Mollit voluptate magna laborum ipsum. Adipisicing amet ipsum minim eiusmod exercitation irure duis culpa labore proident. Magna laborum id reprehenderit enim laborum exercitation eu."
    },
]

blog_authors = [
    {
        "id": 1,
        "author_profile_id": 2,
        "blog_id": 1, 
    },
    {
        "id": 2,
        "author_profile_id": 3,
        "blog_id": 4, 
    },
    {
        "id": 3,
        "author_profile_id": 1,
        "blog_id": 2, 
    },
    # {
    #     "id": 4,
    #     "author_profile_id": 3,
    #     "blog_id": 4, 
    # },
]

comments = [
    {
        "id": 1,
        "blog_id": 1,
        "text": "Love it!"

    },
    {
        "id": 2,
        "blog_id": 1,
        "text": "Can't wait for more!"

    },
    {
        "id": 3,
        "blog_id": 2,
        "text": "Can't wait for your next tutorial!"

    },
    {
        "id": 4,
        "blog_id": 2,
        "text": "Love it!"

    },
    {
        "id": 5,
        "blog_id": 2,
        "text": "Great Post!"

    },
    {
        "id": 6,
        "blog_id": 3,
        "text": "Not really a fan of this one!"

    },
    {
        "id": 7,
        "blog_id": 4,
        "text": "Very good post!"

    },
]

def seed_db():
    """ seed our sqlite database with sample data defined above """
    data = [(users, User), (authors, AuthorProfile), (blogs, Blog), 
            (blog_authors, BlogAuthor), (comments, Comment)]
    for objects, model in data:
        for obj in objects:
            session.add(model(**obj))
        session.commit()


if __name__ == "__main__":
    seed_db()