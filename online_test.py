import re


RE_phone = re.compile("^[a-z0-9]{10}$")
class Contacts:

	name = ""
	email = ""
	phone = ""

	contactList = [{"name":'Alice Brown', "email":'', "phone":'1231112223'},
		    {"name":'Bob Crown', "email":'bob@crowns.com', "phone":''},
		    {"name":'Carlos Drew', "email":'carl@drewess.com', "phone":'3453334445'},
		    {"name":'Doug Emerty', "email":'', "phone":'4564445556'},
		    {"name":'Egan Fair', "email":'eg@fairness.com', "phone":'5675556667'}]

	def add_contact_list(self, name="", email="", phone=""):
		if phone:
			phone_number = phone.lower()
			if not RE_phone.match(phone_number):
				raise ValueError("%s is not a valid Phone number." % phone)

		self.contactList.append({"name": name, "email": email, "phone": phone_number})
		print("##################",self.contactList)

	def check_existence_and_add_in_contact(self, data, leadList):
		registrant_data = data.get('registrant')
		contactList = self.contactList
		exists = True
		for contact_dict in contactList:
			if registrant_data['email'] == contact_dict['email']:
				exists = False
				if not contact_dict['phone']:
					contact_dict['phone'] = registrant_data['phone']
				if not contact_dict['name']:
					contact_dict['name'] = registrant_data['name']
				
			else:
				if registrant_data['phone'] == contact_dict['phone']:
					exists = False
					if not contact_dict['email']:
						contact_dict['email'] = registrant_data['email']
					if not contact_dict['name']:
						contact_dict['name'] = registrant_data['name']
				else:
					for lead_dict in leadList:
						if registrant_data['email'] == lead_dict['email']:
							leadList.remove(lead_dict)
							
							self.add_contact_list(registrant_data['name'],registrant_data['email'],registrant_data['phone'])
							exists = False
							break
						else:
							if registrant_data['phone'] == lead_dict['phone']:
								leadList.remove(lead_dict)
								self.add_contact_list(registrant_data['name'],registrant_data['email'],registrant_data['phone'])
								exists = False
								break

		if exists:
			self.add_contact_list(registrant_data['name'],registrant_data['email'],registrant_data['phone'])
			
		print("@@@@@@@@",leadList,self.contactList)


class Leads:

	name = ""
	email = ""
	phone = ""

	leadList = [{"name": '', "email": 'kevin@keith.com', "phone": ''},
		    {"name": 'Lucy', "email": 'lucy@liu.com', "phone": '3210001112'},
		    {"name": '', "email": 'mary@middle.com', "phone": '3331112223'},
		    {"name": '', "email": '', "phone": '4442223334'},
		    {"name": '', "email": 'ole@olson.com', "phone": ''}]

	def add_lead_list(self, name="", email="", phone=""):
		if phone:
			phone_number = phone.lower()
			if not RE_phone.match(phone_number):
				raise ValueError("%s is not a valid Phone number." % phone)

		self.leadList.append({"name": name, "email": email, "phone": phone_number})


contactObj = Contacts()

leadObj = Leads()
leadList = leadObj.leadList
print("!!!!!!!!!!!!!!!!!",leadList)
print("%%%%%%%%%%%%%%$",contactObj.contactList)
data = {
	  "registrant": 
	     { 
		"name": "Lucy", 
		"email": "lucy@liu.com",
		"phone": "3210001112",
	     }
	}
contactObj.check_existence_and_add_in_contact(data,leadList)










