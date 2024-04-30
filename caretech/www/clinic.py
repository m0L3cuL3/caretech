import frappe

def get_context(context):
    clinic = frappe.get_doc('Clinic Settings')
    doctor = frappe.get_all('Doctor', fields=['*'])
    context.name = clinic.clinic_name
    context.address = clinic.address
    context.phone_number = clinic.phone_number
    context.schedule = clinic.clinic_schedule

    context.doctors = doctor