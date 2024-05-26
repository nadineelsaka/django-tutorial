from django.contrib import admin
from .models import Board, Topic, Post
from django.contrib.auth.models import Group

# Register your models here.
# admin.site.register(Board)
# admin.site.register(Topic)
admin.site.register(Post)

# unRegister your models here.
admin.site.unregister(Group)

# to change header or title
admin.site.site_header = 'Boards Admin Panel'
admin.site.site_title = 'Boards Admin Panel'

# to customize some features


class Inline(admin.StackedInline):
    model = Topic
    extra = 1


class BoardAdmin(admin.ModelAdmin):
    inlines = [Inline]


admin.site.register(Board, BoardAdmin)


class TopicAdmin(admin.ModelAdmin):
    fields = ('subject', 'board', 'created_by', 'views')
    list_display = ('subject', 'board', 'created_by', 'combine')
    list_display_links = ('board',)
    list_editable = ('subject',)
    list_filter = ('created_by', 'board')
    search_fields = ('board',)

    def combine(self, obj):  # must combine == combine
        return '{} - {}'.format(obj.subject, obj.board)


admin.site.register(Topic, TopicAdmin)
