from datetime import datetime
import hashlib
import requests

class Forgot_password(object):
    """docstring for Forgot_password"""

    def __init__(self, account, User_birthday):
        super(Forgot_password, self).__init__()
        self.paramString = account + User_birthday                         # Username + User_birthday
        self.account = account                                             # Username
        self.User_birthday = User_birthday                                           # User_birthday
        self.access_token = ""                                             # Token
        self.str1 = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S') # Device Time
        self.str2 = '2.2.0'                                                # App Version
        self.str3 = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')      # Call time
        # You may want to change these accordingly
        self.ModelId = 'MIX 3'                                             # Model ID
        self.OsVersion = '9'                                               # Android OS Version
        self.Platform = 'Android'                                          # Platform
        self.DeviceUuid = 'device_uuid'                                    # Device UUID; can be any string
        self.OrderNo = self.DeviceUuid + self.str3                         # Order No
        self.cardNo = 'cardNo'                                             # Card NO

    def Change_password(self):
        # Mask = MD5('Mc' + OrderNo + Platform + OsVersion + ModelId + DeviceUuid + str1 + str2 + paramString + 'Donalds')
        data = 'Mc%s%s%s%s%s%s%s%sDonalds' % (
            self.OrderNo,
            self.Platform,
            self.OsVersion,
            self.ModelId,
            self.DeviceUuid,
            self.str1,
            self.str2,
            self.paramString
        )
        mask = hashlib.md5()
        mask.update(data.encode('utf-8'))    

        json = {
            "account" : self.account,
            "birthday": self.User_birthday,
            "OrderNo" : self.OrderNo,
            "mask"    : mask.hexdigest(),
            "source_info": {
                "app_version": self.str2,
                "device_time": self.str1,
                "device_uuid": self.DeviceUuid,
                "model_id"   : self.ModelId,
                "os_version" : self.OsVersion,
                "platform"   : self.Platform,
            }
        }

        # Get the response
        response = requests.post('https://api.mcddaily.com.tw/forget_password', json = json).text

        # Clean the garbage date
        response = response.replace('null', '""')
        response = response.replace('true', '"true"')
        response = response.replace('false', '"false"')

        # Convert the string to dictionary type
        response = eval(response)

        # Return the dictionary type of response
        return response

# Python 3.8.0 update
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y/%m/%d')
        atvice = False
    except:
        print("Incorrect data format, should be YYYY/MM/DD")
        atvice = True


def Main():
    # User login date
    Username = input('Username : ')
    User_birthday = input('Birthday : ')

    # Login and print login information 
    Account = Forgot_password(Username, User_birthday)
    list = Account.Change_password()

    # Print the results
    print('')
    print('Login status : ' + list['rm'])

if __name__ == '__main__':
    Main()
