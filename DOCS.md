# ยินดีต้อนรับเข้าสู่วิธีการใช้งาน Pythai
**การติดตั้ง** 
```css
1. เปิด cmd ชองท่าน
2. pip install pythai
3. พิมพ์ from pythai import * ในไฟล์ Python ของท่าน
```
**คำสั่งพื้นฐาน**

```css
จริง
return ค่าเป็น True
```
```css
เท็จ
return ค่าเป็น False
```
```css
ไม่จำเป็น
return ค่าเป็น None
```
```css
ลูปตลอดกาล(ฟังก์ชั่น,หน่วงเวลา:หน่วงเวลา=ไม่จำเป็น)
White loop
```
```css
ปริ้น(ข้อความ)
ปริ้นข้อความออกมาจะเป็นค่าหรือสตริงก็ได้
```
```css
ถ้าเท่ากับ(พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น)
เมื่อ พารามิเตอร์ทั้งสองเท่ากัน จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้
```
```css
ถ้ามากกว่า(พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น)
เมื่อ พารามิเตอร์1 มากกว่า พารามิเตอร์2 จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้
```
```css
ถ้าน้อยกว่า(พารามิเตอร์1,พารามิเตอร์2,ฟังก์ชั่น)
เมื่อ พารามิเตอร์1 น้อยกว่า พารามิเตอร์2 จะทำการรันฟังก์ชั่นที่ท่านกำหนดไว้
```
```css
เปิดไฟล์(ชื่อไฟล์,ประเภทการเปิด,ข้อความ=None)
```

### ตัวอย่าง การอ่านไฟล์
```css
    a = เปิดไฟล์("ชื่อไฟล์.นามสกุล","อ่าน")
    ปริ้น(a)
```
    
### ตัวอย่าง การเขียนไฟล์
```css
   เปิดไฟล์("ชื่อไฟล์.นามสกุล","เขียน","ข้อความ")
```

### ตัวอย่าง การเขียนทับไฟล์
```css
   เปิดไฟล์("ชื่อไฟล์.นามสกุล","เขียนทับ","ข้อความ")
```





**สตริง**
```css
ตัวใหญ่(ตัวแปร:str,คัวแรกเท่านั้น:bool=None)
return ค่าเป็น str
```
```css
ตัวเล็ก(ตัวแปร:str)
return ค่าเป็น str
```
```css
นับตัวอักษร()
return ค่าเป็น int
```
```css
ถ้าตัวใหญ่(self:str)
return ค่าเป็น boolean
```
```css
ถ้าตัวเล็ก(self:str)
return ค่าเป็น boolean
```
```css
ถ้าเว้นวรรค(self:str)
return ค่าเป็น boolean
```
```css
แทนที่(ข้อความที่จะแทนที่,แทนที่ด้วย)
return ค่าเป็น str
```
