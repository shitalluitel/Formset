from django.shortcuts import render,redirect
from .models import Student, Marks
from .forms import StudentForm, MarksForm
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError

# Create your views here.

def create(request):
	context = {}
	MarksFormset = modelformset_factory(Marks, form=MarksForm)	
	form = StudentForm(request.POST or None)
	formset = MarksFormset(request.POST or None, queryset= Marks.objects.none(), prefix='marks')
	if request.method == "POST":
		if form.is_valid() and formset.is_valid():
			try:
				with transaction.atomic():
					student = form.save(commit=False)
					student.save()

					for mark in formset:
						data = mark.save(commit=False)
						data.student = student
						data.save()
			except IntegrityError:
				print("Error Encountered")

			return redirect('multi_forms:list')


	context['formset'] = formset
	context['form'] = form
	return render(request, 'multi_forms/create.html', context)

def list(request):
	datas = Student.objects.all()
	return render(request, 'multi_forms/list.html', {'datas':datas})