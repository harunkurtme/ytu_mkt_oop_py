from patient import Patient



class RegularPatient(Patient):
    
    def __init__(self, first_name, last_name, ssn, weekly_payment):
        Patient.__init__(self,first_name, last_name, ssn)
        self._weekly_payment = weekly_payment
    
    @property
    def weekly_payment(self):
        return self._weekly_payment
    
    @weekly_payment.setter
    def weekly_payment(self, value):
        self._weekly_payment = value if value > 0 else 0
    
    def calculate_cost(self):
        return self.weekly_payment
    
    def __str__(self) -> str:
        return "RegularPatient: {}, weekly_payment={}".format(super()._repr_(),self.weekly_payment)
    
    def _repr_(self):
        return "RegularPatient: {}, weekly_payment={}".format(super()._repr_(),self.weekly_payment)

        
        
