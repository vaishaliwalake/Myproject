
import os
import sys
import django
from django.core.paginator import Paginator

django.setup()
from django.db.models import Sum, Count
from django.db.models.query import QuerySet
from .models import Order


class OrderDetails ():

    orderSummeryQrSet: QuerySet
    contactDetailsQrSet: QuerySet
    allOrdersQrSet = Order.objects.all().prefetch_related ("company__id")
    orderSummeryQrSet = allOrdersQrSet.values ("company__id", "company__name").annotate (Sum ('total'), Count ('order_number'))

    contactDetailsQrSet = Order.objects.all().prefetch_related ("company__id", "concat__id").values ("contact__id", "contact__first_name","contact__last_name").annotate (Count ('order_number'))

    def getOrderDetails(self):
        return self.orderSummeryQrSet

    def getContactsDetails(companyId):
        ct = OrderDetails.contactDetailsQrSet.filter(company__id=companyId)
        return ct

    def getOrderCountPerCompany(self):
        cnt = OrderDetails.allOrdersQrSet.values ("company__id").annotate (Count ('company__id'))
        return cnt