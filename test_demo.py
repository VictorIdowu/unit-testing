import unittest
import demo

class TestDemo(unittest.TestCase):
  def test_add(self):
    self.assertEqual(demo.add(2,2),4)
    self.assertEqual(demo.add(10,2),12)
    self.assertEqual(demo.add(5,9),14)
  
  def test_sub(self):
    self.assertEqual(demo.sub(2,2),0)
    self.assertEqual(demo.sub(10,2),8)
    self.assertEqual(demo.sub(5,9),-4)

  def test_mul(self):
    self.assertEqual(demo.mul(2,2),4)
    self.assertEqual(demo.mul(10,2),20)
    self.assertEqual(demo.mul(5,9),45)
  
  def test_div(self):
    self.assertEqual(demo.div(2,2),1)
    self.assertEqual(demo.div(10,2),5)
    self.assertEqual(demo.div(21,3),7)



if __name__ == '__main__':
  unittest.main()