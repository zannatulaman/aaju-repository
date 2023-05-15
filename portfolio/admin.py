from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blogs)
admin.site.register(Portfolio)



class InternshipAdmin(admin.ModelAdmin):
    list_display = ('fullname',
                    'usn',
                    'email',
                    'college_name',
                    'offer_status',
                    'start_date',
                    'end_date',
                    'proj_report',
                    'timeStamp')
    search_fields=('fullname','usn','email')
    list_filter=['college_name','proj_report','offer_status']

admin.site.register(Internship,InternshipAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('birthday',
                    'phonenumber',
                    'website',
                    'age',
                    'city',
                    'phoneEmail',
                    'freelance',
                    'degree')
    search_fields=('birthday','website','phoneEmail')
    list_filter=['city','age','degree']

admin.site.register(About,AboutAdmin)

