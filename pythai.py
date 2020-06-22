"""
ไพทอน ภาษาไทย โดย NateTH
เข้าใจง่าย เข้าถึงง่าย มีบทสอนในตัว





"""





"""
สำหรับผู้ที่เปิดไฟล์นี้ ที่ไมได้ import

การดัดแปลง แก้ไข ๆลๆ โดยไม่ได้รับอนุญาต มีความผิดทางกฏหมายลิขสิทธิ์



FUYU Studio - NateTH
"""




class thai():
    """ไพไทย ไพทอนภาษาไทยยังไม่เต็มรูปแบบ
    โดย NateTH"""
    def ปริ้น(self,ข้อความ=None):
        """จะปริ้นข้อความที่ท่านระบุ"""
        return print(str(self))
    def ถ้าเท่ากับ(self,พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น):
        """เมื่อ พารามิเตอร์ทั้งสองเท่ากัน จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้"""
        if พารามิเตอร์1 == พารามิเตอร์2:
            ฟังก์ชั่น()
    def ถ้ามากกว่า(self,พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น):
        """เมื่อ พารามิเตอร์1 มากกว่า พารามิเตอร์2 จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้"""
        if พารามิเตอร์1 >= พารามิเตอร์2:
            ฟังก์ชั่น()
    def ถ้าน้อยกว่า(self,พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น):
        """เมื่อ พารามิเตอร์1 น้อยกว่า พารามิเตอร์2 จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้"""
        if พารามิเตอร์1 <= พารามิเตอร์2:
            ฟังก์ชั่น()
    def เปิดไฟล์(self,ประเภทการเปิด,ข้อความ=None):
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
            with open(self,'r',encoding='utf8') as f:
                print(1)
                return f.read()
        if ประเภทการเปิด == "เขียนทับ":
            with open(self,'w',encoding='utf8') as f:
                f.write(ข้อความ)
            with open(self,'r',encoding='utf8') as f:
                return f.read()
        if ประเภทการเปิด == "เขียนเติม" or ประเภทการเปิด == "เขียน":
            with open(self,'a+',encoding='utf8') as f:
                f.write(ข้อความ)
            with open(self,'r',encoding='utf8') as f:
                return f.read()

class json():
    """ก่อนที่จะ import คลาสนี้\nท่านต้องติดตั้ง Json ก่อนถึงจะสามารถใช้งานได้\n\n\n...วิธีการติดตั้ง...\n1.ไปที่ cmd ของท่าน\n2.พิมพ์ pip install json ไปอันเสร็จสิ้น"""
    import json
