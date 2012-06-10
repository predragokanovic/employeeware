from django.template import Context, loader
from orgchartapp.models import Employee, ReportingRelationship
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def home(request):
    return HttpResponse("Peopleware by Rajiv: Organization Chart Management")
    


def byEmployee(request):
	employee_list = Employee.objects.all()
	t = loader.get_template('orgchart/employees.html')
	c = Context({
	'employee_list': employee_list,
	})
	return HttpResponse(t.render(c))
	
	
def byReportingRelationship(request, manager_id):
	reporting_relationship_list = ReportingRelationship.objects.filter(Q(supervisor_id = manager_id) | Q(employee_id = manager_id))
	primary_supervisor_id = ReportingRelationship.objects.filter(Q(employee_id = manager_id))[0].supervisor_id
	t = loader.get_template('orgchart/chart.html')
	c = Context({
	'primary_supervisor_id': primary_supervisor_id,
	'reporting_relationship_list': reporting_relationship_list,
	})
	return HttpResponse(t.render(c))
