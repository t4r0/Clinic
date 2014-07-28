# formularios para vistas

from django import formularios
from consultation.models import pathology, consultation, physicaltest, diagnostic


class formPathology(forms.ModelForm):
	class Meta:
		model = pathology
		fields = ['pathology']

class formConsultation(forms.ModelForm):
	class Meta:
		model = consultation
		fields = ['date','observation','symptoms','patient']

class formPhysicaltest(forms.ModelForm):
	class Meta:
		model = physicaltest
		fields = ['size','weight','pressure','temperature','hartrate','consultation']

class formDiagnostic(forms.ModelForm):
	class Meta:
		model = diagnostic
		fields = ['pathology','consultation']