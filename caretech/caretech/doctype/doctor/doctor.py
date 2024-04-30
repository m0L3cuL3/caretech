# Copyright (c) 2024, Sean Baang and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Doctor(Document):
	def validate(self):
		self.set_full_name()

	def set_full_name(self):
		if self.middle_initial == None:
			self.full_name = self.first_name + ' ' + self.last_name
		else:
			self.full_name = self.first_name + ' ' + self.middle_initial + ' ' + self.last_name
			