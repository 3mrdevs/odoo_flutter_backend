from odoo import fields, models, api


class Books (models.Model):
    _name = 'flutter.book'
    _description = 'Model for storing books and do CRUD operations.'

    # name of the book. Char is varchar or string with a small length.
    name = fields.Char()

    # active is to determine if the book available or not. Boolean is true or false value.
    active = fields.Boolean(default=True)

    # Adding a filed (column) for the number of the book. Integer is a field for numbers.
    number = fields.Integer()

    # Adding a filed (column) for the description of the book which has more string length than char.
    description = fields.Text()

    # Adding a filed (column) for the image of the book which stores binary data for any file format.
    image = fields.Binary()

    # Adding a filed (column) for the status of the book which stores a string of the current state.
    state = fields.Selection([
        ('draft','Draft'),
        ('waiting','Waiting approval'),
        ('reviewed','Reviewed'),
        ('published','Published'),
    ],default='draft')

    # Adding a filed (column) for the publish date of the book which stores string containing a date format.
    publish_date = fields.Date()

    # Adding a filed (column) for the language of the book which stores string containing the key of the selected option.
    language = fields.Selection([
        ('ar','Arabic'),
        ('en','english')
    ],default='en')

    # name of the book. Char is varchar or string with a small length. you can use char to store numbers sometime which
    # is more advanced.
    isbn = fields.Char("International Standard Book Number")

    # Adding a filed (column) for the price cost of the book which stores real number.
    price = fields.Float()

    # Adding a filed (column) for the relation of the author with the book which stores the author id who wrote the book.
    author = fields.Many2one("flutter.author")

    # Adding a filed (column) for the relation of the publisher with the book which stores the publisher id who published the book of the author.
    publisher = fields.Many2one("flutter.publisher")

    # Adding a filed (column) for the relation of the categories with the books which stores the categories ids which the admin selected. Note: postgres stores then as ids but odoo display them as lists and when you click on them you can choose what categories you want for this book.
    categories = fields.Many2many("flutter.category")

# Adding author model for book authors.
class Author (models.Model):
    _name = 'flutter.author'
    _description = 'Model for storing authors of books and do CRUD operations.'

    # name of the author. Char is varchar or string with a small length.
    name = fields.Char()

    # name of the book. Char is varchar or string with a small length.
    image = fields.Binary()

    # Adding a filed (column) for the reverse relation of the publisher with the book which stores all the books ids that the publisher had published. Note: postgres stores ids but odoo displays them as a list of books records in his views which is nice.
    books = fields.One2many("flutter.book","author")

# Adding a publisher model to store publishers info
class Publisher (models.Model):
    _name = 'flutter.publisher'
    _description = 'Model for storing publishers of books and do CRUD operations.'

    # name of the publisher. Char is varchar or string with a small length.
    name = fields.Char()


    image = fields.Binary()

    publishers = fields.One2many("flutter.book", "publisher")

class Category (models.Model):
    _name = 'flutter.category'
    _description = 'Model for storing categories of the books and do CRUD operations.'

    name = fields.Char()
    books = fields.Many2many("flutter.book")