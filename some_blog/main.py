from some_blog import models


if __name__ == '__main__':
    session = models.start_session

    print(models.Author.get_author_tags(session, author_name="Jack Travis"))
    print(models.Tag.get_tag_authors(session, tag_name="hunter"))
