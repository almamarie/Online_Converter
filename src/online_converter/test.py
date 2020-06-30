import unittest
import backend as lb

class Test_Backend(unittest.TestCase):

    def test_weightConverter(self):
        print('Weight Converter')
        self.assertEqual(lb.weightConverter(1, 'kg', 'g'), 1000)


    def test_lengthConverter(self):
        print('Length Converter')
        self.assertEqual(lb.lengthConverter(1, 'km', 'm'), 1000)


    def test_temperatureConverter(self):
        print('Temp COnverter')
        self.assertEqual(lb.temperatureConverter(0, 'cel', 'fah'), 32)


    def test_areaConverter(self):
        print('Area COnverter')
        self.assertEqual(lb.areaConverter(1, 'square km', 'square meter'), 1000000)



if __name__ == '__main__':
    unittest.main()