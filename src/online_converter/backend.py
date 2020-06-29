import urllib.request
from datetime import date, timedelta


def CurrencyConverter(amt, frm, to):

    ids = {"US Dollar" : 'USD', "Euros" : 'EUR', "Indian Rupees" : 'INR', "Qatar Doha" : 'QAR', "Zimbwabe Harare" : 'ZWD', "Arab Emirates Dirham" : 'AED', "Pound Sterling" : 'GBP', "Japanese Yen" : 'JPY', "Yuan Renminbi" : 'CNY'}

    html = urllib.request.urlopen("http://www.exchangerate-api.com/%s/%s/%f?k=a28d653d2d4fd2727003e437" % (frm , to, amt))
    
    return html.read().decode('utf-8')







def getHistoricalData(sym1, sym2):
    sym = sym1 + "," + sym2
    if "EUR" in sym:
        sym = sym.replace("EUR", "")
        sym = sym.replace(",", "")
    link  = "https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&symbols=" + sym

    html =urllib.request.urlopen(link) 
    dic = html.read().decode('utf-8')

    dic1 = ast.literal_eval(dic)
    return dic               







def weightConverter(amt, frm, to):
        # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
    ids = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "gram" : 'g', "centigram" : 'cg', "milligram" : 'mg'}
    # function to convert from a given unit to another
    
    # It is converting an amount(amt), from a unit(frm) to another unit(to)
    if frm != 'g':
        amt = amt * factors[frm]
        return amt / factors[to]
    else:
        return amt / factors[to]
 

    
    
    
    

    
def lengthConverter(amt, frm, to):
        # factors to multiply to a value to convert from the following units to meters(m)
    factors = {'nmi' : 1852, 'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
    ids = {"Nautical Miles" : 'nmi', "Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "meters" : 'm', "centimeters" : 'cm', "millileters" : 'mm'}

    # function to convert from a given unit to another
    if frm != 'm':
        amt = amt * factors[frm]
        return amt / factors[to]
    else:
        return amt / factors[to]
    
    
    
   
    
    
def temperatureConverter(amt, frm, to):

    if frm == 'cel':
        celToFah = ((amt * (9/5)) + 32)
        return celToFah

    else:
        fahToCel = ((amt - 32) * (5/9))
        return fahToCel
    
    
    
    
def areaConverter(x, fromUnit, toUnit):
    
    meterFactor = {'square meter':1,'square km':1000000,'square rood':1011.7141056,'square cm':0.0001,'square foot':0.09290304 ,
                    'square inch':0.00064516, 'square mile':2589988.110336, 'milimeter':0.000001,'square rod':25.29285264,
                    'square yard':0.83612736, 'square township':93239571.9721, 'square acre':4046.8564224 ,'square are': 100,
                    'square barn':1e-28, 'square hectare':10000, 'square homestead':647497.027584 }

    if fromUnit in meterFactor.keys() and toUnit in meterFactor.keys():     
        result = (x*meterFactor[fromUnit])/ (meterFactor[toUnit])
        return result
    
    
