# STD-CS350-Data_Structures-Lab1_RecursiveSearchInCharacterArray
# Lab1: Recursive Search in Character Array

## คำอธิบาย

กำหนดข้อมูลอาร์เรย์ `data` ขนาด 12 บรรทัด แต่ละบรรทัดเป็นตัวอักษรภาษาอังกฤษพิมพ์ใหญ่ทั้งหมด โดยมีตัวอักษรพิมพ์เล็กซ่อนอยู่ ให้นักศึกษาเขียนโปรแกรมภาษา Python โดย **ใช้ Recursive Function เท่านั้น** (ห้ามใช้ loop เช่น for หรือ while) เพื่อแก้ปัญหาต่อไปนี้

---

## ฟังก์ชันที่กำหนด

1. **CountLowercase**
   เขียนฟังก์ชันแบบ recursive เพื่อนับจำนวนตัวอักษรพิมพ์เล็กทั้งหมดในอาร์เรย์

2. **FindLinesWithLowercase**
   เขียนฟังก์ชันแบบ recursive เพื่อหาว่ามีตัวพิมพ์เล็กอยู่ในบรรทัดใดบ้าง (เก็บเฉพาะหมายเลขบรรทัด)

3. **CollectLowerCaseCharacters**
   เขียนฟังก์ชันแบบ recursive เพื่อดึงเฉพาะตัวพิมพ์เล็กทั้งหมดที่พบ ออกมาเป็น list

4. **FindLowerCasePositions**
   เขียนฟังก์ชันแบบ recursive ที่ค้นหาตัวพิมพ์เล็กทั้งหมด และบันทึกตำแหน่งในรูปแบบ tuple
   `(row, col, character)`
   โดย `row` คือเลขบรรทัด (เริ่มจาก 0), `col` คือเลขตำแหน่งคอลัมน์ในบรรทัด (เริ่มจาก 0) และ `character` คืออักษรพิมพ์เล็กที่พบ

---

## ข้อมูลที่กำหนด

```python
data = [
    "QWERTYUIOPASDFGHJKLZXCVBNM",
    "ASDFGHJKLZXCVBNMqWERTYUIOP",
    "ZXCVBNMASDFGHJKLZWERTYUIOP",
    "POIUYTREWQLKJHGFDSAmNBVCXZ",
    "MNBVCXZLKJHGFDSAPOIUYTREWQ",
    "LKJHGFDSAZXCVBNMqPOIUYTREW",
    "ASDFGHJKLZXCVBNMWERTYuIOP",
    "QWERTYUIOPASDFGHJKLZXCVBNM",
    "ZXCVBNMASDFGHJKLZWERTYUIOP",
    "POIUYTREWQLKJHGFDSAZXCVBNM",
    "MNBVCXZLKJhGFDSAPOIUYTREWQ",
    "QWERTYUIOPASDFGHJKLZXCVBNM"
]
```

---

## ผลลัพธ์ที่คาดหวัง

Total number of lowercase characters: 10
Lines containing lowercase characters: [1, 3, 5, 6, 10]
Lowercase characters found: ['q', 'm', 'q', ...]
Positions found: [(1, 16, 'q'), (3, 20, 'm'), ...]


---

## หมายเหตุ

- ห้ามใช้ loop ทุกชนิดในการแก้ปัญหา
- ห้ามลบหรือแก้ไขข้อมูลในอาร์เรย์ `data`
- ให้นักศึกษาเขียนฟังก์ชันแต่ละตัวแยกกัน และทดสอบผลลัพธ์ของฟังก์ชันแต่ละตัวอย่างน้อย 3 กรณี
- ส่งไฟล์ที่มีโค้ดฟังก์ชันทั้งหมด พร้อมผลลัพธ์ที่ทดสอบแล้ว

