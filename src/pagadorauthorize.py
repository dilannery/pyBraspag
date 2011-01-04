#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import sys

class PagadorAuthorizeRequest(object):
    def __init__(self, orderId):
        request = etree.Element('request')
        order_id = etree.SubElement(request, 'OrderId')
        order_id.text = orderId
        self.request = request
        
    def setCard(self, cardHolder, cardNumber, cardExpirationDate, 
                cardSecurityCode):
        card_holder = etree.SubElement(self.request, 'CardHolder')
        card_holder.text = cardHolder
        card_number = etree.SubElement(self.request, 'CardNumber')
        card_number.text = cardNumber
        card_expirationdate = etree.SubElement(self.request, 'CardExpirationDate')
        card_expirationdate.text = cardExpirationDate
        card_securitycode = etree.SubElement(self.request, 'CardSecurityCode')
        card_securitycode.text = cardSecurityCode
    
    
    def get_xml(self):
        return etree.tostring(self.request)    
