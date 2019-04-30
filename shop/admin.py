from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# from django.apps import apps

# Register your models here.

# for model in apps.get_app_config('shop').models.values():  # registering all models
#     admin.site.register(model)
admin.site.site_header = 'Car Details Shop'
admin.site.unregister(Group)


def get_model_fields(model):
    return [field.name for field in model._meta.get_fields()][1:]


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = get_model_fields(VehicleType)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Mark)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Region)


@admin.register(DetailType)
class DetailTypeAdmin(admin.ModelAdmin):
    list_display = get_model_fields(DetailType)


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Detail)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Vehicle)


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Other)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Review)
    readonly_fields = ['name', 'comment', 'time']

