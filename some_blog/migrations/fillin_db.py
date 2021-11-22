import random
import string

import names
from sqlalchemy import func
from sqlalchemy.orm.exc import FlushError

from some_blog.models import Author, Article, Tag, DB


if __name__ == '__main__':
    db = DB()
    migration = db.maker()

    # add tags
    with open("tags.txt", mode="r") as f:
        text = f.read()
        tags = list(map(str, text.split()))

    for i in tags:
        Tag.create(migration, name=i)

    # add authors
    authors_count = 100

    authors_total = migration.query(func.count(Author.id)).scalar()
    for i in range(authors_count - authors_total):
        author = Author.create(migration, name=names.get_full_name())

        # add article
        articles_count = random.randint(50, 100)
        while articles_count:
            article = Article.create(migration, subject=str(''.join(random.sample(string.ascii_lowercase, 25))),
                                     data=str(''.join(random.sample(string.ascii_lowercase, 25))),
                                     author_id=author.id)
            articles_count -= 1

    # add tags to the article
    article_tags_count = 3
    count = 0
    while True:
        try:
            while article_tags_count:
                article = migration.query(Article).offset(count).first()

                tag = migration.query(Tag).order_by(func.random()).first()
                art = tag.articles.append(article)
                migration.commit()

                article_tags_count -= 1

            count += 1
            article_tags_count = 3
        except FlushError:
            break

    migration.close()
