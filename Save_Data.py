import os
import json
from datetime import datetime
import cv2

class Save_Person_Info:
    def __init__(self) -> None:
        self.pid =len(os.listdir('data'))+1

    def save_image(self,Person_Image=None):
        folder_path = f'data/Person_{self.pid}'
        if not os.path.exists(folder_path):
            # Path to the folder where you want to save the Person Data and Image.
            # Check if the folder exists, if not, create it
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            # Save the image
            image_path = os.path.join(folder_path, 'Person.jpg')
            cv2.imwrite(image_path, Person_Image)
            self.save_Bio()


    def save_Bio(self,Person_id = None, Name =None, Email =None, Contact = None, Age = None):
        if Person_id != None:
            folder_path = f'data/Person_{Person_id}'
            if os.path.exists(folder_path):
                with open(f'data/Person_{Person_id}/data.json', 'r') as file:
                    data = json.load(file)
                data['Name'] = Name
                data['Email'] = Email
                data['Contact'] = Contact
                data['Age'] = Age
                # Path to the JSON file
                file_path = os.path.join(folder_path, 'data.json')

                
            # Save data to the JSON file
                with open(file_path, 'w') as json_file: 
                    json.dump(data, json_file, indent=4)

                return f"Data saved of pid = {Person_id}"
            else:
                return "Person Does not Exists."
        else :
            folder_path = f'data/Person_{self.pid}'
            if os.path.exists(folder_path):
                # Data to be saved in JSON format
                Person_Info = {
                    "Person_id": self.pid,
                    "Name": "XYZ",
                    "Email": "@gmail.com",
                    "Contact": "xxxxxxxxxx",
                    "Age": 0,
                    "Date": 0,
                    "time": 0,
                    "Total_Attendence": 1,
                    "Today_Attendence": True
                }

                # Path to the JSON file
                file_path = os.path.join(folder_path, 'data.json')

                # Save data to the JSON file
                with open(file_path, 'w') as json_file:
                    json.dump(Person_Info, json_file, indent=4)

                return f"Data saved to {folder_path}"
            else:
                return "Connot Make image."

    def Attendence_True(self, Person_id=None):
        folder_path = f'data/Person_{Person_id}'
        if os.path.exists(folder_path):
            with open(f'data/Person_{Person_id}/data.json', 'r') as file:
                data = json.load(file)
            data['Date'] = str(datetime.now().date())
            data['time'] = str(datetime.now().time())
            data['Total_Attendence'] +=1
            data['Today_Attendence'] = True

            # Path to the JSON file
            file_path = os.path.join(folder_path, 'data.json')

            # Save data to the JSON file
            with open(file_path, 'w') as json_file:  # Use 'w' mode instead of 'a' to overwrite existing data
                json.dump(data, json_file, indent=4)

            return f"Data saved to {folder_path}"
        else:
            return "Cannot Make image."
  
    def Attendence_False(self, Person_id=None):
        folder_path = f'data/Person_{Person_id}'
        if os.path.exists(folder_path):
            # Read the JSON file
            with open(f'data/Person_{Person_id}/data.json', 'r') as file:
                data = json.load(file)

            # Update the specific key in the dictionary
            data['Today_Attendence'] = False

            # Save data to the JSON file
            with open(f'data/Person_{Person_id}/data.json', 'w') as file:
                json.dump(data, file, indent=4)

            return f"Data saved to {folder_path}"
        else:
            return "Cannot Make image."
