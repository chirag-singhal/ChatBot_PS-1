from django.contrib import admin
from .models import Query
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.forms import ValidationError
# Register your models here.


class QueryResource(resources.ModelResource):
    class Error(object):
        def __init__(self, error, traceback=None, row=None):
            self.error = error
            self.traceback = traceback
            self.row = row
    class Meta:
        model = Query
        skip_unchanged = True
        report_skipped = False
        exclude = ('id')
        import_id_fields = ('intent', 'response',)
        fields = ('intent', 'response',)
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for row in dataset:
            print(row)
            if row[0] is None and row[1] is None:
                raise ValidationError('Row cannot be empty\n')
            elif row[1] is None:
                raise ValidationError(' Response cannot be null for intent = %s\n' % row[0])
            elif row[0] is None:
                raise ValidationError(' Intent cannot be null for response = %s\n' % row[1])
        return

class QueryAdmin(ImportExportModelAdmin):
    resource_class = QueryResource

admin.site.register(Query, QueryAdmin)
