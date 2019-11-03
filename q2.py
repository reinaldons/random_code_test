from collections import namedtuple


def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """
    patient_attrs = {}
    for record in records:
        patient_attrs.update(record._asdict())

    Patient = namedtuple('Patient', patient_attrs.keys())
    patient = Patient(**patient_attrs)

    return patient


PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth='06-04-1972')

Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color='Blue', hair_color='Black')

print(merge(personal_details, complexion))
