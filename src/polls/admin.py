from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)
