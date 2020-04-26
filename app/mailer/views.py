#-*- coding: utf-8 -*-

# Create your views here.

from django.template.defaulttags import register
from django.views.generic import ListView
from .OrderDetailsHelper import *

class LimitOffsetPagination(Paginator):
    def count(self):
        paginatorValue = OrderDetails.getOrderCountPerCompany ("count")
        print ("pagination value --> ", paginatorValue)
        return paginatorValue

    @property
    def paginator(self):
        paginator = super ().paginator
        paginatorValue = OrderDetails.getOrderCountPerCompany ("count")
        print ("pagination value --> ", paginatorValue)
        paginator.count = paginatorValue
        return paginator

class IndexView(ListView):
    template_name = "mailer/index.html"
    pagination_class = LimitOffsetPagination
    order = OrderDetails.getOrderCountPerCompany
    paginate_by = 100

    def get_queryset(self):
        #tried to use pagination with custom count, since current pagination is using order
        # summary sql to get count which is bit expensive, but still not using with following way,
        # this implemntation is still pending, that would add to reduce 10-15 MS in page load performance
        #paginator = Paginator (OrderDetails.getOrderCountPerCompany ("count"), 10)
        #paginator.paginate_by=100
       return OrderDetails.orderSummeryQrSet

    @register.simple_tag()
    def getContactsForCompanyId(companyId):
        ct = OrderDetails.getContactsDetails(companyId)
        return ct
