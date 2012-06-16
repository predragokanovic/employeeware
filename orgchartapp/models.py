from django.db import models


# Create your models here.

class Employee(models.Model):
	full_name        = models.CharField(max_length=100)
	job_title        = models.CharField(max_length=100)
	contractor       = models.BooleanField(default=False)
	part_time_status = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.full_name + ", " + self.job_title


class ReportingRelationship(models.Model):
	employee      = models.ForeignKey(Employee)
	supervisor    = models.ForeignKey(Employee, related_name='+')
	dotted        = models.BooleanField(default=False)
#	assistant     = models.BooleanField(default=False)
	
	def employee_full_name(self):
		return self.employee.full_name
	employee_full_name.admin_order_field  = 'employee'

	def employee_job_title(self):
		return self.employee.job_title
	employee_job_title.admin_order_field  = 'job_title'
	
	def supervisor_full_name(self):
		return self.supervisor.full_name
	supervisor_full_name.admin_order_field  = 'supervisor'
	
	def __unicode__(self):
		if (self.dotted) : 
			label = self.employee.full_name + " -- dotted reports to --> " + self.supervisor.full_name
		else:
			label = self.employee.full_name + " -- reports to --> " + self.supervisor.full_name	
		return label
