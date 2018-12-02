import Persons

if __name__ == "__main__":
  raise Exception("This file is not meant to run by itself")

# --- Make child class ---
class Customer(Persons.Person):
  def __init__(self, Id=""):
    # Attributes
    self.__Id = Id

  # --Properties--
  # Id
  @property  # getter(accessor)
  def Id(self):
    return self.__Id

  @Id.setter  # (mutator)
  def Id(self, Value):
    self.__Id = Value

  # --Methods--

  def ToString(self):
    """Explictly returns field data"""
    strData = super().ToString()
    return str(self.Id) + ',' + strData

  def __str__(self):
    """Implictly returns field data"""
    return self.ToString()
  # --End of Class Customer --

class CustomerList(object):
  __lstCustomers = []

  @staticmethod
  def AddCustomer(Customer):
    if str(Customer.__class__) == "<class 'Customers.Customer'>":
      CustomerList.__lstCustomers.append(Customer)
    else:
      raise Exception("Only Customer objects can be added to the CustomerList.")

  def ToString():
    strData = "Id,FirstName,LastName\n"
    for customer in CustomerList.__lstCustomers:
      strData += str(customer.Id) + "," + customer.FirstName + "," + customer.LastName + "\n"
    return strData