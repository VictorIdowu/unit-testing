import unittest
import demo

class TestCalculate(unittest.TestCase):
  def setUp(self):
    self.calculate = demo.Calculate()
  
  def tearDown(self):
    print("Tear down")
  
  def test_add(self):
    self.assertEqual(self.calculate.add(2,2),4)
    self.assertEqual(self.calculate.add(10,2),12)
    self.assertEqual(self.calculate.add(5,9),14)

  def test_sub(self):
    self.assertEqual(self.calculate.sub(2,2),0)
    self.assertEqual(self.calculate.sub(10,2),8)
    self.assertEqual(self.calculate.sub(5,9),-4)

  def test_mul(self):
    self.assertEqual(self.calculate.mul(2,2),4)
    self.assertEqual(self.calculate.mul(10,2),20)
    self.assertEqual(self.calculate.mul(5,9),45)
  
  def test_div(self):
    self.assertEqual(self.calculate.div(2,2),1)
    self.assertEqual(self.calculate.div(10,2),5)
    with self.assertRaises(ValueError):
      self.calculate.div(10,0)
  

if __name__ == '__main__':
  unittest.main()