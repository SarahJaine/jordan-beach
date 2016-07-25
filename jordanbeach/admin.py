from django.contrib import admin
from .models import Teaching, Award, Poster, Talk, Publication


class TeachingAdmin(admin.ModelAdmin):
    pass


class AwardAdmin(admin.ModelAdmin):
    pass


class PosterAdmin(admin.ModelAdmin):
    pass


class TalkAdmin(admin.ModelAdmin):
    pass


class PublicationAdmin(admin.ModelAdmin):
    model = Publication
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Teaching, TeachingAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Publication, PublicationAdmin)
