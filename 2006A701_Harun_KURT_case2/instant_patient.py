from patient import Patient


class InstantPatient(Patient):
    def __init__(self, first_name, last_name, ssn, hours, payment_per_hour):
        Patient.__init__(self,first_name, last_name, ssn)
        self._hours = hours
        self._payment_per_hour = payment_per_hour
    
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        self._hours = value if 0 <= value <= 168 else 0
    
    @property
    def payment_per_hour(self):
        return self._payment_per_hour
    
    @payment_per_hour.setter
    def payment_per_hour(self, value):
        self._payment_per_hour = value if value > 0 else 0
    
    def calculate_cost(self)->str:
        overtime_hours = max(self.hours - 40, 0)
        overtime_pay = overtime_hours * self.payment_per_hour * 1.5
        return str(overtime_pay + self.hours * self.payment_per_hour)
    
    def __str__(self)->str:
        return "InstantPatient: {} hours={}, payment_per_hour={}".format(super()._repr_(),self.hours,self.payment_per_hour)
    
    def _repr_(self):
        return "InstantPatient: {}, hours={}, payment_per_hour={}".format(super()._repr_(),self.hours,self.payment_per_hour)