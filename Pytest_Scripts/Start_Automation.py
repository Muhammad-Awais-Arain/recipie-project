import os
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('Linked Union Automation App')
root.geometry('880x880')
root.configure(bg='#52C3FF')
w = Label(root, text='Pytest Selenium Scripts', bg="Green", fg="white")
w.grid(row=0, column=3, padx=10, pady=10)

w = Label(root, text='Navigation Menus', bg="Red", fg="white")
w.grid(row=1, column=3, padx=10, pady=10)

#ROW2 --------------------------------------------------------------------------------------------------------------------------------

def Organize_My_Workplace():
    tkinter.messagebox.showinfo("Organize My Workplace", "Running Organize My Workplace Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_OMW.py')
    tkinter.messagebox.showinfo("Organize My Workplace", "Successfully completed automation of Organize My Workplace Navigation")
run_script = Button(root, text='Run OMW', bg="black", fg="white", command=Organize_My_Workplace)
run_script.grid(row=2, column=1, padx=5, pady=5)

def Event():
    tkinter.messagebox.showinfo("Event", "Running Test Event Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_event.py')
    tkinter.messagebox.showinfo("Event", "Successfully completed automation of Test Event Navigation")
run_script = Button(root, text='Run Event', bg="black", fg="white", command=Event)
run_script.grid(row=2, column=2, padx=5, pady=5)

def Legislative_Bills():
    tkinter.messagebox.showinfo("Legislative Bills", "Running Legislative Bills Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_Legislative.py')
    tkinter.messagebox.showinfo("Legislative Bills", "Successfully completed automation of Legislative Bills Navigation")
run_script = Button(root, text='Run Legislative Bills', bg="black", fg="white", command=Legislative_Bills)
run_script.grid(row=2, column=3, padx=5, pady=5)

def Find_My_Elected_Officials():
    tkinter.messagebox.showinfo("Find My Elected Officials", "Running Find My Elected Officials Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_FMEO.py')
    tkinter.messagebox.showinfo("Find My Elected Officials", "Successfully completed automation of Find My Elected Officials Navigation")
run_script = Button(root, text='Run FMEO', bg="black", fg="white", command=Find_My_Elected_Officials)
run_script.grid(row=2, column=4, padx=5, pady=5)

def Member_Discount():
    tkinter.messagebox.showinfo("Member Discount", "Running Member Discount Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_MemberDiscount.py')
    tkinter.messagebox.showinfo("Member Discount", "Successfully completed automation of Member Discount Navigation")
run_script = Button(root, text='Run Member Discount', bg="black", fg="white", command=Member_Discount)
run_script.grid(row=2, column=5, padx=5, pady=5)

#ROW3 --------------------------------------------------------------------------------------------------------------------------------

def Multiple_News():
    tkinter.messagebox.showinfo("Multiple News", "Running Multiple News Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_MultipleNews.py')
    tkinter.messagebox.showinfo("Multiple News", "Successfully completed automation of Multiple News Navigation")
run_script = Button(root, text='Run Multiple News', bg="black", fg="white", command=Multiple_News)
run_script.grid(row=3, column=1, padx=5, pady=5)

def Sub_Menu():
    tkinter.messagebox.showinfo("Sub Menu", "Running Sub Menu Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_SubMenu.py')
    tkinter.messagebox.showinfo("Sub Menu", "Successfully completed automation of Sub Menu Navigation")
run_script = Button(root, text='Run Sub Menu', bg="black", fg="white", command=Sub_Menu)
run_script.grid(row=3, column=2, padx=5, pady=5)

def Web_View():
    tkinter.messagebox.showinfo("Web View", "Running Web View Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_Webview.py')
    tkinter.messagebox.showinfo("Web View", "Successfully completed automation of Web View Navigation")
run_script = Button(root, text='Run Web View', bg="black", fg="white", command=Web_View)
run_script.grid(row=3, column=3, padx=5, pady=5)

def Social_Media():
    tkinter.messagebox.showinfo("Social Media", "Running Social Media Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_social.py')
    tkinter.messagebox.showinfo("Social Media", "Successfully completed automation of Social Media Navigation")
run_script = Button(root, text='Run Social Media', bg="black", fg="white", command=Social_Media)
run_script.grid(row=3, column=4, padx=5, pady=5)

def Multiple_Web_Links():
    tkinter.messagebox.showinfo("Multiple Web Links", "Running Multiple Web Links Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_MultipleWebLinks.py')
    tkinter.messagebox.showinfo("Multiple Web Links","Successfully completed automation of Multiple Web Links Navigation")
run_script = Button(root, text='Run Multiple Web Links', bg="black", fg="white", command=Multiple_Web_Links)
run_script.grid(row=3, column=5, padx=5, pady=5)

#ROW4 --------------------------------------------------------------------------------------------------------------------------------

def Union_Representative():
    tkinter.messagebox.showinfo("Union Representative", "Running Union Representative Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_UnionRepresentative.py')
    tkinter.messagebox.showinfo("Union Representative", "Successfully completed automation of Union Representative Navigation")
run_script = Button(root, text='Run Union Representative', bg="black", fg="white", command=Union_Representative)
run_script.grid(row=4, column=2, padx=5, pady=5)

def Report_Workplace_Violence():
    tkinter.messagebox.showinfo("Report Workplace Violence", "Running Report Workplace Violence Navigation Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_RWV.py')
    tkinter.messagebox.showinfo("Report Workplace Violence", "Successfully completed automation of Report Workplace Violence Navigation")
run_script = Button(root, text='Run Report Workplace Violence', bg="black", fg="white", command=Report_Workplace_Violence)
run_script.grid(row=4, column=3, padx=5, pady=5)

def Add_All_Navigations():
    tkinter.messagebox.showinfo("Add All Navigations", "Running Add All Navigations Automation")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Navigation_Scripts/test_AddAllNavigations.py')
    tkinter.messagebox.showinfo("Add All Navigations", "Successfully completed automation of Add All Navigations")
run_script = Button(root, text='Run Add All Navigations', bg="black", fg="white", command=Add_All_Navigations)
run_script.grid(row=4, column=4, padx=5, pady=5)

#Unhappy Paths Starts from here
y = Label(root, text='Unhappy Paths for Navigation Menus', bg="Red", fg="white")
y.grid(row=5, column=3, padx=10, pady=10)

def Unhappy_Path_Event():
    tkinter.messagebox.showinfo("Event Fail", "Running Event Automation Unhappy Path")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Unhappy_Paths/test_event.py')
    tkinter.messagebox.showinfo("Report Workplace Violence", "Successfully completed automation of Event Automation Unhappy Path Navigation")
run_script = Button(root, text='Run Event', bg="black", fg="white", command=Unhappy_Path_Event)
run_script.grid(row=6, column=1, padx=5, pady=5)


#Login Scenarios Starts from here
x = Label(root, text='Login Scenarios', bg="Red", fg="white")
x.grid(row=9, column=3, padx=10, pady=10)

def Login():
    tkinter.messagebox.showinfo("Backend Login", "Running Login Script")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Login_Scripts/test_login.py')
    tkinter.messagebox.showinfo("Backend Login", "Successfully completed automation of Login")
run_script = Button(root, text='Backend Login', bg="black", fg="white", command=Login)
run_script.grid(row=10, column=1, padx=5, pady=5)

def Multiple_Login():
    tkinter.messagebox.showinfo("Multiple Login", "Running Multiple Login Script")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_Login_Scripts/test_MultipleLogin.py')
    tkinter.messagebox.showinfo("Multiple Login", "Successfully completed automation of Multiple Login")
run_script = Button(root, text='Multiple Login', bg="black", fg="white", command=Multiple_Login)
run_script.grid(row=10, column=2, padx=5, pady=5)



#New Feature Scripts Starts from here
x = Label(root, text='New Feature Scenarios', bg="Red", fg="white")
x.grid(row=12, column=3, padx=10, pady=10)

def Promotional_Banner():
    tkinter.messagebox.showinfo("Promotional Banner", "Running Promotional Banner Script")
    os.system('pytest Pytest_Selenium_Scripts/Pytest_New_Feature_Scripts/test_PromotionalBanner.py')
    tkinter.messagebox.showinfo("Promotional Banner", "Successfully completed automation of Promotional Banner")
run_script = Button(root, text='Promotional Banner', bg="black", fg="white", command=Promotional_Banner)
run_script.grid(row=13, column=1, padx=5, pady=5)


#Robot Framework Scripts Starts from here
w = Label(root, text='Robot Framework Scripts', bg="Gray", fg="white")
w.grid(row=16, column=3, padx=10, pady=10)


def BackendLogin():
    tkinter.messagebox.showinfo("Backend Login", "Running Backend Login using Robot Framework Script")
    os.system('robot Robot_FrameWork_Scripts/BackendLogin.robot')
    tkinter.messagebox.showinfo("Backend Login", "Successfully completed automation of Backend Login using Robot Framework Script")
run_script = Button(root, text='Backend Login', bg="black", fg="white", command=BackendLogin)
run_script.grid(row=17, column=1, padx=5, pady=5)


x = Label(root, text='Register User Scenarios', bg="Red", fg="white")
x.grid(row=20, column=3, padx=10, pady=10)

x = Label(root, text='Web 2.0', bg="Gray", fg="white")
x.grid(row=21, column=3, padx=10, pady=10)

def RegisterUser():
    tkinter.messagebox.showinfo("Register User", "Running Register User using Selenium Script")
    os.system('pytest Register_User_Scripts/Web_2/test_Register.py')
    tkinter.messagebox.showinfo("Register User", "Successfully completed automation of Register User using Selenium Script")
run_script = Button(root, text='Register User', bg="black", fg="white", command=RegisterUser)
run_script.grid(row=22, column=1, padx=5, pady=5)


def RegisterUserAdminApproval():
    tkinter.messagebox.showinfo("Register User", "Running Register User Admin Approval using Selenium Script")
    os.system('pytest Register_User_Scripts/Web_2/test_AdminApproval.py')
    tkinter.messagebox.showinfo("Register User Admin Approval", "Successfully completed automation of Register User Admin Approval using Selenium Script")
run_script = Button(root, text='Register User Admin Approval', bg="black", fg="white", command=RegisterUserAdminApproval)
run_script.grid(row=22, column=2, padx=5, pady=5)


def RegisterUserTwoFactor():
    tkinter.messagebox.showinfo("Register User", "Running Register User Two Factor using Selenium Script")
    os.system('pytest Register_User_Scripts/Web_2/test_2FA_Register.py')
    tkinter.messagebox.showinfo("Register User 2FA", "Successfully completed automation of Register User Two Factor using Selenium Script")
run_script = Button(root, text='Register User 2FA', bg="black", fg="white", command=RegisterUserTwoFactor)
run_script.grid(row=22, column=3, padx=5, pady=5)

def TwoFactorFail():
    tkinter.messagebox.showinfo("Register User", "Running Register User Two Factor Fail Scenario using Selenium Script")
    os.system('pytest Register_User_Scripts/Web_2/test_2FA_Fail.py')
    tkinter.messagebox.showinfo("2FA Continue Fail", "Successfully completed automation of Register User Two Factor Fail Scenario using Selenium Script")
run_script = Button(root, text='2FA Continue Fail', bg="black", fg="white", command=TwoFactorFail)
run_script.grid(row=22, column=4, padx=5, pady=5)

def TwoFactorContinueAdminApproval():
    tkinter.messagebox.showinfo("Register User", "Running Register User Two Factor Continue Admin Approval Scenario using Selenium Script")
    os.system('pytest Register_User_Scripts/Web_2/test_2FAContinueAP.py')
    tkinter.messagebox.showinfo("2FA Continue Admin Approval", "Successfully completed automation of Register User Two Factor Continue Admin Approval Scenario using Selenium Script")
run_script = Button(root, text='2FA Continue Admin Approval', bg="black", fg="white", command=TwoFactorContinueAdminApproval)
run_script.grid(row=22, column=5, padx=5, pady=5)




x = Label(root, text='Web 3.0', bg="Gray", fg="white")
x.grid(row=24, column=3, padx=10, pady=10)


def RegisterUser3_0():
    tkinter.messagebox.showinfo("Register User", "Running Register User on 3.0 using Selenium Script")
    os.system('pytest Register_User_Scripts/Web_3/test_Register.py')
    tkinter.messagebox.showinfo("Register User", "Successfully completed automation of Register User on 3.0 using Selenium Script")
run_script = Button(root, text='Register User', bg="black", fg="white", command=RegisterUser3_0)
run_script.grid(row=25, column=1, padx=5, pady=5)

def TWOFA_REGISTER3_0():
    tkinter.messagebox.showinfo("Register User", "Running 2FA Register User on 3.0 using Selenium Script")
    os.system('pytest Register_User_Scripts/Web_3/test_2FA_Register.py')
    tkinter.messagebox.showinfo("Register User", "Successfully completed automation of 2FA Register User on 3.0 using Selenium Script")
run_script = Button(root, text='2FA Register User', bg="black", fg="white", command=TWOFA_REGISTER3_0)
run_script.grid(row=25, column=2, padx=5, pady=5)


x = Label(root, text='Union Onboarding', bg="Gray", fg="white")
x.grid(row=26, column=3, padx=10, pady=10)


def Add_Backend():
    tkinter.messagebox.showinfo("Add New Backend", "Running Add New Backend using Selenium Script")
    os.system('pytest Union_Onboarding_Scripts/test_OpenBackends.py')
    tkinter.messagebox.showinfo("Add New Backend", "Successfully completed automation of Add New Backend using Selenium Script")
run_script = Button(root, text='Add New Backend', bg="black", fg="white", command=Add_Backend)
run_script.grid(row=27, column=1, padx=5, pady=5)

root.mainloop()
