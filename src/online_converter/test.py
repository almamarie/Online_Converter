import unittest
import backend as lb

class Test_Backend(unittest.TestCase):

    def test_weightConverter(self):
        print('Weight Converter test random value')
        self.assertEqual(lb.weightConverter(1, 'kg', 'g'), 1000)


    def test_areaConverterNone(self):
        print('Area Converter test for return none')
        self.assertEqual(lb.areaConverter(1, 'square kilometerm', 'square meter'), None)
    


class Test_Area(unittest.TestCase):
    
    def test_areaConverter(self):
        print('Area Cnverter, test random value')
        self.assertEqual(lb.areaConverter(1, 'square km', 'square meter'), 1000000)

    def test_areaConverterNone(self):
        print('Area Converter test for return none')
        self.assertEqual(lb.areaConverter(1, 'square kilometerm', 'square meter'), None)
        
        
        
class Test_Length(unittest.TestCase):
    
    def test_lengthConverter(self):
        print('Length Converter test for random value')
        self.assertEqual(lb.lengthConverter(1, 'km', 'm'), 1000)
    
 

class Test_temp(unittest.TestCase):
    
    def test_temperatureConverter(self):
        print('Temp Converter test for none value')
        self.assertEqual(lb.temperatureConverter(0, 'cel', 'fah'), 32)
        
        
# class Test_form(unittest.TestCase):
# 	form = forms.convertForm(request.POST or None)

# 	def test_form_is_valid(self):
#    		self.assertTrue(form.isvalid())



if __name__ == '__main__':
    unittest.main()