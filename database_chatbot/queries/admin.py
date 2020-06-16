from django.contrib import admin
from .models import Query
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.


class QueryResource(resources.ModelResource):
    class Meta:
        model = Query
        skip_unchanged = True
        report_skipped = False
        exclude = ('id')
        import_id_fields = ('intent', 'response',)
        fields = ('intent', 'response',)

class QueryAdmin(ImportExportModelAdmin):
    resource_class = QueryResource

admin.site.register(Query, QueryAdmin)
