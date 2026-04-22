from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("class/<int:class_id>/", views.class_detail, name="class_detail"),
    path("book/<int:class_id>/", views.book_class, name="book_class"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_class/", views.create_class, name="create_class"),
    path("edit_class/<int:class_id>/", views.edit_class, name="edit_class"),
    path("delete_class/<int:class_id>/", views.delete_class, name="delete_class"),
]