import requests
URL = 'https://randomuser.me/api/'
class RandomUser:
    def __init__(self):
        self.data = requests.get(URL).json()


    def get_first_name(self):
        """
        This method returns the first name
        """
        return self.data['results'][0]['name']['first']
    
    def get_last_name(self):
        """
        This method returns the last name
        """
        pass 

    def get_full_name(self):
        """
        This method returns the full name
        """
        pass 

    def get_email(self):
        """
        This method returns the email
        """
        pass 

    def get_phone(self):
        """
        This method returns the phone
        """
        pass 

    def get_cell(self):
        """
        This method returns the cell
        """
        pass 

    def get_picture(self):
        """
        This method returns the picture
        """
        pass
    def get_gender(self):
        """
        This method returns the gender
        """
        pass
    def get_nationality(self):
        """
        This method returns the nationality
        """
        pass
    def get_location(self):
        """
        This method returns the location
        """
        pass
    def get_date(self):
        """
        This method returns the date
        """
        pass
    def get_dob(self):
        """
        This method returns the dob
        """
        pass

    def get_age(self):
        """
        This method returns the age
        """
        pass