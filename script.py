# from faker import Faker
from faker import *
import os
import time
import webbrowser as wb
from termcolor import colored

def ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE():
    os.system('cls')
    print("""
 _  ______      _           
(_)(______)    (_) _   ____ 
 _ (_)__  ____ (_)(_) (____)
(_)(____)(____)(___) (_)_(_)
(_)(_)  ( )_( )(_)(_)(__)__ 
(_)(_)   (__)_)(_) (_)(____)
                            
      by ZeaCeR#5641

help - will take you to the menu will all commands
    """)
    commandcs = input("command>> ")
    if commandcs.lower() == "start high":
        os.system('cls')
        print("""
Supported Localized Providers: 

ar_AA, ar_EG, ar_JO, ar_PS, ar_SA, bg_BG, bs_BA, cs_CZ, da_DK, de, de_AT, 
de_CH, de_DE, dk_DK, el_CY, el_GR, en, en_AU, en_CA, en_GB, en_IE, en_IN, 
en_NZ, en_PH, en_TH, en_US, es, es_CA, es_ES, es_MX, et_EE, fa_IR, fi_FI, 
fil_PH, fr_CA, fr_CH, fr_FR, fr_QC, ga_IE, he_IL, hi_IN, hr_HR, hu_HU, hy_AM, 
id_ID, it_CH, it_IT, ja_JP, ka_GE, ko_KR, la, lb_LU, lt_LT, lv_LV, mt_MT, 
ne_NP, nl_BE, nl_NL, no_NO, or_IN, pl_PL, pt_BR, pt_PT, ro_RO, ru_RU, sk_SK, 
sl_SI, sv_SE, ta_IN, th, th_TH, tl_PH, tr_TR, tw_GH, uk_UA, zh_CN, zh_TW
        """)
        mantype = input("\n[*] Enter the localized provider: ")
        fakeus = Faker(mantype)
        how_many = int(input("[*] Number of profiles: "))
        for i in range(how_many):
            
            USname = fakeus.name()

            # credit card gen
            # UScreditcardprovider = fakeus.credit_card_provider()
            # UScreditcardnumber = fakeus.credit_card_number()
            # UScreditcardSecurityCode = fakeus.credit_card_security_code()
            # UScreditcardExpire = fakeus.credit_card_expire()

            shitng = i + 1
            file = open(str(shitng) + "-" +USname + ".txt", 'w+', encoding="utf8")

            try:
                print("\n\nName: " + USname)
                file.write("Name: " + USname)
            except:
                print("")
                file.write("\n")
            # date of birth
            try:
                USdob = fakeus.date_of_birth()
                print("DOB: " + str(USdob))
                file.write("\nDOB: " + str(USdob))
            except:
                print("")
                file.write("\n")
            # city
            try:
                UScity = fakeus.city()
                print("City: " + UScity)
                file.write("\nCity: " + UScity)
            except:
                print("")
                file.write("\n")
            # address
            try:
                USaddress= fakeus.address()
                print("Address: " + USaddress)
                file.write("\nAddress: " + USaddress)
            except:
                print("")
                file.write("\n")
            # job
            try:
                USjob = fakeus.job()
                print("Job: " + USjob)
                file.write("\nJob: " + USjob)
            except:
                print("")
                file.write("\n")
            # favourite color
            try:
                USfavColor = fakeus.color_name()
                print("Fav Color: " + USfavColor)
                file.write("\nFav Color: " + USfavColor)
            except:
                print("")
                file.write("\n")
            # zipcode
            try:
                USzip = fakeus.zipcode()
                print("ZIP code: " + USzip)
                file.write("\nZIP code: " + USzip)
            except:
                print("")
                file.write("\n")
            # license plate
            try:
                USnumberPlate = fakeus.license_plate()
                print("Number Plate: " + USnumberPlate)
                file.write("\nNumber Plate: " + USnumberPlate)
            except:
                print("")
                file.write("\n")
            # basic bank account number
            try:
                USbasicBankAccountNumber = fakeus.bban()
                print("Basic Bank Account Number: " + USbasicBankAccountNumber)
                file.write("\nBasic Bank Account Number: " + USbasicBankAccountNumber)
            except:
                print("")
                file.write("\n")
            # international bank account number
            try:
                USinternationalBankAccountNumber = fakeus.iban()
                print("International Bank Account Number: " + USinternationalBankAccountNumber)
                file.write("\nInternational Bank Account Number: " + USinternationalBankAccountNumber)
            except:
                print("")
                file.write("\n")
            # degree / bs
            try:
                USbs = fakeus.bs()
                print("BS: " + USbs)
                file.write("\nBS: " + USbs)
            except:
                print("")
                file.write("\n")
            # company
            try:
                UScompany = fakeus.company()
                print("Company: " + UScompany)
                file.write("\nCompany: " + UScompany)
            except:
                print("")
                file.write("\n")
            # credit card full details ( this not connected to the above mentioned profile)
            try:
                UScreditcard = fakeus.credit_card_full()
                print("Credit Card Full: " + UScreditcard)
                file.write("\nCredit Card Full: \n" + UScreditcard)
            except:
                print("")
                file.write("\n")
            # company email
            try:
                UScompanyemail = fakeus.company_email()
                print("Company Email: " + UScompanyemail)
                file.write("\nCompany Email: " + UScompanyemail)
            except:
                print("")
                file.write("\n")
            # phone number
            try:
                USphoneNumber = fakeus.phone_number()
                print("Phone Number: " + USphoneNumber)
                file.write("\nPhone Number: " + USphoneNumber)
            except:
                print("")
                file.write("\n")
            # personal email
            try:
                USpersonalmail = fakeus.ascii_free_email()
                print("Personal Email: " + USpersonalmail)
                file.write("\nPersonal Email: " + USpersonalmail)
            except:
                print("")
                file.write("\n")
            # catch phrase
            try:
                UScatchPhrase = fakeus.catch_phrase()
                print("Catch Phrase: " + UScatchPhrase)
                file.write("\nCatch Phrase: " + UScatchPhrase)
            except:
                print("")
                file.write("\n")
            # ssn
            try:
                USssa = fakeus.ssn()
                print("SSA: " + USssa)
                file.write("\nSSA: " + USssa)
            except:
                print("")
                file.write("\n")
            # user agent ( only chrome )
            try:
                USuseragent = fakeus.chrome()
                print("User Agent: " + USuseragent + "\n\n")
                file.write("\nUser Agent: " + USuseragent)
            except:
                print("")
                file.write("\n")

        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()

    
    elif commandcs.lower() == "credits":
        os.system('cls')
        print(colored(""" 
███████╗███████╗ █████╗  ██████╗███████╗██████╗ 
╚══███╔╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
  ███╔╝ █████╗  ███████║██║     █████╗  ██████╔╝
 ███╔╝  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
███████╗███████╗██║  ██║╚██████╗███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
                                                
             Made by ZeaCeR#5641
   This is made for educational purposes only!
         """, 'green'))
        creditssubc = input("credits>> ")
        creditssubcl = creditssubc.lower()
        if creditssubcl == "menu":
            ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()
        else:
            print(colored("Please enter a valid input!", 'red'))
            time.sleep(3)
            ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()

    elif commandcs.lower() == "clear":
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()

    elif commandcs.lower() == "cls":
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()
    
    elif commandcs.lower() == "start mid":
        fake_mid = Faker()
        number_of_times_sp = int(input("[*] Number of profiles: "))
        for g in range(number_of_times_sp):
            simple_dict = fake_mid.profile()
            print("\nName: " + simple_dict['name'])
            print("Job: " + simple_dict['job'])
            print("DOB: " + str(simple_dict['birthdate']))
            print("Company: " + simple_dict['company'])
            print("SSN: " + simple_dict['ssn'])
            print("Residence: " + simple_dict['residence'])
            print("Current Location: " + str(simple_dict['current_location']))
            print("Blood Group: " + simple_dict['blood_group'])
            print("Username: " + simple_dict['username'])
            print("Address: " + simple_dict['address'])
            print("eMail: " + simple_dict['mail'] + "\n\n")

            i_sp = g + 1
            file_simple = open(str(i_sp) + "-" + simple_dict['name'] + ".txt", 'w+', encoding="utf8")
            file_simple.write("Name: " + simple_dict['name'])
            file_simple.write("\nJob: " + simple_dict['job'])
            file_simple.write("\nDOB: " + str(simple_dict['birthdate']))
            file_simple.write("\nCompany: " + simple_dict['company'])
            file_simple.write("\nSSN: " + simple_dict['ssn'])
            file_simple.write("\nResidence: " + simple_dict['residence'])
            file_simple.write("\nCurrent Location: " + str(simple_dict['current_location']))
            file_simple.write("\nBlood Group: " + simple_dict['blood_group'])
            file_simple.write("\nUsername: " + simple_dict['username'])
            file_simple.write("\nAddress: " + simple_dict['address'])
            file_simple.write("\neMail: " + simple_dict['mail'])
            file_simple.close()

        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()


    elif commandcs.lower() == "start low":
        fake_low = Faker()
        number_of_times_vsp = int(input("[*] Number of profiles: "))
        for h in range(number_of_times_vsp):
            shitthing_simple = fake_low.simple_profile()

            print("\nName: " + shitthing_simple['name'])
            print("Username: " + shitthing_simple['username'])
            print("Sex: " + shitthing_simple['sex'])
            print("Address: \n" + shitthing_simple['address'])
            print("Mail: " + shitthing_simple['mail'])
            print("Birdthday: " + str(shitthing_simple['birthdate']))

            i_vsp = h + 1
            file_verySimple = open(str(i_vsp) + "-" + shitthing_simple['name'] + ".txt", 'w+', encoding="utf8")
            file_verySimple.write("\nName: " + shitthing_simple['name'])
            file_verySimple.write("\nUsername: " + shitthing_simple['username'])
            file_verySimple.write("\nSex: " + shitthing_simple['sex'])
            file_verySimple.write("\nAddress: \n" + shitthing_simple['address'])
            file_verySimple.write("\nMail: " + shitthing_simple['mail'])
            file_verySimple.write("\nBirthday: " + str(shitthing_simple['birthdate']))
            file_verySimple.close()

        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()


    
    elif commandcs.lower() == "cc all":
        fake_ccall = Faker()
        how_many_cc_all = int(input("\n[*] Number of CC: "))
        for q in range(how_many_cc_all):
            FAKE_CC_ALL = fake_ccall.credit_card_full()
            print(FAKE_CC_ALL)

            q_acc = q + 1
            file_cc_all = open(str(q_acc) + "-CC_ALL.txt", 'w+', encoding="utf8")
            file_cc_all.write(FAKE_CC_ALL)
            file_cc_all.close()

        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()

    elif commandcs.lower() == "cc pr":
        fake_ccpr = Faker()
        how_many_cc_pr = int(input("\n[*] Number of CC Providers: "))

        file_cc_prw = open("CC_PROVIDERS.txt", 'w', encoding="utf8")
        file_cc_prw.write("CC Providers - \n")
        file_cc_prw.close()

        file_cc_pr = open("CC_PROVIDERS.txt", 'r+', encoding="utf8")

        for a in range(how_many_cc_pr):
            FAKE_CC_PR = fake_ccpr.credit_card_provider()
            print(FAKE_CC_PR)
            file_cc_pr.write("\n" + FAKE_CC_PR)

        file_cc_pr.close()

        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()

    elif commandcs.lower() == "cc no":
        fake_ccno = Faker()
        how_many_cc_no = int(input("\n[*] Number of CC Numbers: "))

        file_cc_now = open("CC_NUMBERS.txt", 'w', encoding="utf8")
        file_cc_now.write("CC Numbers - \n")
        file_cc_now.close()

        file_cc_no = open("CC_NUMBERS.txt", 'r+', encoding="utf8")
        
        for a in range(how_many_cc_no):
            FAKE_CC_NO = fake_ccno.credit_card_number()
            print(FAKE_CC_NO)
            file_cc_no.write("\n" + FAKE_CC_NO)
        
        file_cc_no.close()

        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()

    elif commandcs.lower() == "cc cvv":
        fake_cccvv = Faker()
        how_many_cc_no = int(input("\n[*] Number of CC CVV: "))
        
        file_cc_cvvw = open("CC_CVV.txt", 'w+', encoding="utf8")
        file_cc_cvvw.write("CC CVV - \n")
        file_cc_cvvw.close()

        file_cc_cvv = open("CC_CVV.txt", 'r+', encoding="utf8")

        for b in range(how_many_cc_no):
            FAKE_CC_CVV = fake_cccvv.credit_card_security_code()
            print(FAKE_CC_CVV)
            file_cc_cvv.write("\n" + FAKE_CC_CVV)

        file_cc_cvv.close()
        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()
    
    elif commandcs.lower() == "cc exp":
        fake_ccexp = Faker()
        how_many_cc_exp = int(input("[*] Number of CC CVV: "))

        file_cc_expw = open("CC_EXPIRES_DATES.txt", 'w+', encoding="utf8")
        file_cc_expw.write("CC EXPIRE DATES - \n")
        file_cc_expw.close()

        file_cc_exp = open("CC_EXPIRES_DATES.txt", 'r+', encoding="utf8")

        for o in range(how_many_cc_exp):
            FAKE_CC_EXP = fake_ccexp.credit_card_expire()
            print(FAKE_CC_EXP)
            file_cc_exp.write("\n" + FAKE_CC_EXP)
        file_cc_exp.close()

        print(colored("[+] Done!", 'green'))
        time.sleep(3)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()
    
    elif commandcs.lower() == "cc checke":
        # os.system('cls')
        print(colored("\n[+] Opening the tool! Please Wait..", 'green'))
        time.sleep(3)
        url_cc_check = "http://eldersc0de.top/card/ccn1/"
        wb.open(url_cc_check)
    
    elif commandcs.lower() == "cc gene":
        print(colored("\n[+] Opening the tool! Please Wait..", 'green'))
        time.sleep(3)
        url_cc_gene = "https://namso-gen.com/"
        wb.open(url_cc_gene)

    elif commandcs.lower() == "cc check": # This code is contributed by rutvik_56
        def checkLuhn(cardNo):

            nDigits = len(cardNo)
            nSum = 0
            isSecond = False

            for i in range(nDigits - 1, -1, -1):
                d = ord(cardNo[i]) - ord('0')

                if (isSecond == True):
                    d = d * 2
                
                # We add two digits to handle
                # cases that make two digits after
                # doubling
                nSum += d // 10
                nSum += d % 10

                isSecond = not isSecond

            if (nSum % 10 == 0):
                return True
            else:
                return False
        
        if __name__=="__main__":
            # "79927398713"
            cardNo = input("\n[+] Enter the card number: ")
            
            if (checkLuhn(cardNo)):
                print(colored("\nThis is a valid card", 'green'))
            else:
                print(colored("\nThis is not a valid card", 'red'))
        
        time.sleep(5)
        os.system('cls')
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()

    elif commandcs.lower() == "help":
        os.system('cls')
        print("""
( These work only in the main page! )
Command - Function
help - will take you to this page
start high - generate profiles with high information
             and has a fature to select the nationality
             eg - en_US
start mid - generate profiles with normal information
start low - generates profiles with low information
cc all - generate Random Fake Credit Card with all information
cc pr - generate Credit Card Providers
cc no - generate Credit Card Numbers
cc cvv - generate Random Credit Card CVVs
cc exp - generate Random Expiry Dates for Credit Cards
cc gene - take you to an external CC generator
cc check - will use the 'modulo 10' algorithm to check 
           weather the Number is valid ( this is offline )
cc checke - tak you do an external CC checking website
credits - take you to the credits page

( when you are in other pages)
menu - to go to the main page ( beacuse all the other commands work there)

        """)
        subcmdhelp = input("help>> ")
        if subcmdhelp.lower() == "menu":
            ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()
        else:
            print(colored("\n[-] Enter a Valid Command!\nYou will be redirected to the home page now!", 'red'))
            time.sleep(3)
            ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()
    
    else:
        print(colored("+ The term you entered is not recognized as a command of this program! \nMaybe, check for any spelling mistakes in what you typed and try again!\n\nWhat you entered: " + commandcs.lower() + "\n\n+ The program will start again in 5 seconds!", 'red'))
        time.sleep(3)
        ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()


