import requests
URL = 'https://randomuser.me/api/'
class RandomUser:
    def __init__(self):
        self.data = requests.get(URL).json()['results'][0]

    def get_first_name(self):
        """
        This method returns the first name
        """
        return self.data['name']['first']
    
    def get_last_name(self):
        """
        This method returns the last name
        """
        return self.data['name']['last'] 

    def get_full_name(self):
        """
        This method returns the full name
        """
        return self.data['name']['first'] + ' ' + self.data['name']['last'] 

    def get_email(self):
        """
        This method returns the email
        """
        return self.data['email'] 

    def get_phone(self):
        """
        This method returns the phone
        """
        return self.data['phone'] 

    def get_cell(self):
        """
        This method returns the cell
        """
        return self.data['call']  

    def get_picture(self):
        """
        This method returns the picture
        """
        return self.data['picture']['medium']
    def get_gender(self):
        """
        This method returns the gender
        """
        return self.data['gender'] 
    def get_nationality(self):
        """
        This method returns the nationality
        """
        return self.data['nat'] 
    def get_location(self):
        """
        This method returns the location
        """
        location = {
            'latitude': self.data['location']['coordinates']['latitude'],
            'longitude': self.data['location']['coordinates']['longitude']

        }
        return location
    def get_date(self):
        """
        This method returns the date
        """
        return self.data['dob']['date']
    def get_dob(self):
        """
        This method returns the dob
        """
        return self.data['dob']

    def get_age(self):
        """
        This method returns the age
        """
        return self.data['dob']['age']