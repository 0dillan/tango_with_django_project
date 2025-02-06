import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

import django
django.setup()

from rango.models import Category, Page

def populate():
    # Example pages
    python_pages = [
        {"title": "Official Python Tutorial", "url": "http://docs.python.org/3/tutorial/"},
        {"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/3/thinkpython/"},
        {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial", "url": "https://docs.djangoproject.com/en/2.1/intro/tutorial01/"},
        {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask", "url": "http://flask.pocoo.org/"}
    ]

    # Example Categories
    categories = {
        "Python": {"pages": python_pages},
        "Django": {"pages": django_pages},
        "Other Frameworks": {"pages": other_pages}
    }

    # Creates every category object and associates all the relevant pages to it
    for category_name, category_data in categories.items():
        category = add_category(category_name)

        for page in category_data["pages"]:
            add_page(category, page["title"], page["url"])

    # Prints every page in every category
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(f"- {category}: {page}")

def add_category(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.save()

    return category

def add_page(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category, title=title)[0]
    page.url = url
    page.views = views
    page.save()

    return page

# Start of code execution when not imported
if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()