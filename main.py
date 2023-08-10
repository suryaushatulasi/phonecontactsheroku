def _add_contact(self):
    new_contact = {'name': 'Himansh', 'ph_no': 6789012345}
    response = self.app.post('/insert-contacts', json=new_contact)
    self.assertEqual(response.status_code, 404)
    created_contact = response.get_json()

    self.assertIsInstance(created_contact, dict)
    print(created_contact)
    self.assertEqual(created_contact, {'id': 5, 'name': 'Himansh', 'ph_no': 6789012345})
    self.assertEqual(created_contact['name'], new_contact['name'])
    self.assertEqual(created_contact['ph_no'], 6789012345)
    self.assertEqual(created_contact['id'], 5)