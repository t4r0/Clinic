from django.contrib import admin

from models import consultation, pathology, physicaltest, diagnostic
admin.site.register(consultation)
admin.site.register(pathology)
admin.site.register(physicaltest)
admin.site.register(diagnostic)

