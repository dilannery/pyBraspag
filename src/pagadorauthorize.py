#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

class PagadorAuthorizeRequest(object):
    def __init__(self, orderId):
        request = etree.Element('request')
        order_id = etree.SubElement(request, 'OrderId')
        order_id.text = orderId
        self.request = request
        
    def set_customerName(self, name):
        custumer_name = etree.SubElement(self.request, 'CustomerName')
        custumer_name.text = name
        return self
        
    def set_valor(self, valor):
        _valor = etree.SubElement(self.request, 'TransactionAmount')
        _valor.text = valor
        return self
        
    def set_card(self, cardHolder, cardNumber, cardExpirationDate, 
                cardSecurityCode):
        card_holder = etree.SubElement(self.request, 'CardHolder')
        card_holder.text = cardHolder
        card_number = etree.SubElement(self.request, 'CardNumber')
        card_number.text = cardNumber
        card_expirationdate = etree.SubElement(self.request, 'CardExpirationDate')
        card_expirationdate.text = cardExpirationDate
        card_securitycode = etree.SubElement(self.request, 'CardSecurityCode')
        card_securitycode.text = cardSecurityCode
        return self
        
    def set_parcelas(self, numero):
        parcelas = etree.SubElement(self.request, 'InstallmentCount')
        parcelas.text = numero
        return self
        
    def set_cpf(self, numero):
        cpf = etree.SubElement(self.request, 'Cpf')
        cpf.text = numero
        return self
        
    def set_cnpj(self, numero):
        cnpj = etree.SubElement(self.request, 'Cnpj')
        cnpj.text = numero
        return self
        
    def set_data(self, data):
        _data = etree.SubElement(self.request, 'MerchantLocalDate')
        _data.text = data
        return self
        
    def set_buyerInfo(self, ip, email):
        buyer_ip = etree.SubElement(self.request, 'BuyerIp')
        buyer_ip.text = ip
        buyer_email = etree.SubElement(self.request, 'BuyerE-mail')
        return self
        
    def set_tipoDePagamento(self, numero):
        tipo_de_pagamento = etree.SubElement(self,request, 'PaymentType')
        tipo_de_pagamento.text = numero
        return self
    
    def get_xml(self):
        return etree.tostring(self.request)
