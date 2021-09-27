from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from reporting import forms
from reporting.models import MyUser, Course, Batch, TimeSheet
from django.contrib.auth import authenticate, login, logout
from .decorators import Signin_Required
from django.utils.decorators import method_decorator
from .filters import TimeFilter


# Create your views here.
class AdminHome(TemplateView):
    template_name = 'reporting/admin_home.html'

    # def get(self,request):
    #     return render(request,'reporting/admin_home.html')


class UserAdd(CreateView):
    model = MyUser
    form_class = forms.UserAddForm
    template_name = 'reporting/user_add.html'
    success_url = reverse_lazy('adminhome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.model.objects.all()
        return context

    # context={}
    # def get(self,request):
    #     form=self.form_class()
    #     self.context['form']=form
    #     return render(request,self.template_name,self.context)
    # def post(self,request):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('adminhome')


#
class UserEditView(UpdateView):
    model = MyUser
    form_class = forms.UserAddForm
    template_name = 'reporting/user_update.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('adminhome')


class UserListView(ListView):
    model = MyUser
    template_name = 'reporting/user_list.html'
    context_object_name = 'users'


class AddCourse(CreateView):
    model = Course
    form_class = forms.CourseAddForm
    template_name = 'reporting/course_add.html'
    success_url = reverse_lazy('adminhome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.model.objects.all()
        return context

    # def get(self,request):
    #     form=self.form_class()
    #     self.context['form']=form
    #     return render(request,self.template_name,self.context)
    # def post(self,request):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('addbatch')


class CourseListView(ListView):
    model = Course
    template_name = 'reporting/course_list.html'
    context_object_name = 'courses'


class CourseEditView(UpdateView):
    model = Course
    form_class = forms.CourseAddForm
    template_name = 'reporting/course_update.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('addcourse')


class BatchAdd(CreateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = 'reporting/batch_add.html'
    success_url = reverse_lazy('addbatch')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batches'] = self.model.objects.all()
        return context


class BatchListView(ListView):
    model = Batch
    template_name = 'reporting/batch_list.html'
    context_object_name = 'batches'


class BatchEditView(UpdateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = 'reporting/batch_update.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('addbatch')


class UserSigninView(TemplateView):
    template_name = 'reporting/user_signin.html'
    form_class = forms.UserSigninForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                if request.user.is_admin:
                    return redirect('adminhome')
                else:
                    return redirect('userhome')
            else:
                return redirect('userhome')


@method_decorator(Signin_Required, name='dispatch')
class UserHomeView(TemplateView):
    template_name = 'reporting/user_home.html'


@method_decorator(Signin_Required, name='dispatch')
class SignOutView(TemplateView):
    def get(self, request, **kwargs):
        logout(request)
        return redirect('signin')


@method_decorator(Signin_Required, name='dispatch')
class TimeSheetAdd(CreateView):
    model = TimeSheet
    template_name = 'reporting/add_timesheets.html'
    form_class = forms.TimeSheetForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            time = form.save(commit=False)
            time.user = request.user
            time.save()
            return redirect('userhome')


@method_decorator(Signin_Required, name='dispatch')
class TimeSheetList(FilterView):
    model = TimeSheet
    template_name = 'reporting/list_timesheet.html'
    context_object_name = 'timesheets'
    filterset_class = TimeFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset_class
        return context

    def get_queryset(self):
        if self.request.user.is_admin:
            queryset = self.model.objects.all()

        else:
            queryset = self.model.objects.filter(user=self.request.user)
        return queryset
    # def get(self,request,**kwargs):
    #     time=self.models.objects.filter(user=request.user)
    #     context={}
    #     context['time']=time
    #     return render(request,self.template_name,self.context)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = self.filterset_class
    #     return context


@method_decorator(Signin_Required, name='dispatch')
class UserTimeSheetUpdate(UpdateView):
    model = TimeSheet
    template_name = 'reporting/user_edittimesheet.html'
    form_class = forms.TimeSheetForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listtimesheets')


class AdminVerifyTime(TemplateView):
    model = TimeSheet
    pk_url_kwarg = 'id'

    # template_name = 'reporting/list_timesheet.html'
    def get(self, request, *args, **kwargs):
        time = self.model.objects.get(id=kwargs['id'])
        time.verified = True
        time.save()
        return redirect('listtimesheets')


