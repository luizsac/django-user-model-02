from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclude = ['autor',]

    def _autor(self, instance) -> str:
        return f'{instance.autor.get_full_name()}'  # método da classe django.contrib.auth.models.User

    def get_queryset(self, request):  # sobrescreve método da superclasse para filtrar autores
        qs = super().get_queryset(request)
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
