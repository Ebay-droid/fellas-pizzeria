import unittest
import json
import os
from app import create_app,db



class PizzaTestCase(unittest.TestCase):
  '''
  Represents pizza testcase
  '''
  
  def setUp(self):
    self.app = create_app(config_name='testing')
    self.client = self.app.test_client
    self.pizza ={'flavour':'Hawaian'}
    
    with self.app.app_context():
      db.create_all()
      
  def test_pizza_creation(self):
    '''
    test API can create a post request
    '''
    res = self.client().post('/pizzas/', data = self.pizza)
    self.assertEqual(res.status_code,201)
    self.assertIn('Hawaian',str(res.data))
    
    
  def test_api_can_get_all_pizzas(self):
    '''
    test that it can get a pizza
    '''
    res = self.client().post('/pizzas/', data=self.pizza)  
    self.assertEqual(res.status_code, 201)
    res = self.client().get('/pizzas/')
    self.assertEqual(res.status_code, 200)
    self.assertIn('Hawaian',str(res.data))
    
    
  def test_api_can_get_pizzas_by_id(self):
    '''
    test to get a single pizza by id
    '''
    rv = self.client().post('/pizzas/', data=self.pizza)
    self.assertEqual(rv.status_code, 201)
    result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
    result = self.client().get(
          '/pizzas/{}'.format(result_in_json['id']))
    self.assertEqual(result.status_code, 200)
    self.assertIn('Hawaian',str(result.data))
    
  def pizza_can_be_edited(self):
    '''
    testing a put request
    '''  
    rv = self.client().post(
      '/pizzas/',
      data={
        "flavour": "borewores"
      })
    self.assertEqual(rv.status_code,201)
    rv = self.client().put(
      '/pizzas/1',
      data={
        "flavour": "deluxe"
      })
    self.assertEqual(rv.status_code,200)
    results =  self.client().get('/pizzas/1')
    self.assertIn('deluxe',str(results.data))
    
  def test_pizza_deletion(self):
    '''
    test if existing pizza 
    '''
    rv = self.client().post(
      '/pizzas/',
      data ={'flavour':'deluxe'})
    self.assertEqual(rv.status_code,201)
    res = self.client().delete('/pizzas/1') 
    self.assertEqual(res.status_code, 200)
    #test existence 
    result = self.client().get('/pizzas/1')
    self.assertEqual(result.status_code,404)
    
  def tearDown(self):
    '''
    tear down initialized variables
    '''
    with self.app.app_context():
      #dropal tables
      db.session.remove()
      db.drop_all()
    
if __name__ == "__main__":
  unittest.main()      
