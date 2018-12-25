from django import forms
from .models import Student, Marks

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student

		fields = [
			'name',
			'gender',
			'age',
		]

		labels = {
			'name': 'Name',
			'gender':'Gender',
			'age':'Age',
		}


class MarksForm(forms.ModelForm):
	class Meta:
		model = Marks

		fields = [
			'class_name',
			'english',
			'nepali',
		]

		widgets = {
			'class_name': forms.TextInput(attrs={'class': 'formset-field'}),
			'english': forms.TextInput(attrs={'class': 'formset-field'}),
			'nepali': forms.TextInput(attrs={'class': 'formset-field'})
		}