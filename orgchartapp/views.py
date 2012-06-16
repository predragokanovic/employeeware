from django.template import Context, loader
from orgchartapp.models import Employee, ReportingRelationship
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
	t = loader.get_template('orgchart/homepage.html')
	c = Context({
	})
	return HttpResponse(t.render(c))

@login_required
def byEmployee(request):
	employee_list = Employee.objects.all().order_by('full_name')
	t = loader.get_template('orgchart/employees.html')
	c = Context({
	'employee_list': employee_list,
	})
	return HttpResponse(t.render(c))

@login_required
def byReportingRelationship(request, manager_id):
	supervisors_list = ReportingRelationship.objects.filter(Q(employee_id = manager_id))
	reporting_relationship_list = ReportingRelationship.objects.filter(Q(supervisor_id = manager_id) | Q(employee_id = manager_id)).order_by('dotted', 'employee__full_name')

	if supervisors_list:
		primary_supervisor_id = supervisors_list[0].supervisor_id
	else:
		manager_name_title = str(Employee.objects.get(Q(id = manager_id)))
		return HttpResponse(manager_name_title + ' has no supervisor defined in the system.')
	
	if (len(reporting_relationship_list) > 0):
		t = loader.get_template('orgchart/chart.html')
		c = Context({
		'primary_supervisor_id': primary_supervisor_id,
		'reporting_relationship_list': reporting_relationship_list,
		})
		return HttpResponse(t.render(c))
	else:
		return HttpResponse(reporting_relationship_list)
