
import csv

from application.models import Application
from django import forms
from django.contrib import admin, messages
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse

from .models import Result


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    change_list_template = 'result/admin/result_changelist.html'
    list_display = ['application', 'get_roll', 'remarks']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            data_set = csv_file.read().decode('UTF-8')
            import io
            io_string = io.StringIO(data_set)
            # next(io_string)
            error_applications = []
            for row in csv.DictReader(io_string, delimiter=','):
                try:
                    application = Application.objects.get(
                        id=row['Application ID'], details__serial=row['Roll'])
                    result, created = Result.objects.update_or_create(
                        application_id=application.id, remarks=row['Remarks'])
                except:
                    error_applications.append(row['Application ID'])

            if len(error_applications) > 0:
                self.message_user(
                    request,  f'Could not Upload these applications: {error_applications}', messages.ERROR)
                return HttpResponseRedirect("..")
            else:
                self.message_user(
                    request, "Your csv file has been imported")
                return HttpResponseRedirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "result/admin/csv_form.html", payload
        )

    @admin.display(description='Roll')
    def get_roll(self, obj):
        return obj.application.details.serial
