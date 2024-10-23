from django.contrib import admin
from posts.models import FactPosts, DimUsers, DimPosts, DimCompanies, DimAddresses

admin.site.register(FactPosts, admin.ModelAdmin)
admin.site.register(DimUsers, admin.ModelAdmin)
admin.site.register(DimPosts, admin.ModelAdmin)
admin.site.register(DimCompanies, admin.ModelAdmin)
admin.site.register(DimAddresses, admin.ModelAdmin)
