from django.conf.urls import url
from login import views
from django.contrib.auth import views as auth_views
from django.urls import path,re_path

urlpatterns = [
##        url(r'^base', views.base, name='base'),
        url(r'^$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        url(r'^plzlogin', views.plzlogin, name='plzlogin'),
        url(r'^logout', auth_views.LogoutView.as_view(template_name='logout.html'), {'next_page': '/'}, name='logout'),
        url(r'^signup', views.signup, name='signup'),
        url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='reset_form.html'), name='password_reset'),
        url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='reset_done.html'), name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                    auth_views.PasswordResetConfirmView.as_view(template_name='reset_confirm.html'), name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='reset_complete.html'), name='password_reset_complete'),
        url(r'^profile', views.update_profile, name='profile'),
        url(r'^showmylist', views.showmylist, name='showmylist'),
        url(r'^nearcrimes', views.shownearcrimes, name='nearcrimes'),

]

