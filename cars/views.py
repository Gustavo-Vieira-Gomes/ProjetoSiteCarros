from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm #, CarForm
# from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.

def root_path_view(request):
    return redirect('cars_list')
    

class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    # success_url = '/cars/'

    def get_success_url(self) -> str:
        return reverse_lazy('car_detail', kwargs={'pk':self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'







# function view

#def cars_view(request):
#    cars = Car.objects.all().order_by('brand')
#    search = request.GET.get('search')
#
#    if search:
#        cars = cars.filter(model__contains=search).order_by('model')
#    
#    return render(
#        request,
#        'cars.html',
#        {'cars': cars}
#    )

#def new_car_view(request):
#    if request.method == 'POST':
#        # new_car_form = CarForm(request.POST, request.FILES) -> Formulário normal
#        new_car_form = CarModelForm(request.POST, request.FILES)
#        if new_car_form.is_valid():
#            new_car_form.save()
#            return redirect('cars_list')
#    else:
#        # new_car_form = CarForm() -> formulário normal
#        new_car_form = CarModelForm()
#    return render(request, 'new_car.html', { 'new_car_form': new_car_form })


#class CarsView(View):
#    
#    def get(self, request):
#        cars = Car.objects.all().order_by('brand')
#        search = request.GET.get('search')
#    
#        if search:
#            cars = cars.filter(model__contains=search).order_by('model')
#        
#        return render(
#            request,
#            'cars.html',
#            {'cars': cars}
#        )

#class NewCarView(View):
#    
#    def get(self, request):
#        new_car_form = CarModelForm()
#        return render(request, 'new_car.html', { 'new_car_form': new_car_form })
#
#    def post(self, request):
#        new_car_form = CarModelForm(request.POST, request.FILES)
#        if new_car_form.is_valid():
#            new_car_form.save()
#            return redirect('cars_list')
#        return render(request, 'new_car.html', { 'new_car_form': new_car_form })
