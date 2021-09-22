from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from reporting import forms
from reporting.models import MyUser,Course,Batch


# Create your views here.
class AdminHome(TemplateView):
    template_name = 'reporting/admin_home.html'
    # def get(self,request):
    #     return render(request,'reporting/admin_home.html')

class UserAdd(CreateView):
    model=MyUser
    form_class=forms.UserAddForm
    template_name ='reporting/user_add.html'
    success_url = reverse_lazy('adminhome')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['users']=self.model.objects.all()
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
    model=MyUser
    template_name = 'reporting/user_list.html'
    context_object_name='users'


class AddCourse(CreateView):
    model=Course
    form_class=forms.CourseAddForm
    template_name = 'reporting/course_add.html'
    success_url = reverse_lazy('adminhome')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['courses']=self.model.objects.all()
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
    context_object_name= 'courses'

class CourseEditView(UpdateView):
    model=Course
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
        context=super().get_context_data(**kwargs)
        context['batches']=self.model.objects.all()
        return context

class BatchListView(ListView):
    model = Batch
    template_name = 'reporting/batch_list.html'
    context_object_name='batches'

class BatchEditView(UpdateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = 'reporting/batch_update.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('addbatch')

