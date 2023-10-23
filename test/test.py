import unittest
import os
from flask import Flask, request

class FileUploadTestCase(unittest.TestCase):
    def test_file_upload(self):
        with self.app.test_client() as client:
            with open('test_file.txt', 'w') as f:
                f.write('Test data')
            response = client.post('/upload', data={'file': open('test_file.txt', 'rb')})
            self.assertEqual(response.data.decode(), 'File upload successful')
            os.remove('test_file.txt')