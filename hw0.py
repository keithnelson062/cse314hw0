from faker import Faker
import pandas as pd
from random import shuffle, seed
from faker.providers.person.en import Provider
fake = Faker()

column = ['First_Names', 'Last_Names', 'Addresses', 'Phone_Numbers']


first_names = list(set(Provider.first_names))

seed(466348)
shuffle(first_names)

print(first_names[0:1000])
T_firstname = first_names[0:1000]

data = {
  "First_Names": T_firstname,
  "Last_Names": None,
  "Addresses": None, 
  "Phone_Numbers": None

}
fake_data = pd.DataFrame(data)

#fake_data = pd.DataFrame(first_names, columns=column)

fake_data.to_csv('fake_data.csv', index=False)