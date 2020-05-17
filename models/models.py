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

    language = fields.Selection([
        ('ar','Arabic'),
        ('en','english')
    ],default='en')

    isbn = fields.Char("International Standard Book Number")
    price = fields.Float()

    author = fields.Many2one("flutter.author")
    publisher = fields.Many2one("flutter.publisher")
    categories = fields.Many2many("flutter.category")

class Author (models.Model):
    _name = 'flutter.author'
    _description = 'Model for storing authors of books and do CRUD operations.'

    name = fields.Char()
    image = fields.Binary()

    books = fields.One2many("flutter.book","author")

class Publisher (models.Model):
    _name = 'flutter.publisher'
    _description = 'Model for storing publishers of books and do CRUD operations.'

    name = fields.Char()
    image = fields.Binary()

    publishers = fields.One2many("flutter.book", "publisher")

class Category (models.Model):
    _name = 'flutter.category'
    _description = 'Model for storing categories of the books and do CRUD operations.'

    name = fields.Char()
    books = fields.Many2many("flutter.book")