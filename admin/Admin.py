# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from model.User import User
from model.Category import Category
from model.Product import Product
from model.Role import Role

from admin.Views import UserView, HomeView, ProductView


def start_views(app, db):
    admin = Admin(app, name='Meu Estoque', template_mode='bootstrap3', base_template='admin/base.html',
                  index_view=HomeView())

    admin.add_view(ModelView(Role, db.session, "Funções", category="Usuarios"))
    admin.add_view(UserView(User, db.session, "Usuários", category='Usuarios'))
    admin.add_view(ModelView(Category, db.session, 'Categorias', category="Produtos"))
    admin.add_view(ProductView(Product, db.session, "Produtos", category="Produtos"))

    admin.add_link(MenuLink(name='Logout', url='/logout'))
