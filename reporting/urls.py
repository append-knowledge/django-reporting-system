from django.urls import path
from reporting import views

urlpatterns=[
    path('home',views.UserSigninView.as_view(),name='signin'),
    path('admin/home',views.AdminHome.as_view(),name='adminhome'),
    path('users/add',views.UserAdd.as_view(),name='adduser'),
    path('course/add',views.AddCourse.as_view(),name='addcourse'),
    path('batch/add',views.BatchAdd.as_view(),name='addbatch'),
    path('courses/list',views.CourseListView.as_view(),name='listcourse'),
    path('batches/list',views.BatchListView.as_view(),name='listbatch'),
    path('batches/update/|<int:id>',views.BatchEditView.as_view(),name='batchupdate'),
    path('users/list',views.UserListView.as_view(),name='userlist'),
    path('course/update/<int:id>',views.CourseEditView.as_view(),name='courseupdate'),
    path('user/update/<int:id>',views.UserEditView.as_view(),name='userupdate'),
    # path('user/signin',views.UserSigninView.as_view(),name='usersignin'),
    path('user/home',views.UserHomeView.as_view(),name='userhome'),
    path('signout',views.SignOutView.as_view(),name='signout'),
    path('add/timesheet',views.TimeSheetAdd.as_view(),name='addtimesheet'),
    path('list/timesheets',views.TimeSheetList.as_view(),name='listtimesheets'),
    path('user/timesheet/update/<int:id>',views.UserTimeSheetUpdate.as_view(),name='usertimesheetupdate'),
    path('admin/verify/<int:id>',views.AdminVerifyTime.as_view(),name='verifytime'),






]