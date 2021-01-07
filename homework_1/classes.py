"""
    Classes examples
"""
import services as validators
class Article:
    """
        Article main class
    """
    #pylint: disable=too-many-arguments
    def __init__(self, title, author, description, category, views = 0):
        self.__title = title
        self.__author = author
        self.__description = description
        self.__category = category
        self.__views = views
    def set_title(self, titl):
        '''
            Title setter
        '''
        if  validators.title_validator(titl) == 1:
            self.__title = titl
            print(self.__title)
    def set_author(self, autor):
        '''
            Author setter
        '''
        if  validators.author_validator(autor) == 1:
            self.__author = autor
    def set_desc(self, desc):
        '''
            Description setter
        '''
        if  validators.desc_validator(desc) == 1:
            self.__description = desc
    def set_category(self, kat):
        '''
            Category setter
        '''
        if  validators.category_validator(kat) == 1:
            self.__category = kat
    def set_views(self, pregled):
        '''
            Views setter
        '''
        if validators.views_validator(pregled) == 1:
            self.__views = pregled
    def get_title(self):
        '''
            Title getter
        '''
        return self.__title
    def get_author(self):
        '''
            Author getter
        '''
        return self.__author
    def get_desc(self):
        '''
            Description getter
        '''
        return self.__description
    def get_category(self):
        '''
            Category getter
        '''
        return self.__category
    def get_views(self):
        '''
            Views getter
        '''
        return self.__views
    def inc_views(self, number = 0):
        '''
            Increment views by number
        '''
        if validators.desc_validator(number):
            self.__views = self.__views + number
    def __str__(self):
        '''
            Get class info as string
        '''
        diction = {
                    'title':self.__title,
                    'author':self.__author,
                    'description':self.__description,
                    'category':self.__category,
                    'views':self.__views
                }
        stri = str(diction)[1:len(str(diction)) - 1]
        return stri

class TechArticle(Article):
    """
        Article subclass with default category
    """
    #pylint: disable=too-many-arguments
    def __init__(
                    self,
                    title,
                    author,
                    description,
                    creation_date,
                    lang,
                    views = 0,
                    category = 'Tech'
                ):
        super().__init__(title, author, description, category, views)
        self.__creation_date = creation_date
        self.__lang = lang
    def set_creation_date(self, date):
        '''
            Date setter
        '''
        if validators.date_validator(date):
            self.__creation_date = date
    def set_lang(self, lang):
        '''
            Language setter
        '''
        if validators.lang_validator(lang):
            self.__lang = lang
    def get_creation_date(self):
        '''
            Date getter
        '''
        return self.__creation_date
    def get_lang(self):
        '''
            Language setter
        '''
        return self.__lang
    def __str__(self):
        '''
            Get class info as string
        '''
        diction = {
                    'creation_date': self.__creation_date,
                    'lang': self.__lang
                    }
        stri = str(diction)[1:len(str(diction)) - 1]
        return super().__str__() + ', ' + stri

articles_list = []
categories_list = ["Tech", "Culture", 'World']
ARTICLES_COUNT = 0
while True:
    while True:
        category_input = input(f"Unesite neku od kategorija {categories_list}:\n")
        if categories_list.count(category_input):
            break
        print('Nevalidan unos!')
    while True:
        title_input = input('Unesite titl vaseg artikla (od 1-50 slova):\n')
        if validators.title_validator(title_input):
            break
    while True:
        author_input = input('Unesite ime autora (od 1-100 slova):\n')
        if validators.author_validator(author_input):
            break
    while True:
        description_input = input('Unesite opis (od 1-500 karaktera):\n')
        if validators.desc_validator(description_input):
            break
    while True:
        views_input = input('Unesite broj pregleda (nije obavezno):\n')
        if validators.views_validator(views_input):
            break
    if category_input != "Tech":
        articles_list.append(Article(
                                        title_input,
                                        author_input,
                                        description_input,
                                        category_input,
                                        views_input
                                    ))
    else:
        articles_list.append(TechArticle(
                                            title_input,
                                            author_input,
                                            description_input,
                                            '',
                                            '',
                                            views_input
                                        ))
        while True:
            date_input = input("Unesite datum kreacije u obliku dd/mm/yyyy:\n")
            if not validators.date_validator(date_input):
                print("Nevalidan unos!")
            else:
                articles_list[ARTICLES_COUNT].set_creation_date(date_input)
                break
        while True:
            lang_input = input("Unesite neki od jezika (en, rs):\n")
            if not validators.lang_validator(lang_input):
                print("Nevalidan unos!")
            else:
                articles_list[ARTICLES_COUNT].set_lang(lang_input)
                break
    ARTICLES_COUNT += 1
    if input("Da li zelite da unesete jos artikala? y/n \n") != 'y':
        break

for elem in articles_list:
    print('Naslov - ', elem.get_title())
    print('Autor - ', elem.get_author())
    print('Opis - ', elem.get_desc())
    print('Pregledi - ', elem.get_views())
    print('Kategorija - ', elem.get_category())
    if elem.get_category() == "Tech":
        print ('Kreirano - ', elem.get_creation_date())
        print('Jezik - ', elem.get_lang())
    print('\n')


with open("articles.txt", "w", encoding="utf-8") as f:
    for elem in articles_list:
        f.write(elem.__str__() + '\n')
