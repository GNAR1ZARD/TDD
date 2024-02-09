# test_counter.py

"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app 

# we need to import the file that contains the status codes
from src import status 

class CounterTest(TestCase):
    """Counter tests"""
    
    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        
    def setUp(self):
         self.client = app.test_client()    
         
    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)
    
    # Update test_counter.py:    
    def test_update_a_counter(self):
        """It should update a counter"""
        # Create a counter
        create_result = self.client.post('/counters/updateTest')
        self.assertEqual(create_result.status_code, status.HTTP_201_CREATED)
        
        # Check the baseline counter value
        baseline_result = self.client.get('/counters/updateTest')
        self.assertEqual(baseline_result.status_code, status.HTTP_200_OK)
        baseline_counter = baseline_result.json['updateTest']
        self.assertEqual(baseline_counter, 0)

        # Update the counter
        update_result = self.client.put('/counters/updateTest')
        self.assertEqual(update_result.status_code, status.HTTP_200_OK)
        
        # Check the updated counter value
        updated_result = self.client.get('/counters/updateTest')
        updated_counter = updated_result.json['updateTest']
        self.assertEqual(updated_counter, baseline_counter + 1)
        
    def test_read_a_counter(self):
        """It should read a counter"""
        # Create a counter
        create_result = self.client.post('/counters/readTest')
        self.assertEqual(create_result.status_code, status.HTTP_201_CREATED)
        
        # Read the counter
        read_result = self.client.get('/counters/readTest')
        self.assertEqual(read_result.status_code, status.HTTP_200_OK)
        counter_value = read_result.json['readTest']
        self.assertEqual(counter_value, 0)