def FAKE_PROFILE_SIMPLE():
    fake = Faker()
    number_of_times_sp = int(input("[*] Number of profiles :"))
    for i in range(number_of_times_sp):
        simple_dict = fake.profile()
        print("\n" + simple_dict['name'])
        print(simple_dict['job'])
        print(str(simple_dict['birthdate']))
        print(simple_dict['company'])
        print(simple_dict['ssn'])
        print(simple_dict['residence'])
        print(simple_dict['current_location'])
        print(simple_dict['blood_group'])
        print(simple_dict['username'])
        print(simple_dict['address'])
        print(simple_dict['mail'] + "\n\n")

        i_sp = i + 1
        file_simple = open(str(i_sp) + "-" + simple_dict['name'] + ".txt", 'w+', encoding="utf8")
        file_simple.write("Name: " + simple_dict['name'])
        file_simple.write("\nJob: " + simple_dict['job'])
        file_simple.write("\nDOB: " + str(simple_dict['birthdate']))
        file_simple.write("\nCompany: " + simple_dict['company'])
        file_simple.write("\nSSN: " + simple_dict['ssn'])
        file_simple.write("\nResidence: " + simple_dict['residence'])
        file_simple.write("\nCurrent Location: " + str(simple_dict['current_location']))
        file_simple.write("\nBlood Group: " + simple_dict['blood_group'])
        file_simple.write("\nUsername: " + simple_dict['username'])
        file_simple.write("\nAddress: " + simple_dict['address'])
        file_simple.write("\neMail: " + simple_dict['mail'])
        file_simple.close()

def FAKE_PROFILE_VERY_SIMPLE():
    fake = Faker()
    shitthing_simple = fake.simple_profile()
    print(shitthing_simple)

try:
    ENTIRE_PROGRAM_FAKE_INFO_GEN_OFFLINE()
except:
    print(colored("\n[-] Something went wrong! \n[-] Please contact the creator to fix this issue!\n[-] Discord ID: ZeaCeR#5641", 'red'))
# FAKE_PROFILE_SIMPLE()
# FAKE_PROFILE_VERY_SIMPLE()
