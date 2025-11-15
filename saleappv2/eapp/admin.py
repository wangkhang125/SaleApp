from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from eapp.models import Product, Category, UserRole
from eapp import db, app
from flask_login import current_user, logout_user
from flask import redirect

class AdminView(ModelView):
    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.user_role==UserRole.ADMIN

class ProductView(AdminView):
    column_list = ['id', 'name', 'price', 'active', 'category_id'] #Các cột được hiển thị lên trang quản lý
    column_searchable_list = ['name'] #Thanh search theo tên
    column_filters = ['name', 'price'] #Bộ lọc theo tên, giá
    can_export = True #Có thể xuất file
    edit_modal = True #Chỉnh sửa trong trang popup (nếu ko có lệnh này thì khi chỉnh sửa sẽ nhảy sang trang tab mới)
    column_editable_list = ['name', 'price'] #Chỉnh sửa nd trực tiếp trong cột
    page_size = 5 #Số sản phẩm hiển thị từng trang là 5

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self) -> bool:
        return current_user.is_authenticated


ad = Admin(app=app, name="CELL PHONE S's Admin")
ad.add_view(AdminView(Category, db.session))
ad.add_view(ProductView(Product, db.session))
ad.add_view(LogoutView(name="Đăng xuất"))