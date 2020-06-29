from django import forms
from .backend import CurrencyConverter, getHistoricalData, weightConverter, lengthConverter, temperatureConverter, areaConverter
 
currency_ids = [("US Dollar" , 'USD'), ("Euros" , 'EUR') , ("Indian Rupees" , 'INR'), ("Qatar Doha" , 'QAR'), ("Zimbwabe Harare" , 'ZWD'), ("Arab Emirates Dirham" , 'AED'), ("Pound Sterling" , 'GBP'), ("Japanese Yen" , 'JPY'), ("Yuan Renminbi" , 'CNY')]
    
mass_ids = [("Kilogram" , 'kg'), ("Hectagram" , 'hg'), ("Decagram" , 'dg'), ("Decigram" , 'deg'), ("Kilogram" , 'kg'), ("gram" , 'g'), ("centigram" , 'cg'), ("milligram" , 'mg')]
    
length_ids = [("Nautical Miles" , 'nmi'), ("Miles" , 'mi'), ("Yards" , 'yd'), ("Feet" , 'ft'), ("Inches" , 'inch'), ("Kilometers" , 'km'), ("meters" , 'm'), ("centimeters" , 'cm'), ("millileters" , 'mm')]
	
meterFactor = [('square meter',"square meter"),('square km',"square km"),('square rood',"square rood"),('square cm',"square cm"),('square foot',"square foot") ,
	                    ('square inch',"square inch"), ('square mile',"square mile"), ('milimeter',"milimeter"),('square rod',"square rod"),
	                    ('square yard',"square yard"), ('square township',"square township"), ('square acre', "square acre") ,('square are', "square acre"),
	                    ('square barn', "square barn"), ('square hectare', "square hectre"), ('square homestead', "square homestead")]
fromconvert = [
	("currency","Currency"), ("mass","Mass"), ("length","Length"), ("area","Area"), ("temperature","Temperature")
	]


FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class convertForm(forms.Form):
	convert_from     = forms.CharField(widget=forms.Select(choices=fromconvert))
	convert_to   	 = forms.CharField(widget=forms.Select(choices=convert_from))
	amount = forms.FloatField()


# class convertConverter(forms.Form):
# 	quantity = forms.
# 	amount   = forms.IntegerField()
# 	frm    	 = forms.
# 	to       = forms.