# forms.py

from wtforms import Form, StringField, SelectField, validators

class BookSearchForm(Form):
    choices = [('Title', 'Title'),
               ('Author', 'Author'),
               ('Year', 'Year'),
               ('Category', 'Category')]
    select = SelectField('Search for books:', choices=choices)
    search = StringField('')
    getallbooks = StringField('')