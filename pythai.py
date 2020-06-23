"""
ไพทอน ภาษาไทย โดย NateTH
เข้าใจง่าย เข้าถึงง่าย มีบทสอนในตัว


"""

"""
สำหรับผู้ที่เปิดไฟล์นี้ ที่ไมได้ import

การดัดแปลง แก้ไข ๆลๆ โดยไม่ได้รับอนุญาต มีความผิดทางกฏหมายลิขสิทธิ์



FUYU Studio - NateTH
"""

"""
เวอร์ชั่นปัจจุบัน
"""
version = 0.4
def check_version(versionn):
    import requests
    import urllib
    try:
        url = "https://pastebin.com/raw/XC5JTqjf"
        version =  requests.get(url)
        deline = version.text

        if str(deline) != str(versionn):
            print("Pythai มีเวอร์ชั่นใหม่แล้วกรุณาอัพเดตเพื่อฟีเจอร์ใหม่ๆได้ที่ https://github.com/kidJaNateTH/Pythai")
    except:
        pass
check_version(version)







จริง = True
เท็จ = False
ไม่จำเป็น = None
def หน่วงเวลา(วินาที):
    
    """หน่วยเป็นวินาที"""
    วินาที = int(วินาที)

def ลูปตลอดกาล(ฟังก์ชั่น,หน่วงเวลา:หน่วงเวลา=ไม่จำเป็น):
    import time
    while True:
        if หน่วงเวลา == None:
            ฟังก์ชั่น()
        else:
            ฟังก์ชั่น()
            time.sleep(หน่วงเวลา)


        

def ปริ้น(ข้อความ=None):
    """จะปริ้นข้อความที่ท่านระบุ"""
    return print(str(ข้อความ))
def ถ้าเท่ากับ(พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น):
    """เมื่อ พารามิเตอร์ทั้งสองเท่ากัน จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้"""
    if พารามิเตอร์1 == พารามิเตอร์2:
        ฟังก์ชั่น()
def ถ้ามากกว่า(พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น):
    """เมื่อ พารามิเตอร์1 มากกว่า พารามิเตอร์2 จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้"""
    if พารามิเตอร์1 >= พารามิเตอร์2:
        ฟังก์ชั่น()
def ถ้าน้อยกว่า(พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น):
    """เมื่อ พารามิเตอร์1 น้อยกว่า พารามิเตอร์2 จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้"""
    if พารามิเตอร์1 <= พารามิเตอร์2:
        ฟังก์ชั่น()
def เปิดไฟล์(ชื่อไฟล์,ประเภทการเปิด,ข้อความ=None):
    """เปิดไฟล์ในเครื่อง
    \nวิธีการใช้งาน
    \n
    \nตัวอย่าง การอ่านไฟล์
    \na = thai.เป็นไฟล์("ชื่อไฟล์.นามสกุล","อ่าน")
    \nthai.ปริ้น(a)
    \n่
    \nตัวอย่าง การเขียนไฟล์
    \nthai.เป็นไฟล์("ชื่อไฟล์.นามสกุล","เขียน","ข้อความ")
    \n
    \n่
    \nตัวอย่าง การเขียนทับไฟล์
    \nthai.เป็นไฟล์("ชื่อไฟล์.นามสกุล","เขียนทับ","ข้อความ")
    \n"""
    if ประเภทการเปิด == "อ่าน":
        with open(ชื่อไฟล์,'r',encoding='utf8') as f:
            return f.read()
    if ประเภทการเปิด == "เขียนทับ":
        with open(ชื่อไฟล์,'w',encoding='utf8') as f:
            f.write(ข้อความ)
        with open(ชื่อไฟล์,'r',encoding='utf8') as f:
            return f.read()
    if ประเภทการเปิด == "เขียนเติม" or ประเภทการเปิด == "เขียน":
        with open(ชื่อไฟล์,'a+',encoding='utf8') as f:
            f.write(ข้อความ)
        with open(ชื่อไฟล์,'r',encoding='utf8') as f:
            return f.read()

def thaison_load(ชื่อไฟล์):
    """ก่อนที่จะใช้งาน\nท่านต้องติดตั้ง Json ก่อนถึงจะสามารถใช้งานได้\n\n\n...วิธีการติดตั้ง...\n1.ไปที่ cmd ของท่าน\n2.พิมพ์ pip install json ไปอันเสร็จสิ้น"""
    import json
    with open(str(ชื่อไฟล์),'r',encoding='utf8') as f:
        file = json.load(f)
        return json.dumps(file, indent=4, sort_keys=True)

class สตริง:
    def ตัวใหญ่(self,ตัวแปร:bool=None,คัวแรกเท่านั้น:bool=None):
        if ตัวแปร == True:
            return str(self).capitalize()
        return str(self).upper()
    def ตัวเล็ก(self,ตัวแปร=None):
        return str(self).lower()
    def นับตัวอักษร(self,ตัวแปร=None):
        return len(str(self))
    def ถ้าตัวใหญ่(self,ตัวแปร=None):
        return str(self).isupper()
    def ถ้าตัวเล็ก(self,ตัวแปร=None):
        return str(self).islower()
    def ถ้าเว้นวรรค(self,ตัวแปร=None):
        return str(self).isspace()
    def แทนที่(self,ข้อความที่จะแทนที่=None,แทนที่ด้วย=None):
        return str(self).replace(str(ข้อความที่จะแทนที่),str(แทนที่ด้วย))
