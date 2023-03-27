from django.urls import path
from mainapp.views import home_page_view, post_detail_page, form_create_view, handle_tag_form, handle_author_form
from mainapp import views


urlpatterns = [
    path ('', home_page_view, name = 'home'),
    path ('post/<int:post_id>/', post_detail_page, name = 'detail'),
    path('formprocess/', form_create_view, name = "form-create"),
    path('tag-form-processing/', handle_tag_form, name="tag-form-create"),
    path('author_create/', handle_author_form, name="author_create"),
    path('staff/new-post/', views.post_create_page, name='add-post')
]