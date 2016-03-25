from django.contrib import admin
from .models import Choice, Poll, UserChoice, AnonymousUserChoice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)


class UserChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserChoice, UserChoiceAdmin)
    
class AnonymousUserChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(AnonymousUserChoice, AnonymousUserChoiceAdmin)