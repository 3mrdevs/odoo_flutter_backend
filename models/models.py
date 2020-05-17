from odoo import fields, models, api


class Books (models.Model):
    _name = 'flutter.book'
    _description = 'Model for storing books and do CRUD operations.'

    name = fields.Char()
    number = fields.Integer()
    description = fields.Text()
    image = fields.Binary()
    publish_date = fields.Date()
    language = fields.Selection([
        ('ar','Arabic'),
        ('en','english')
    ],default='en')
    isbn = fields.Char("International Standard Book Number")
    price = fields.Float()

    author = fields.Many2one("flutter.author")
    publisher = fields.Many2one("flutter.publisher")

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