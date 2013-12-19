'''
Open311 API Library

'''
import requests

print ('In open311')
class serviceList:
    def __init__(self,ID, Key):
        
        '''
        Creating Object:

        obj = Open311SNSL.serviceList('API ID ','API Key')

        obj = Open311SNSL.serviceList('12345','987654')
        '''
        self.id = ID
        self.key = Key



        #Content Type Constants
        self.json = 'json'
        self.xml = 'xml'
        #Service List Constants
        self.s_all = 'all'
        self.s_Business = 'Business'
        self.s_Civic_Services = 'Civic Services'
        self.s_Culture_and_Recreation = 'Culture and Recreation'
        self.s_Education = 'Education'
        self.s_Environment = 'Environment'
        self.s_Health = 'Health'
        self.s_Housing_and_Development = 'Housing and Development'
        self.s_Public_Safety = 'Public Safety'
        self.s_Social_Services = 'Social Services'
        self.s_Transportation = 'Transportation'

        
    def validation(self,statusCode, category):
        '''
        Validates whether the search was successful or not.

        '''
        if statusCode == 403:
            print ('Error Code:403 \n Make sure your APP ID/APP Key and Category are correct')
            print ('APP ID: ', self.id,'  App Key: ',self.key , '  Category: ', category)
    
        elif statusCode == 0:
            print ('Error Code:0 \n Make sure your firewall isn\'t blocking any connections')
        
        elif statusCode == 200:
            return True

        
    def getID(self):
        '''
        (Check to make sure the ID entered for an object was correct)

        (Example)

        object.getID()
            ==> Returns the ID number for object
        '''
        print (self.id)
        return self.id

    def getKey(self):
        '''
        (Check to make sure the Key entered for an object was correct)

        (Example)

        object.getKey()
            ==> Returns the key for object
        '''
        print (self.key)
        return self.key

    def setID(self, newID):
        '''
        (Set a new ID for an object)

        (Example)

        object.setID(12345)
            ==> Assigns a new ID number(12345) to the object
        '''
        self.id = newID
        print (self.id)

    def setKey(self,newKey):
        '''
        (Set a new key for an object)

        (Example)

        object.setKey(56789)
            ==> Assigns a new key number(56789) to the object
        '''
        self.key = newKey
        print (self.key)



    def getServiceList(self,serviceFilter , contentType):
        '''
        (Call to search for a specific service/list)

        (Examples)
        
        OBJECT.getServiceList(OBJECT.s_all, OBJECT.json)
                ==> Searches for all services in the service list : Output JSON

        object.getServiceList(object.s_web , OBJECT.xml)
                ==> Searches for "web" in the service list : Output XML


        (Service List Filters)
        
        self.s_all
                    ==> Search 'all'
        self.s_Environment_Sanitation
                    ==> Search 'Environment and Sanitation'
        self.s_Property_Building_Home
                    ==> Search 'Property, Buildings and Homes'
        self.s_Education_Employment
                    ==> Search 'Education and Employment'
        self.s_Business_Finance
                    ==> Search 'Business and Finance'
        self.s_Social_Services
                    ==> Search 'Social Services'
        self.s_Health_Medicine
                    ==> Search 'Health and Medicine'
        self.s_PubSafe_Law
                    ==> Search 'Public Safety and Law'
        self.s_Gov_Civ_Services
                    ==>  'Search Government and Civil Services'
					
		
		self.s_Business
					==> Search 'Business'
        self.s_Civic_Services 
					==> Search 'Civic Services'
        self.s_Culture_and_Recreation 
					==> Search 'Culture and Recreation'
        self.s_Education
					==> Search 'Education'
        self.s_Environment
					==> Search 'Environment'
        self.s_Health
					==> Search 'Health'
        self.s_Housing_and_Development 
					==> Search 'Housing and Development'
        self.s_Public_Safety
					==> Search 'Public Safety'
		self.s_Social_Services
					==> Search 'Social Services'
		self.s_Transportation
					==> Search 'Transportation'
        '''
        if contentType == self.json:
            self.r = requests.get("https://api.cityofnewyork.us/311/v1/services/"+
                         serviceFilter + '.json'
                         "?app_id="+self.id+
                         "&app_key="+self.key)
            
        elif contentType == self.xml:
            self.r = requests.get("https://api.cityofnewyork.us/311/v1/services/"+
                         serviceFilter + '.xml'
                         "?app_id="+self.id+
                         "&app_key="+self.key)

        self.sCode = self.r.status_code
        print (self.sCode)
        self.validator = self.validation(self.sCode , serviceFilter)
        if self.validator == True:           
            return self.r
        
class service:
    def __init__(self, ID, Key, service_id):
        '''
        (Creating Service Object)

        obj = Open311SNSL.service('API ID ','API Key','serv_id')

        obj = Open311SNSL.service('12345','987654','20-4-7')
        '''
        self.id = ID
        self.key = Key
        self.servID = service_id

        #Content Type Constants
        self.json = 'json'
        self.xml = 'xml'
        
    def getService(self,contentType):
        '''
        (Search service based on service ID)

        (Examples)
        
        object.getService(object.json)
                ==> Searches for service based on ID : Output JSON
        object.getService(object.xml)
                ==> Searches for service based on ID : Output XML

        '''

        if contentType == self.json:
            self.r = requests.get("https://api.cityofnewyork.us/311/v1/services/"+
                         self.servID + '.json'
                         "?app_id="+self.id+
                         "&app_key="+self.key)
            
        elif contentType == self.xml:
            self.r = requests.get("https://api.cityofnewyork.us/311/v1/services/"+
                         self.servID + '.xml'
                         "?app_id="+self.id+
                         "&app_key="+self.key)

        self.sCode = self.r.status_code
        print (self.sCode)
        self.validator = self.validation(self.sCode)
        if self.validator == True:
            return self.r

    def validation(self,statusCode):
        '''
        Validates whether the search was successful or not.

        '''
        if statusCode == 403:
            print ('Error Code:403 \n Make sure your APP ID/APP Key and Category are correct')
            print ('APP ID: ', self.id,'  App Key: ',self.key , 'Service ID',self.servID)
    
        elif statusCode == 0:
            print ('Error Code:0 \n Make sure your firewall isn\'t blocking any connections')
        
        elif statusCode == 200:
            return True

