from src.url.schemas.UrlSchemas import *

class UrlLocalRepository():

    _ID_MACHINE = "A" # A unique identifier for machine
    _ID_COUNTER = 0 #
    database = {}

    def __init__(self):
        # create local database
        first_id = self.generate_ids()
        self.database = {first_id: {
                "id":first_id,
                "original_url":"https://www.youtube.com/watch?v=o4Hq8ixhOh0",
                "short_url":f"http://localhost/{first_id}"
                }}

    # Basic CRUD
    def createURL(self, url: CreateUrl):
        new_id = self.generateIds()
        
        return None
    
    def getUrlbyId(self, urlId: str):
        return self.database.get(urlId)
    
    def getAllUrls(self):
        return self.database
    
    def updateUrl(self):
        #To Do
        pass

    def deleteUrl(self, urlId: str):
        try:
            return self.database.pop(urlId)
        except KeyError as e:
            return None


    # To do This function must be performed in the database to ensure the identifiers integrity.
    # function that create new ids, schemas ids -> "ID_MACHINE+ID_COUNTER" examples "A0001", "A0002", ...
    def generateIds(self) -> str:
        new_id = self.ID_MACHINE + str(self.ID_COUNTER).zfill(4)
        self.ID_COUNTER += 1
        return new_id
