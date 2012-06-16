from django.contrib import admin

from orgchartapp.models import Employee
from orgchartapp.models import ReportingRelationship

#class ReportingRelationshipInlineSupervisors(admin.StackedInline):
class ReportingRelationshipInlineSupervisors(admin.TabularInline):
	model   = ReportingRelationship
	fk_name = 'employee'
	extra   = 0
	raw_id_fields = ('employee', 'supervisor')

#class ReportingRelationshipInlineEmployees(admin.StackedInline):
class ReportingRelationshipInlineEmployees(admin.TabularInline):
	model   = ReportingRelationship
	fk_name = 'supervisor'
	extra   = 3
	raw_id_fields = ('employee', 'supervisor')

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'job_title', 'contractor', 'part_time_status')
	search_fields = ['full_name', 'job_title']
	fieldsets = [
		(None,               {'fields': ['full_name', 'job_title', 'contractor', 'part_time_status']}),
		]
	inlines = [ReportingRelationshipInlineSupervisors, ReportingRelationshipInlineEmployees]
	list_filter  = ['contractor', 'part_time_status']


class ReportingRelationshipAdmin(admin.ModelAdmin):
	list_display = ('employee_full_name', 'employee_job_title', 'supervisor_full_name', 'dotted')
	list_filter  = ['dotted']
	raw_id_fields = ('employee', 'supervisor')
	search_fields = ['employee__full_name', 'employee__job_title', 'supervisor__full_name']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ReportingRelationship, ReportingRelationshipAdmin)


