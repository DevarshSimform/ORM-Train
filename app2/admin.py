from django.contrib import admin
from .models import Plan, Account, Blog

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['package', 'level', 'link', 'commission', 'is_paid']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['account', 'title', 'slug', 'content']