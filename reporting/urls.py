from django.urls import path
from reporting import views

urlpatterns=[
    path('home',views.AdminHome.as_view(),name='adminhome'),
    path('users/add',views.UserAdd.as_view(),name='adduser'),
    path('course/add',views.AddCourse.as_view(),name='addcourse'),
    path('batch/add',views.BatchAdd.as_view(),name='addbatch'),
    path('courses/list',views.CourseListView.as_view(),name='listcourse'),
    path('batches/list',views.BatchListView.as_view(),name='listbatch'),
    path('batches/update/|<int:id>',views.BatchEditView.as_view(),name='batchupdate'),
    path('users/list',views.UserListView.as_view(),name='userlist'),
    path('course/update/<int:id>',views.CourseEditView.as_view(),name='courseupdate'),
    path('user/update/<int:id>',views.UserEditView.as_view(),name='userupdate')



]