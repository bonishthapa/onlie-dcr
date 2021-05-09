from django.db import models
from user.models import User, ClientTable, ClientType
from dcr_system.models import ProductInformation

class LeaveReport(models.Model):
    report_initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_initiator')
    report_reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_reciever')
    subject = models.CharField(max_length=250)
    status1 = models.CharField(max_length=250)
    status2 = models.CharField(max_length=250)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_updated_by')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.updated_by.email

class AdminReport(models.Model):
    report_writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_writer')
    subject = models.CharField(max_length=250)
    report_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_supervisor')
    status1 = models.CharField(max_length=250)
    status2 = models.CharField(max_length=250)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_report_updated_by')
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class DailyCallReport(models.Model):
    shift = models.CharField(max_length=250)
    visited_area = models.CharField(max_length=250)
    client_type = models.ForeignKey(ClientType,on_delete=models.CASCADE,related_name='dcr_client_type')
    client_name = models.ForeignKey(ClientTable,on_delete=models.CASCADE,related_name='dcr_client_name')
    gift = models.CharField(max_length=250)
    product = models.ForeignKey(ProductInformation,on_delete=models.CASCADE,related_name='dcr_product')
    quantity = models.IntegerField()
    amount = models.FloatField()
    mpo_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='dcr_mpo_id')
    dcr_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    visited_with = models.ForeignKey(User,on_delete=models.CASCADE,related_name='dcr_visited_with')
    sample = models.ForeignKey(ProductInformation,on_delete=models.CASCADE,related_name='dcr_sample_product')
    sample_qty = models.IntegerField()

    def __str__(self):
        return self.client_name.name

class DcrHigher(models.Model):
    date = models.DateField()
    supervised_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='dcr_higher_supervised')
    dcr_id = models.ForeignKey(DailyCallReport,on_delete=models.CASCADE,related_name='dcr_id')
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='dcr_higher_updated_by')
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.supervised_id.email


class SalesReport(models.Model):
    date = models.DateField()
    client_name = models.ForeignKey(ClientTable,on_delete=models.CASCADE, related_name='sr_cleint_name')
    address = models.CharField(max_length=250)
    product = models.ForeignKey(ProductInformation, on_delete=models.CASCADE, related_name='sr_product')
    qunatity = models.IntegerField()
    sales_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sr_sale_person')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sr_updated_by')
    updated_date = models.DateField(auto_now=True)

