from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest
from .models import *
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ngettext
    

@admin.register(UploadApplicant)
class ApplicantUploadData(admin.ModelAdmin):
    list_display = ('uploaded_at', 'ApplicantName' , 'jobPosition' , 'embed_pdf', 'detail_url','subklasifikasiSKA', 'klasifikasiSKA', 'detail_ska','status' ,'Action') 
    readonly_fields = [
        'uploaded_at', 
        'ApplicantName' , 
        'jobPosition' ,
        'document',
        
    ]
    class Meta:
         verbose_name = "Pending Applicant"

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    actions = ['Review']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(status='Pending')
        return qs

    def Action(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.id])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
        return format_html(html)

    def Review(self, request, queryset):
        updated =  queryset.update(status = 'On Review')
        self.message_user(
            request,
            ngettext(
                "%d Applicant was successfully marked as On Review.",
                "%d Applicant were successfully marked as On Review.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    def Reject(self, request, queryset):
        queryset.update(status = 'Reject')
   
    
    def embed_pdf(self, obj):
        try:
            html = f'<iframe src="{obj.document.url}" width="200px" height="200px" frameborder="2"></iframe>'
            formatted_html = format_html(html.formenat(url=obj.document.url))
            return formatted_html
        except Exception as e:
            pass

    embed_pdf.short_description = "Applicant Document"


    def detail_url(self, document):
        url = document.document.url
        return mark_safe(f'<a href="{url}" target="_blank" rel="nofollow"">View Document</a>')

    def detail_ska(self, document):
        if self.detail_ska:
            return format_html('<p> Tidak ada Lampiran </p>')
        else:
            return mark_safe(f'<a href="{document.lampiranSKA}" target="_blank" rel="nofollow"">View Document</a>')

@admin.register(ApprovedApplicant)
class ApprovedApplicant(admin.ModelAdmin):
    list_display = ('uploaded_at', 'ApplicantName' , 'jobPosition' , 'embed_pdf', 'detail_url','subklasifikasiSKA', 'klasifikasiSKA', 'detail_ska' , 'status','Action') 
    readonly_fields = [
        'uploaded_at', 
        'ApplicantName' , 
        'jobPosition' ,
        'document',
        
    ]
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(status='Approve')
        return qs
    
        
    def Action(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.id])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
        return format_html(html)
  
    
    def embed_pdf(self, obj):
        try:
            html = f'<iframe src="{obj.document.url}" width="200px" height="200px" frameborder="2"></iframe>'
            formatted_html = format_html(html.format(url=obj.document.url))
            return formatted_html
        except Exception as e:
            pass

    embed_pdf.short_description = "Applicant Document"


    def detail_url(self, document):
        url = document.document.url
        return mark_safe(f'<a href="{url}" target="_blank" rel="nofollow"">View Document</a>')
    
    def detail_ska(self, document):
        if self.detail_ska:
            return format_html('<p> Tidak ada Lampiran </p>')
        else:
            return mark_safe(f'<a href="{document.lampiranSKA}" target="_blank" rel="nofollow"">View Document</a>')
    

@admin.register(RejectApplicant)
class RejectApplicant(admin.ModelAdmin):
    list_display = ('uploaded_at', 'ApplicantName' , 'jobPosition' , 'embed_pdf', 'detail_url','subklasifikasiSKA', 'klasifikasiSKA', 'detail_ska', 'status','Action') 
    readonly_fields = [
        'uploaded_at', 
        'ApplicantName' , 
        'jobPosition' ,
        'document',
        
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(status='Reject')
        return qs

    def has_add_permission(self, request):
        return False

    def Action(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.id])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
        return format_html(html)
  
    
    def embed_pdf(self, obj):
        try:
            html = f'<iframe src="{obj.document.url}" width="200px" height="200px" frameborder="2"></iframe>'
            formatted_html = format_html(html.format(url=obj.document.url))
            return formatted_html
        except Exception as e:
            pass

    embed_pdf.short_description = "Applicant Document"


    def detail_url(self, document):
        url = document.document.url
        return mark_safe(f'<a href="{url}" target="_blank" rel="nofollow"">View Document</a>')
    
    
    def detail_ska(self, document):
        if self.detail_ska:
            return format_html('<p> Tidak ada Lampiran </p>')
        else:
            return mark_safe(f'<a href="{document.lampiranSKA}" target="_blank" rel="nofollow"">View Document</a>')

@admin.register(ReviewApplicant)
class ReviewApplicant(admin.ModelAdmin):
    list_display = ('uploaded_at', 'ApplicantName' , 'jobPosition' , 'embed_pdf', 'detail_url','subklasifikasiSKA', 'klasifikasiSKA', 'detail_ska', 'status' ,'Action') 
    readonly_fields = [
        'uploaded_at', 
        'ApplicantName' , 
        'jobPosition' ,
        'document',
        
    ]
    actions = ['Approve','Reject']

    def has_delete_permission(self, request, obj=None):
        return False

    def Approve(self, request, queryset):
        updated =  queryset.update(status = 'Approve')
        self.message_user(
            request,
            ngettext(
                "%d Applicant was successfully marked as On Approve Applicant.",
                "%d Applicant were successfully marked as On Approve Applicant.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    def Reject(self, request, queryset):
        rejected = queryset.update(status = 'Reject')
        self.message_user(
            request,
            ngettext(
                "%d Applicant was successfully marked as On Reject Applincant.",
                "%d Applicant were successfully marked as On Reject Applincant.",
                rejected,
            )
            % rejected,
            messages.SUCCESS,
        )
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(status='On Review')
        return qs

    def has_add_permission(self, request):
        return False

    def Action(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.id])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
        return format_html(html)
  
    
    def embed_pdf(self, obj):
        try:
            html = f'<iframe src="{obj.document.url}" width="200px" height="200px" frameborder="2"></iframe>'
            formatted_html = format_html(html.format(url=obj.document.url))
            return formatted_html
        except Exception as e:
            pass

    embed_pdf.short_description = "Applicant Document"


    def detail_url(self, document):
        url = document.document.url
        return mark_safe(f'<a href="{url}" target="_blank" rel="nofollow"">View Document</a>')
    
    def detail_ska(self, document):
        if self.detail_ska:
            return format_html('<p> Tidak ada Lampiran </p>')
        else:
            return mark_safe(f'<a href="{document.lampiranSKA}" target="_blank" rel="nofollow"">View Document</a>')

@admin.register(Career)
class CareerView(admin.ModelAdmin):
    list_display = ('PostDate', 'department', 'position', 'location', 'employeeType')
    def PostDate(self, obj):
        return obj.posting_date.strftime('%Y-%m-%d')


@admin.register(News)
class News(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image.url:
            return format_html('<img src="{}" width="150px" height="100px" />'.format(obj.image.url))
        else:
            return format_html('<img src="{/images/placeholder.jpg}" width="150px" height="100px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('createAt','image_tag', 'headline')


@admin.register(Kegiatan)
class Kegiatan(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image.url:
            return format_html('<img src="{}" width="150px" height="100px" />'.format(obj.image.url))
        else:
            return format_html('<img src="{/images/placeholder.jpg}" width="150px" height="100px" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('createAt', 'textarea','image_tag', 'headline')


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ('namaPekerjaan', 'tahun', 'latCoor','longCoor', 'ktPekerjaan', 'impact', 'unitImpact')

# @admin.register(ApprovedApps)
# class ApprovedApplicant(admin.ModelAdmin):
#     model = UploadApplicant
#     list_display = ('approved_date', 'ApplicantName' )


    # def ApplicantName(self, obj):
    #     return obj.status

# @admin.register(DepartementList)
# class DepartementList(admin.ModelAdmin):
    # list_display = ('jobList')

# admin.site.register(ApprovedApplicant)
admin.site.register(DepartementList)
admin.site.register(EmployeeTypeList)
# admin.site.register(InputApplicant)
@admin.register(InputApplicant)
class ApplicantUploadData(admin.ModelAdmin):
    list_display = ('submit_at', 'jobPosition' , 'FirstName' , 'LastName') 
    readonly_fields = [
        'jobPosition',
        'FirstName',
        'LastName',
        'Gender',
        'DoB',
        'PoB',
        'Nationality',
        'personalEmail',
        'personalMobile',
        'LicDrive',
        'linkedin',
        'address_1',
        'address_2',
        'expectedSalary',
        'grossSalary',
        'medicalHistory',
        'ReferensiInfo',
        'referensiName',
        'referensiRelasi',
        'submit_at',
        
    ]
    

admin.site.register(Tag)
admin.site.register(ActivityTag)
admin.site.register(User, UserAdmin)