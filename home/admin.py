from django.contrib import admin
from .models import Clothing, Trade

# Register your models here.
# class ProblemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'image', 'user']

# class GeneratedProblemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'problem', 'generated']
    
class ClothingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'title', 'color', 'size', 'cType', 'trade']


class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user1', 'user2']


# admin.site.register(Problem, ProblemAdmin)
# admin.site.register(GeneratedProblem, GeneratedProblemAdmin)
admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Trade, TradeAdmin)