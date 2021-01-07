"""
   Validators for classes
"""
from datetime import datetime
def title_validator(titl):
    """
        Validate title
    """
    return len(titl) < 50 and not titl.isspace()

def author_validator(author):
    """
        Validate authors name
    """
    if len(author) < 100 and not author.isspace():
        return True
    print("Nevalidan unos!")
    return False

def desc_validator(desc):
    """
        Validate description - up to 500 characters
    """
    if len(desc) == 0 or len(desc) > 500:
        print("Nevalidan unos!")
        return False
    return True

def category_validator(kat):
    """
        Validate category
    """
    if 0 > len(kat) > 20:
        print("Nevalidan unos!")
        return False
    return True

def date_validator(date):
    """
        Validate date
    """
    try:
        datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        print("Pogrešan format, format treba da bude oblika dd/mm/GGGG")
        return False
def lang_validator(lang):
    """
        Validate language
    """
    return lang in ('en', 'rs')

def views_validator(views):
    """
        Validate views count
    """
    try:
        int(views)
    except ValueError:
        print("Nevalidan unos!")
        return False
    return True
