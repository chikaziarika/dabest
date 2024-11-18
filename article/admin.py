from django.contrib import admin, messages

# Register your models here.

from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ngettext


@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('headline' , 'author' ,'createAt', 'get_tags', 'artstatus' ,'Action')
    
    actions = ['Approve','Reject']

    @admin.display(description='tags')
    def get_tags(self, obj):
        return [tags.nameTag for tags in obj.tags.all()]

    class Meta:
         verbose_name = "Pending Article"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(artstatus='Pending')
        return qs
    
    def Action(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.id])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
        return format_html(html)

    def Approve(self, request, queryset):
        updated =  queryset.update(artstatus = 'Approve')
        self.message_user(
            request,
            ngettext(
                "%d Article was successfully marked as Approve.",
                "%d Article were successfully marked as Approve.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    def Reject(self, request, queryset):
        queryset.update(artstatus = 'Reject')

    # def has_delete_permission(self, request, obj=None):
    #     return False

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'get_headline', 'body', 'created_on')

    def get_headline(self, obj):
        return obj.article.headline

    def has_add_permission(self, request):
        return False

@admin.register(ApprovedArticle)
class ApprovedArticle(admin.ModelAdmin):
    list_display = ('headline','createAt' , 'author',  'get_tags', 'artstatus' ,'Action')
    
    # actions = ['Approve','Reject']

    @admin.display(description='tags')
    def get_tags(self, obj):
        return [tags.nameTag for tags in obj.tags.all()]

    class Meta:
         verbose_name = "Approved Article"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(artstatus='Approve')
        return qs
    
    def Action(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.id])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
        return format_html(html)

    def Approve(self, request, queryset):
        updated =  queryset.update(artstatus = 'Approve')
        self.message_user(
            request,
            ngettext(
                "%d Article was successfully marked as Approve.",
                "%d Article were successfully marked as Approve.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    def Reject(self, request, queryset):
        queryset.update(artstatus = 'Reject')

    def has_delete_permission(self, request, obj=None):
        return False
    

@admin.register(RejectArticle)
class RejectArticle(admin.ModelAdmin):
    list_display = ('headline','createAt', 'author' , 'get_tags', 'artstatus' ,'Action')
    
    # actions = ['Approve','Reject']

    @admin.display(description='tags')
    def get_tags(self, obj):
        return [tags.nameTag for tags in obj.tags.all()]

    class Meta:
         verbose_name = "Reject Article"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(artstatus='Rejected')
        return qs
    
    def Action(self, obj):
        view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.id])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)
        return format_html(html)

    def Approve(self, request, queryset):
        updated =  queryset.update(artstatus = 'Approve')
        self.message_user(
            request,
            ngettext(
                "%d Article was successfully marked as Approve.",
                "%d Article were successfully marked as Approve.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    def Reject(self, request, queryset):
        queryset.update(artstatus = 'Reject')

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Tag)
# admin.site.register(Comment)