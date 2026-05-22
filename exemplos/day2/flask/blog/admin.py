from datetime import datetime, date
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_admin.theme import Bootstrap4Theme
from flask_simplelogin import login_required
from flask_admin.model import typefmt
from wtforms import form, fields, validators
from blog.database import mongo

# Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)

class PostsForm(form.Form):
    title = fields.StringField("Title", [validators.data_required()])
    slug = fields.HiddenField("Slug")
    content = fields.TextAreaField("Content")
    published = fields.BooleanField("Published", default=True)

def date_format(view, value):
    return value.strftime('%d/%m/%Y %H:%M:%S')

MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({
        type(None): typefmt.null_formatter,
        date: date_format
    })

class AdminPosts(ModelView):
    column_list = ("title", "slug", "content", "published", "date")
    form = PostsForm
    column_type_formatters = MY_DEFAULT_FORMATTERS

    def on_model_change(self, form, post, is_created):
        post["slug"] = post["title"].replace("_", "-").replace(" ", "-").lower()
        if is_created:
            post["date"] = datetime.now()

def configure(app):
    admin = Admin(
        app,
        name=app.config.get("TITLE"),
        theme=Bootstrap4Theme(
            swatch=app.config.get("FLASK_ADMIN_SWATCH", "cerulean")
        ),
    )
    admin.add_view(AdminPosts(mongo.db.posts, "Post"))
    