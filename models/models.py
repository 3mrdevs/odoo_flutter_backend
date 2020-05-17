from odoo import fields, models, api

# This python module imports:

# ORM is Object relational mapping which Odoo uses to connect with postgres through psycopg2 lib
# Odoo fields module to implement database columns with a pre-defined sql queries in the ORM module
# Odoo models module to inherit the ORM methods that Odoo uses and create the columns and the behavior
# Odoo api module to access the api annotations of the Odoo ORM methods which each one of them has a purpose,

# Adding books model to store books data.
class Books (models.Model):

    # Holds the name of the table in database
    _name = 'flutter.book'

    # Holds the description of the table in database
    _description = 'Model for storing books and do CRUD operations.'

    # Sorts the categories descending order with the time of creation.
    _order = "create_date desc"

    # Adding a filed (column) for the name of the book. Char is varchar or string with a small length.
    name = fields.Char(required=True)

    # Adding a filed (column) for the activeness of the book which stores true or false to determine
    # if the book is still in stock for sale..
    active = fields.Boolean(default=True)

    # Adding a filed (column) for the number of the book. Integer is a field for numbers.
    number = fields.Integer()

    # Adding a filed (column) for the description of the book which has more string length than char.
    description = fields.Text(required=True)

    # Adding a filed (column) for the image of the book which stores binary data for any file format.
    image = fields.Binary()

    # Adding a filed (column) for the status of the book which stores a string of the current state.
    state = fields.Selection([
        ('draft','Draft'),
        ('waiting','Waiting approval'),
        ('reviewed','Reviewed'),
        ('published','Published'),
    ],default='draft')

    # Adding a filed (column) for the publish date of the book which stores string containing a
    # date format.
    publish_date = fields.Date()

    # Adding a filed (column) for the language of the book which stores string containing the key
    # of the selected option.
    language = fields.Selection([
        ('ar','Arabic'),
        ('en','english')
    ],default='en')

    # Adding a filed (column) for the isbn of the book. Char is varchar or string with a
    # small length. You can use char to store numbers sometime which is more advanced.
    isbn = fields.Char("International Standard Book Number")

    # Adding a filed (column) for the price cost of the book which stores real number.
    price = fields.Float(required=True)

    # Adding a filed (column) for the relation of the author with the book which stores
    # the author id who wrote the book.
    author = fields.Many2one("flutter.author",required=True)

    # Adding a filed (column) for the relation of the publisher with the book which stores
    # the publisher id who published the book of the author.
    publisher = fields.Many2one("flutter.publisher",required=True)

    # Adding a filed (column) for the relation of the categories with the books which stores
    # the categories ids which the admin selected. Note: postgres stores then as ids but odoo
    # display them as lists and when you click on them you can choose what categories you want
    # for this book.
    categories = fields.Many2many("flutter.category")

# Adding author model for book authors.
class Author (models.Model):

    # Holds the name of the table in database
    _name = 'flutter.author'

    # Holds the description of the table in database
    _description = 'Model for storing authors of books and do CRUD operations.'

    # Sorts the authors descending order with the time of registration.
    _order = "create_date desc"

    # Adding a filed (column) for the name of the author. Char is varchar or string with a
    # small length.
    name = fields.Char(required=True)

    # Adding a filed (column) for the image of the author which stores binary data for any
    # file format.
    image = fields.Binary()

    # Adding a filed (column) for the reverse relation of the publisher with the book which
    # stores all the books ids that the publisher had published. Note: postgres stores ids
    # but odoo displays them as a list of books records in his views which is nice.
    books = fields.One2many("flutter.book","author")

# Adding a publisher model to store publishers info
class Publisher (models.Model):

    # Holds the name of the table in database
    _name = 'flutter.publisher'

    # Holds the description of the table in database
    _description = 'Model for storing publishers of books and do CRUD operations.'

    # Sorts the publishers descending order with the time of registration.
    _order = "create_date desc"

    # Adding a filed (column) for the name of the publisher. Char is varchar or string with
    # a small length.
    name = fields.Char()

    # Adding a filed (column) for the image of the publisher which stores binary data for any
    # file format.
    image = fields.Binary()

    # Adding a filed (column) for the reverse relation of the publisher with the book which
    # stores all the books ids that the publisher had published. Note: postgres stores ids but
    # odoo displays them as a list of books records in his views which is nice.
    books = fields.One2many("flutter.book", "publisher")

# Adding a category model to store multiple categories of the published books.
class Category (models.Model):

    # Holds the name of the table in database
    _name = 'flutter.category'

    # Holds the description of the table in database
    _description = 'Model for storing categories of the books and do CRUD operations.'

    # Sorts the categories descending order with the time of creation.
    _order = "create_date desc"

    # Adding a filed (column) for the name of the publisher. Char is varchar or string with
    # a small length.
    name = fields.Char()

    # Adding a filed (column) for the reverse relation of the categories with the books which
    # stores the books ids which the admin selected for the book. Note: postgres stores then
    # as ids but odoo display them as lists and when you click on them you can choose what
    # books you want for this category.
    books = fields.Many2many("flutter.book")