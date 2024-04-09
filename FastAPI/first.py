from fastapi import FastAPI, HTTPException, Depends
from typing import List
from pydantic import BaseModel
import firebase_admin
from firebase_admin import firestore, credentials, auth

cred = credentials.Certificate("food-park-easydine-firebase-adminsdk-qg6ap-440e1a064d.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

members = [{
    'regno': '22BAI1076',
    'fname': 'Archisman',
    'lname': 'Panda',
    'credits': 6000,
}, 
{
    'regno': '22BLC1234',
    'fname': 'Andrew',
    'lname': 'Hembrom',
    'credits': 6000,
},
{
    'regno': '22BAI1047',
    'fname': 'Joel',
    'lname': 'Beera',
    'credits': 6000,
},
{
    'regno': '22BAI1050',
    'fname': 'Renjith',
    'lname': 'Anil',
    'credits': 6000,
},
]

for member in members:
    doc = db.collection("Members").document(member.get('regno'))
    regno = member.get('regno')
    if regno: 
        query = db.collection("Members").where("regno", "==", regno).limit(1).get()
        if not query:
            doc.set(member)

breakfast_veg_menu = [{
    'name' : 'Idli, Sambar, Chutney',
    'quantity' : '2 Pcs',
    'rate' : 17,
    'image' : 'https://imgs.search.brave.com/BXRBSZwSEJCiP7i6JUd4rgQo93z1EhNloGdRIuRd5UI/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAxLzYxLzEzLzY2/LzM2MF9GXzE2MTEz/NjY3NF9OZ1ZGY1B0/V2Z3TFBZMDNOcEpV/clNpSDlvRHZtYTlS/bi5qcGc'
},
{
    'name' : 'Vada, Sambar, Chutney',
    'quantity' : '2 Pcs',
    'rate' : 22,
    'image' : 'https://imgs.search.brave.com/id4rZlGQkVsmzmXVPeYmM-di8FZ0joMuOnkiySXss_Q/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/dmVncmVjaXBlc29m/aW5kaWEuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIxLzA3/L3ZhZGEtc2FtYmFy/LTEuanBn'
},
{
    'name' : 'Upma',
    'quantity' : '200 gms',
    'rate' : 32,
    'image' : 'https://imgs.search.brave.com/0dAc6lYle5Wt6BfL1G3HAZGV-6B51v35ucwbwMgOLcs/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/Y29va2luZ2FuZG1l/LmNvbS93cC1jb250/ZW50L3VwbG9hZHMv/MjAwOS8wOC8zNzg0/NTgxNjYyXzI1NTEy/Y2RjZjMxLndlYnA'
},
{
    'name' : 'Poori Masala',
    'quantity' : '2 Pcs',
    'rate' : 34,
    'image' : 'https://imgs.search.brave.com/yaFEhTuCfTL7F9nRpXazUI8g3Vs7SbOpE8PoQu7KHmg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9mYXJt/Ni5zdGF0aWNmbGlj/a3IuY29tLzU1NjAv/MTQ3MzE1MTc0MTJf/MTc2YTJkNWE3MF96/LmpwZw'
},
{
    'name' : 'Plain Dosa',
    'quantity' : '1 Pc',
    'rate' : 32,
    'image' : 'https://imgs.search.brave.com/EuRfFc6C8KJCLykx8as3K9I8u96cqrcKYYtznYu7l-w/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFuaGVhbHRo/eXJlY2lwZXMuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDE2/LzAzL3BsYWluLWRv/c2EtcmVjaXBlLmpw/Zy53ZWJw'
},
{
    'name' : 'Uthappam',
    'quantity' : '1 Pc',
    'rate' : 32,
    'image' : 'https://imgs.search.brave.com/sCRnaUqATl6i3WQpSF6Y5R1Ljdc8o35tviPbkqDr0_U/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9yYWtz/a2l0Y2hlbi5uZXQv/d3AtY29udGVudC91/cGxvYWRzLzIwMTMv/MDMvODUyNzIxOTUw/NF8wZGRiMmNkZTZm/X3ouanBn'
},
{
    'name' : 'Masala Dosa',
    'quantity' : '1 Pc',
    'rate' : 36,
    'image' : 'https://imgs.search.brave.com/OHn_x5PLPPWpnxo2SJycJTbFBq_xxksypSkGPEch3q8/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMwMS5ueXQuY29t/L2ltYWdlcy8yMDE1/LzAxLzI4L2Rpbmlu/Zy8yOEtJVENIRU4x/LzI4S0lUQ0hFTjEt/YXJ0aWNsZUxhcmdl/LmpwZz93PTEyODAm/cT03NQ'
},
{
    'name' : 'Bread + Butter + Jam',
    'quantity' : '2 Pcs',
    'rate' : 15,
    'image' : 'https://imgs.search.brave.com/bxomENdElurZo4B1bArnxiaG4Ed2chslftb1LO6qwRM/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9idXR0/ZXJ3aXRoYXNpZGVv/ZmJyZWFkLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvMjAxOS8w/MS9CZXN0LUhvbWVt/YWRlLUJyZWFkLXJl/Y2lwZS0yMS5qcGc'
},
{
    'name' : 'Ghee Roast',
    'quantity' : '1 Pc',
    'rate' : 50,
    'image' : 'https://imgs.search.brave.com/wXR9EnHFn1Y8wfYdBzH3BDMmij2wjsPEmw6-HND0sTc/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/dmVncmVjaXBlc29m/aW5kaWEuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDE2LzA5/L2doZWUtcm9hc3Qt/ZG9zYTI2LmpwZw'
},
{
    'name' : 'Masala Ghee Roast',
    'quantity' : '1 Pc',
    'rate' : 60,
    'image' : 'https://imgs.search.brave.com/rObe2LyIIgJbzKbBEHvD31WkooGKAWnz7bcipMZCFkE/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9kb3Nh/Y29ybmVyLmNhL3dw/LWNvbnRlbnQvdXBs/b2Fkcy9CdXR0ZXJv/ckdoZWVNYXNhbGFE/b3NhZTE1NzEwNDMz/MTE1ODItMTE3MHg3/ODAuanBlZw'
},
{
    'name' : 'Podi Dosa',
    'quantity' : '1 Pc',
    'rate' : 37,
    'image' : 'https://imgs.search.brave.com/HrLUonrmP_zHoTwmAQQVl7OOY2sYx91jLaKNQ5b2iiI/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90aGVt/YWdpY3NhdWNlcGFu/LmNvbS93cC1jb250/ZW50L3VwbG9hZHMv/MjAxNy8wNy9Qb2Rp/LURvc2EtMi5qcGc'
},
{
    'name' : 'Chole Bhatura',
    'quantity' : '1 Pc',
    'rate' : 55,
    'image' : 'https://imgs.search.brave.com/Ugkxq_orbxKXq6JCP5mrFh9MkqY-sG2afRUq0vh1Hkc/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9jZG4u/bXlnaW5nZXJnYXJs/aWNraXRjaGVuLmNv/bS9pbWFnZXMvODAw/cHgvODAwcHgtcmVj/aXBlcy1QdW5qYWJp/LWNob2xlLWJoYXR1/cmUtYW51cGFtYS1w/YWxpd2FsLW15LWdp/bmdlci1nYXJsaWMt/a2l0Y2hlbi03Lmpw/Zw'
},
{
    'name' : 'Aloo Paratha with Curd',
    'quantity' : '1 Pc',
    'rate' : 28,
    'image' : 'https://imgs.search.brave.com/CCHYSLatPRbEAS0YZxiVyNFmJvEu-39WW_dIQaRKSiQ/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aG9tZW1ha2Vyam9i/LmNvbS93cC1jb250/ZW50L3VwbG9hZHMv/MjAyMy8wOC90b3At/dmlldy1waG90by1v/Zi1wdW5qYWJpLWFs/b28tcGFyYXRoYS1k/aGFiYS1zdHlsZS13/aXRoLXBpY2tsZS1h/bmQtY2hpbGllcy1h/LXJlY2lwZS1ieS1o/b21lbWFrZXJqb2Iu/Y29tXy5qcGc'
},
{
    'name' : 'Corn Flakes with Milk',
    'quantity' : '50 gm',
    'rate' : 35,
    'image' : 'https://imgs.search.brave.com/huw4n91Lwpo_QVIhm7w37G0mYL-kn28TlZc1Iol_ZyU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9j/L2MzL0tlbGxvZ2cn/c19Db3JuX0ZsYWtl/cyxfd2l0aF9taWxr/LmpwZw'
},
{
    'name' : 'Chocos with Milk',
    'quantity' : '50 gm',
    'rate' : 45,
    'image' : 'https://imgs.search.brave.com/sgYPSI24vfVEBCtq0vqy5WBbaktEKkWuQ3mGWIo37tQ/rs:fit:500:0:0/g:ce/aHR0cDovL29uZWRh/eWNhcnQuY29tL29k/Y2Ivd3AtY29udGVu/dC91cGxvYWRzLzIw/MTYvMDYvYm93bC1i/cm93bi1jZXJlYWwt/Y2hvY28tZmxha2Vz/LWNob2NvbGF0ZS1m/b29kLUZhdmltLmNv/bS0xMDMzMjguanBn'
},
{
    'name' : 'Corn Cheese Dosa',
    'quantity' : '1 Pc',
    'rate' : 70,
    'image' : 'https://imgs.search.brave.com/sgYPSI24vfVEBCtq0vqy5WBbaktEKkWuQ3mGWIo37tQ/rs:fit:500:0:0/g:ce/aHR0cDovL29uZWRh/eWNhcnQuY29tL29k/Y2Ivd3AtY29udGVu/dC91cGxvYWRzLzIw/MTYvMDYvYm93bC1i/cm93bi1jZXJlYWwt/Y2hvY28tZmxha2Vz/LWNob2NvbGF0ZS1m/b29kLUZhdmltLmNv/bS0xMDMzMjguanBn'
},
{
    'name' : 'Pav Bhaji',
    'quantity' : '2 Pcs',
    'rate' : 38,
    'image' : 'https://imgs.search.brave.com/9Ju1j2xxzohVFo2r98onijkj1tmPMG_GT7D0NeioWWE/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/Y29va3dpdGhtYW5h/bGkuY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDE4LzA1L0Jl/c3QtUGF2LUJoYWpp/LVJlY2lwZS0xMjAw/eDE4MTguanBn'
},
]

for item in breakfast_veg_menu:
    doc = db.collection("Menu").document("Breakfast").collection("Veg").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

breakfast_nv_menu = [{
    'name' : 'Egg Dosa',
    'quantity' : '1 Pc',
    'rate' : 37,
    'image' : 'https://imgs.search.brave.com/yD70_ujjWUPJVlJ9K6wJnFI6J4iF4GthyxlMtaZ2dBQ/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9ncmVh/dGN1cnJ5cmVjaXBl/cy5uZXQvd3AtY29u/dGVudC91cGxvYWRz/LzIwMTcvMDMvZWdn/ZG9zYTMtMS5qcGc'
},
{
    'name' : 'Chicken Keema Dosa',
    'quantity' : '1 Pc',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/oPNaK9iqmjcOsKiCXfoANw7LbEPxYtZKx4unTnVdJHY/rs:fit:500:0:0/g:ce/aHR0cDovL3d3dy5m/b29kdmVkYW0uY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDE4/LzA1L0NoaWNrZW4t/RG9zYS1SZWNpcGUt/MS5qcGc'
},
{
    'name' : 'Chicken Cheese Dosa',
    'quantity' : '1 Pc',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/NY559rytpl2mbyy7kvZvS0IEOFPHmlVV8z8wXbZQR7Q/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9ob25l/c3Rjb29raW5nLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAx/Mi8wOS9oYzEtMS1v/Zi0xLmpwZw'
},
{
    'name' : 'Chicken Curry Dosa',
    'quantity' : '1 Pc',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/WZF3zlWVWaI8aU5y3NQu6uEV-Rsy21o5qIoX-Q1Hqz4/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWct/Z2xvYmFsLmNwY2Ru/LmNvbS9yZWNpcGVz/LzM4YjFiMTE5OWZl/NWNjMWEvNjgweDQ4/MmNxNzAvZG9zYS13/aXRoLWNoaWNrZW4t/Y3VycnktcmVjaXBl/LW1haW4tcGhvdG8u/anBn'
},
{
    'name' : 'Scrambled Eggs',
    'quantity' : '2 Pcs',
    'rate' : 27,
    'image' : 'https://imgs.search.brave.com/Ox1BIJdbPD89qPX2Oj22bQVnCU-MpQIZ6lAbPapYj-I/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzk2L2M0/L2Y5Lzk2YzRmOTNm/NTE0ZjBlNDkyYTk0/Mjg3MGJhZGIxYWM2/LmpwZw'
},
{
    'name' : 'Boiled Eggs',
    'quantity' : '2 Pcs',
    'rate' : 21,
    'image' : 'https://imgs.search.brave.com/_CsqkBbP6Hkvpm7_EcmZ2tgVNy8SICYa0xCNvMUNBxU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAwLzQxLzMwLzE0/LzM2MF9GXzQxMzAx/NDkyX2hMaEhWbDhm/Snh4d2M5eERDVDBB/bFRiSk4wQlFSMjd5/LmpwZw'
},
{
    'name' : 'Bread Omelette',
    'quantity' : '2 eggs',
    'rate' : 27,
    'image' : 'https://imgs.search.brave.com/v2LZVjcQZyTXRmzUo4jsydfKcGL5ks4n3fH2ej3z9xg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vbXl2ZWdl/dGFyaWFucm9vdHMu/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE5LzA5L0RTQ18w/MDE0LTIuanBnP3Jl/c2l6ZT05NjEsMTAy/NCZzc2w9MQ'
},
{
    'name' : 'Masala Omelette',
    'quantity' : '2 eggs',
    'rate' : 27,
    'image' : 'https://imgs.search.brave.com/hKLZpxHGO7BdUGaeunBUEjBc0lbMFIs0mlZu5lqDN0g/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/Y2Fyb2xpbmVzY29v/a2luZy5jb20vd3At/Y29udGVudC91cGxv/YWRzLzIwMjAvMDkv/bWFzYWxhLW9tZWxl/dHRlLXBob3RvLmpw/Zw'
},
{
    'name' : 'Cheese Omelette',
    'quantity' : '2 eggs',
    'rate' : 50,
    'image' : 'https://imgs.search.brave.com/Aj9Qp8t32krNKMNTd8Jlxtr70TT3mbW6gMGiKdscJL4/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9uYXRh/c2hhc2tpdGNoZW4u/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDIyLzAyL0VnZy1P/bWVsZXR0ZS0zLTcy/OHgxMDkxLmpwZw'
},
{
    'name' : 'Egg Masala',
    'quantity' : '2 eggs',
    'rate' : 55,
    'image' : 'https://imgs.search.brave.com/QLJ49AFB0btk5inqCjGw5Fvj_hhnPWGaaZfWPZ-nbLM/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/c2hhcm1pc3Bhc3Np/b25zLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxMy8wMi9F/Z2dNYXNhbGE1Lmpw/Zw'
},
{
    'name' : 'Fried Egg',
    'quantity' : '2 eggs',
    'rate' : 27,
    'image' : 'https://imgs.search.brave.com/atUWRauMfIqc_ND4pYa9BI5tWlLXcmmSL0TzZGUv4Fw/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS1waG90by9m/cmllZC1lZ2dzXzE0/MTc5My03MzAuanBn/P3NpemU9NjI2JmV4/dD1qcGc'
},
{
    'name' : 'Spanish Omelette',
    'quantity' : '2 eggs',
    'rate' : 35,
    'image' : 'https://imgs.search.brave.com/rqd6jkgCrf2ERtQbNRvezhPKQkKBmRrXlirE1SaZ9Fw/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/am9jb29rcy5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMTMv/MDYvc3BhbmlzaC1v/bWVsZXR0ZS0xLTI1/LmpwZw'
},
{
    'name' : 'French Toast',
    'quantity' : '2 eggs',
    'rate' : 27,
    'image' : 'https://imgs.search.brave.com/OUUSxm0gg813NzJvG1zitfMscJvw8ocNyYhUQHIwcOY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9mb29k/LmZuci5zbmRpbWcu/Y29tL2NvbnRlbnQv/ZGFtL2ltYWdlcy9m/b29kL2Z1bGxzZXQv/MjAwOC8zLzI2LzAv/SUUwMzA5X0ZyZW5j/aC1Ub2FzdC5qcGcu/cmVuZC5oZ3R2Y29t/LjEyODAuNzIwLnN1/ZmZpeC8xNDMxNzMw/NDMxMzQwLmpwZWc'
},
{
    'name' : 'Egg Bhurji',
    'quantity' : '2 eggs',
    'rate' : 27,
    'image' : 'https://imgs.search.brave.com/aNwMp4ZzXuXcw9H__PbT7ZwVZ9TE_dgtdm8uCNg3xjY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFuaGVhbHRo/eXJlY2lwZXMuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDIz/LzAxL2VnZy1iaHVy/amktcmVjaXBlLmpw/Zy53ZWJw'
},
]

for item in breakfast_nv_menu:
    doc = db.collection("Menu").document("Breakfast").collection("Non-Veg").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

breakfast_bev_menu = [{
    'name' : 'Tea',
    'quantity' : '1 Cup',
    'rate' : 13,
    'image' : 'https://imgs.search.brave.com/hW7EipwjFYXiLGryt9uFZ--Mzu8BOHcNPxM8gma0dYg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFuaGVhbHRo/eXJlY2lwZXMuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDIz/LzA1L2luZGlhbi1t/YXNhbGEtY2hhaS10/ZWEuanBnLndlYnA'
},
{
    'name' : 'Coffee',
    'quantity' : '1 Cup',
    'rate' : 15,
    'image' : 'https://imgs.search.brave.com/CIAk0KQs6w3ycLiz_wZvzD8x58kYQWsI9uNji1ZfMvY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTE0/NzQ5NzE2MC9waG90/by9jb2ZmZWUtY3Vw/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1sb202dTlPbVhQ/UU9XTHNld0xrTmsz/NU1Sb2xEWThYbDMx/RFZ3LVZGd1A4PQ'
},
{
    'name' : 'Milk',
    'quantity' : '1 Glass',
    'rate' : 15,
    'image' : 'https://imgs.search.brave.com/L0kuzV7nlfKVUCMfxdtJToXNC3d4bbIlgIDdtXlEX7w/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDYw/MTU3NTA5L3Bob3Rv/L21pbGstaW4tdGhl/LWdsYXNzLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz14cVNt/MEU3RVdSQnZReDc0/Zml0MzROcUxaSnc2/RnhoRTBzS21DZVo1/VEUwPQ'
},
{
    'name' : 'Green Tea',
    'quantity' : '1 Cup',
    'rate' : 13,
    'image' : 'https://imgs.search.brave.com/loQQ54FV80apprK32qHV6mldgc6K13ZyI0-CJxnbB90/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzAwLzgwLzgwLzAx/LzM2MF9GXzgwODAw/MTUzX21aaFBwSHVS/TE9JQ3hGZ21SaUg3/R092RUxKWjJCNExv/LmpwZw'
},
{
    'name' : 'Ice Lemon Tea',
    'quantity' : '1 Cup',
    'rate' : 13,
    'image' : 'https://imgs.search.brave.com/D48OZW1_V0w4Wy7MVTQvP3mg8cZXe1CQLbgB8oZkkjc/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTQ3/MzMyOTAwL3Bob3Rv/L2ljZS10ZWEtd2l0/aC1sZW1vbi1waXRj/aGVyLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz1HaHNHQ011/eXprQ2UzQ0dsM0hl/a0JOZTk0RlZydWZP/MlRmd2NtakxzQU1n/PQ'
},
{
    'name' : 'Masala Tea',
    'quantity' : '1 Cup',
    'rate' : 15,
    'image' : 'https://imgs.search.brave.com/8dzA49GAM4l6V8P7vAFj_lRXcV7faW_IiLfxlqhPaQo/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTE0/MTk5MDM2NS9waG90/by9tYXNhbGEtY2hh/aS10ZWEuanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPTdKcC01/a0hVZy16ZGxUeTJU/eWdidDZJZGJGSVIx/YlVTZGRsd0o5OUxq/ZnM9'
},
{
    'name' : 'Ginger Tea',
    'quantity' : '1 Cup',
    'rate' : 15,
    'image' : 'https://imgs.search.brave.com/MWSgVJuAkECBgD1I78TY-4p_giJHNhsst_3HgbU0OMk/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTcw/NDg4MDQzL3Bob3Rv/L2dpbmdlci10ZWEu/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PXpNYlBkYnR1YmNo/TS15dTJLVW1udDRG/Q1hldGR6dUZUYWVH/b1pCZVJMMXc9'
},
]

for item in breakfast_bev_menu:
    doc = db.collection("Menu").document("Breakfast").collection("Beverages").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

veg_menu = [{
    'name' : 'Veg Meals',
    'quantity' : '1 Plate',
    'rate' : 55,
    'image' : 'https://imgs.search.brave.com/8pRlPAjv7QZ0QSTyHD58WuZ_wuSKGuA3VhxhZMkPIMk/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTYy/Mzk5NTYxL3Bob3Rv/L2luZGlhbi10aGFs/aS5qcGc_cz02MTJ4/NjEyJnc9MCZrPTIw/JmM9WlVyNUV4SVUt/NFpLQncxSTNzN3pL/Q2NYeUdWVWJWWmtL/NUhoa3hFNUdJST0'
},
{
    'name' : 'Plain Naan',
    'quantity' : '1 Pc',
    'rate' : 17,
    'image' : 'https://imgs.search.brave.com/pr9lxJDTFMkLVyZwE3u82qCKxq_Vuwp7zM4l9H6KbPU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9yYXNh/bWFsYXlzaWEuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDE5/LzEyL25hYW41Lmpw/Zw'
},
{
    'name' : 'Butter Naan',
    'quantity' : '1 Pc',
    'rate' : 23,
    'image' : 'https://imgs.search.brave.com/_XrttfSssde0hxCUsOl2Dd3PhqJ7J6-4MxHc4EPgwJQ/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzA1Lzk4LzcwLzg0/LzM2MF9GXzU5ODcw/ODQyOV9oYXlNZ3hx/dWJjOWx4MTFIYjNh/ckpMVnVrWnB6NDhC/Qi5qcGc'
},
{
    'name' : 'Phulka',
    'quantity' : '1 Pc',
    'rate' : 16,
    'image' : 'https://imgs.search.brave.com/nJMzyE76ZNSuYqrNwfPXVKRQyI8PFhQJ0eI_CU8QWpA/rs:fit:500:0:0/g:ce/aHR0cHM6Ly95dW1t/eWluZGlhbmtpdGNo/ZW4uY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDE1LzA5L3Bo/dWxrYS1yZWNpcGUu/anBn'
},
{
    'name' : 'Veg Fried Rice',
    'quantity' : '1 Plate',
    'rate' : 55,
    'image' : 'https://imgs.search.brave.com/R5vdSOjOpzbIe0sucZkXY4ppiukzYuDO2XtQ7GDHrQM/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/Z2ltbWVzb21lb3Zl/bi5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMTcvMDcvSG93/LVRvLU1ha2UtRnJp/ZWQtUmljZS1SZWNp/cGUtMy0xLmpwZw'
},
{
    'name': 'Paneer Fried Rice',
    'quantity': '1 Plate',
    'rate': 65,
    'image' : 'https://imgs.search.brave.com/MmXwK6gCG0YdF_7nECuilXbXBQRJKQi5boOkHHa99UU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9iMjk1/ODEyNS5zbXVzaGNk/bi5jb20vMjk1ODEy/NS93cC1jb250ZW50/L3VwbG9hZHMvcGFu/ZWVyLWZyaWVkLXJp/Y2UtcmVjaXBlLTEt/NS5qcGc_bG9zc3k9/MSZzdHJpcD0xJndl/YnA9MQ'
},
{
    'name': 'Curd',
    'quantity': '1 Cup',
    'rate': 12,
    'image' : 'https://imgs.search.brave.com/lODyumD8a5rwGAnlKEEzmTrkanf4eTlr_HiqxCTgwcY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFudmVnZ2ll/ZGVsaWdodC5jb20v/d3AtY29udGVudC91/cGxvYWRzLzIwMjMv/MDYvaG9tZW1hZGUt/eW9ndXJ0LmpwZw'
},
{
    'name': 'Palak Paneer',
    'quantity': '1 Plate',
    'rate': 60,
    'image' : 'https://imgs.search.brave.com/TAGc0OQopnkKf_NR6o44VX8I8DGgCakUQfA-_dIa0tg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9jZG4y/LmZvb2R2aXZhLmNv/bS9zdGF0aWMtY29u/dGVudC9mb29kLWlt/YWdlcy9jdXJyeS1y/ZWNpcGVzL3BhbGFr/LXBhbmVlci1yZWNp/cGUvcGFsYWstcGFu/ZWVyLXJlY2lwZS5q/cGc'
},
{
    'name': 'Paneer Butter Masala',
    'quantity': '1 Plate',
    'rate': 65,
    'image' : 'https://imgs.search.brave.com/tNg2rJJ89mGmknZW2aRb6S9CH5wiNiDWzfnUESUHXAg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFuaGVhbHRo/eXJlY2lwZXMuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDIx/LzA3L3BhbmVlci1i/dXR0ZXItbWFzYWxh/LmpwZy53ZWJw'
},
{
    'name': 'Paneer Chatpata',
    'quantity': '1 Plate',
    'rate': 72,
    'image' : 'https://imgs.search.brave.com/qeiS3akFisJYL0NYt506aedcPKx8nF50DlC146dOgE8/rs:fit:500:0:0/g:ce/aHR0cDovL3d3dy5y/ZWxpc2h0aGViaXRl/LmNvbS93cC1jb250/ZW50L3VwbG9hZHMv/MjAyMC8wNi80MTQ0/NkRFNi1DNjZBLTQ0/NDMtQTMxQy1FM0Qw/NzhCMkVCNTguanBn'
},
{
    'name': 'Plain Dal',
    'quantity': '1 Plate',
    'rate': 52,
    'image' : 'https://imgs.search.brave.com/lr8OSlhvIQ1K0LtHtixhayYSJdvu3GXn8Is1JFivUcU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9nbGVi/ZWtpdGNoZW4uY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDIz/LzEwL3NpbXBsZWRh/bHNwb29uZnVsbC5q/cGc'
},
{
    'name': 'Aloo Jeera',
    'quantity': '1 Plate',
    'rate': 50,
    'image' : 'https://imgs.search.brave.com/6PPV_ZAhF4LybWzQ85480FXGgQTwfFL6Y9_9hO2wgD4/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFuaGVhbHRo/eXJlY2lwZXMuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDIy/LzA0L2plZXJhLWFs/b28uanBnLndlYnA'
},
{
    'name': 'Veg Biryani',
    'quantity': '1 Plate',
    'rate': 58,
    'image' : 'https://imgs.search.brave.com/zRr1w9695cZg9AWXilsb9u_J_80BFn7qk2BrOAV7YzI/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTI3/MzI5MTMxMy9waG90/by9kZWxpY2lvdXMt/dmVnLXBlYXMtcHVs/YW8tcmljZS5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9VzRR/LXF4OWdQZm1SWXpH/OV9sNWg5MW9MR1o4/N1FOZFhfNHNXc29E/T1luRT0'
},
]

for item in veg_menu:
    doc = db.collection("Menu").document("Lunch").collection("Veg").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

for item in veg_menu:
    doc = db.collection("Menu").document("Dinner").collection("Veg").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

nv_menu = [{
    'name' : 'Chicken Biryani',
    'quantity' : '1 Plate',
    'rate' : 100,
    'image' : 'https://imgs.search.brave.com/ePOgnZWfANHQ43fAOXnaP37uFhCMejk41hLtU7tGoLg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTA1/ODAyOTA5Ni9waG90/by9jaGlja2VuLWJp/cnlhbmkuanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPXlWVjFS/QXJrWXoxZlhmMEJs/cGV1d3h0MHlUSEhE/bmxPVVJWTUptWWdB/ZUk9'
},
{
    'name' : 'Chicken Fried Rice',
    'quantity' : '1 Plate',
    'rate' : 80,
    'image' : 'https://imgs.search.brave.com/lwy2uj_fajQcY9pUsYRR-OgfmNODAJ-Wdx3yfC0Y-g8/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQ3/MDQ2MTk4OC9waG90/by9jaGlja2VuLWZy/aWVkLXJpY2UuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPUVX/TzE1dWNNVkdwTmFN/N1RnN25PT25pWlZv/UmZGaTR1V2F1UF8x/cjBwU289'
},
{
    'name' : 'Chicken 65',
    'quantity' : '1 Plate',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/cBqqIuwTPrxZv9N32tbhSB7dINBIsXs5FhqbWRSjnik/rs:fit:500:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9k/L2Q3L0NoaWNrZW5f/NjUuanBn'
},
{
    'name' : 'Chicken Hyderabadi',
    'quantity' : '1 Plate',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/jY9ROzqckV4HR73bgOYfLx39jbbh0T1fe23J3AxKTMU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWct/Z2xvYmFsLmNwY2Ru/LmNvbS9yZWNpcGVz/L2NkZTBmNWQ1MmEy/MzM2OGUvNjgweDQ4/MmNxNzAvaHlkZXJh/YmFkaS1jaGlja2Vu/LW1hc2FsYS1yZWNp/cGUtbWFpbi1waG90/by5qcGc'
},
{
    'name' : 'Malai Chicken',
    'quantity' : '1 Plate',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/cQES9z3MeSNebjLKSiuNhM6dBo5Px-UJwZCOebxcAhI/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFuaGVhbHRo/eXJlY2lwZXMuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDIz/LzEwL21hbGFpLWNo/aWNrZW4uanBnLndl/YnA'
},
{
    'name' : 'Egg Biryani',
    'quantity' : '1 Plate',
    'rate' : 80,
    'image' : 'https://imgs.search.brave.com/NXi6H27Hy4ParM53otByowhaTM5woFEuchAwx4HurI8/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vY29va2lu/Z2Zyb21oZWFydC5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MTUvMDYvRWdnLUJp/cml5YW5pLTIuanBn/P3Jlc2l6ZT02ODQs/MTAyNCZzc2w9MQ'
},
{
    'name' : 'Egg Fried Rice',
    'quantity' : '1 Plate',
    'rate' : 60,
    'image' : 'https://imgs.search.brave.com/iVzz0Cie2WWeU5agkAfZ1uvNha551zKwDMXNnAOFnpw/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9jaHJp/c3RpZWF0aG9tZS5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MjIvMDYvRWdnLUZy/aWVkLVJpY2UtMy5q/cGc'
},
{
    'name' : 'Fish Fry',
    'quantity' : '1 Plate',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/8b595JogS4rTvkaXmN-WFm_lHwzFEjJgUpYO9yThMCo/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTMw/OTM1Mzg2Ni9waG90/by9zZWVyLWZpc2gt/ZnJ5LmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz0xOG1ENW1D/RXJPTkFFUVltT3o5/NzBaZk0xekVfQ2ZN/RDk2VlBhSG1OU2ZB/PQ'
},
{
    'name' : 'Egg Masala',
    'quantity' : '1 Plate',
    'rate' : 60,
    'image' : 'https://imgs.search.brave.com/s7Rt_JEiqNWtx2kkczh0k4JRpbqLGDXmeTg60l7E_HU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/c2hhcm1pc3Bhc3Np/b25zLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxMy8wMi9F/Z2dNYXNhbGE0Lmpw/Zw'
},
]

for item in nv_menu:
    doc = db.collection("Menu").document("Lunch").collection("Non Veg").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

for item in nv_menu:
    doc = db.collection("Menu").document("Dinner").collection("Non Veg").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

dessert_menu = [{
    'name' : 'Gulab Jamun',
    'quantity' : '2 Pcs',
    'rate' : 21,
    'image' : 'https://imgs.search.brave.com/hOXqQThz6XotkyMLVGNycx0_PKlx5yBW84cUs9zoh3Y/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/aW5kaWFuaGVhbHRo/eXJlY2lwZXMuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDIx/LzA5L2d1bGFiLWph/bXVuLmpwZy53ZWJw'
},
{
    'name' : 'Jalebi',
    'quantity' : '2 Pcs',
    'rate' : 21,
    'image' : 'https://imgs.search.brave.com/YOUBko9CgjIDXW2JMENcoQdBcm-dVOJo-sorFPQd5r4/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA0LzM4LzQ3LzQ5/LzM2MF9GXzQzODQ3/NDk5MF9Kb0czNTNM/a1cxSHpxSXlBUnQ5/Z05KMHJ4Zm1wMFB4/QS5qcGc'
},
{
    'name' : 'Chocolate Ice Cream with Dates',
    'quantity' : '1 Cup',
    'rate' : 50,
    'image' : 'https://imgs.search.brave.com/hFoxYXqEXHt0O600klcLnRfPCJHInfdGVIX6GfX0_jk/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAxLzQ3LzYxLzg2/LzM2MF9GXzE0NzYx/ODY3Nl9FV09WQUlK/NFN3bUhtOGlTR01o/QzM4OVNFSkwyVGho/WC5qcGc'
},
{
    'name' : 'Vanilla Ice Cream with Chocolate Syrup',
    'quantity' : '1 Cup',
    'rate' : 50,
    'image' : 'https://imgs.search.brave.com/cQYY2N89O4Kh5rNI3wCTFwXSsUQoPkAetupgcPO8RBQ/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTgw/NjUxNzczL3Bob3Rv/L3ZhbmlsbGEtaWNl/LWNyZWFtLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1BTlVv/U0VXbUlKU2lzYWRf/MGFoWGUzcm11S0Jt/emlzR0pkQ19zUk13/NnNjPQ'
},
{
    'name' : 'Strawberry Ice Cream',
    'quantity' : '1 Cup',
    'rate' : 50,
    'image' : 'https://imgs.search.brave.com/eACaNL_vl7L5NAzob9k9A75RwWoMfB54KnKhCkykFek/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pMy53/cC5jb20vbG1sZC5v/cmcvd3AtY29udGVu/dC91cGxvYWRzLzIw/MTgvMDcvU3RyYXdi/ZXJyeS1JY2UtQ3Jl/YW0tMTAuanBn'
},
{
    'name' : 'Mango Ice Cream with Gulab Jamun',
    'quantity' : '1 Cup',
    'rate' : 50,
    'image' : 'https://imgs.search.brave.com/CeO46pKBs1ByXhVC6ExcbLP-O0XPbgrltuLWN3E8osM/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vc2FuZGh5/YWhhcmloYXJhbi5j/by51ay93cC1jb250/ZW50L3VwbG9hZHMv/MjAxOC8wNS9tYW5n/by1pY2UtY3JlYW0t/MS1vZi0zLW1pbi5q/cGc_cmVzaXplPTcw/MCwxMDUwJnNzbD0x'
},
]

for item in dessert_menu:
    doc = db.collection("Menu").document("Lunch").collection("Dessert").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

for item in dessert_menu:
    doc = db.collection("Menu").document("Dinner").collection("Dessert").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

tc_menu = [{
    'name' : 'Chicken Biryani',
    'quantity' : '1 Plate',
    'rate' : 100,
    'image' : 'https://imgs.search.brave.com/ePOgnZWfANHQ43fAOXnaP37uFhCMejk41hLtU7tGoLg/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTA1/ODAyOTA5Ni9waG90/by9jaGlja2VuLWJp/cnlhbmkuanBnP3M9/NjEyeDYxMiZ3PTAm/az0yMCZjPXlWVjFS/QXJrWXoxZlhmMEJs/cGV1d3h0MHlUSEhE/bmxPVVJWTUptWWdB/ZUk9'
},
{
    'name' : 'Chocolate Ice Cream with Dates',
    'quantity' : '1 Cup',
    'rate' : 50,
    'image' : 'https://imgs.search.brave.com/hFoxYXqEXHt0O600klcLnRfPCJHInfdGVIX6GfX0_jk/rs:fit:500:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAxLzQ3LzYxLzg2/LzM2MF9GXzE0NzYx/ODY3Nl9FV09WQUlK/NFN3bUhtOGlTR01o/QzM4OVNFSkwyVGho/WC5qcGc'
},
{
    'name': 'Paneer Chatpata',
    'quantity': '1 Plate',
    'rate': 72,
    'image' : 'https://imgs.search.brave.com/qeiS3akFisJYL0NYt506aedcPKx8nF50DlC146dOgE8/rs:fit:500:0:0/g:ce/aHR0cDovL3d3dy5y/ZWxpc2h0aGViaXRl/LmNvbS93cC1jb250/ZW50L3VwbG9hZHMv/MjAyMC8wNi80MTQ0/NkRFNi1DNjZBLTQ0/NDMtQTMxQy1FM0Qw/NzhCMkVCNTguanBn'
},
{
    'name' : 'Chicken Hyderabadi',
    'quantity' : '1 Plate',
    'rate' : 90,
    'image' : 'https://imgs.search.brave.com/jY9ROzqckV4HR73bgOYfLx39jbbh0T1fe23J3AxKTMU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWct/Z2xvYmFsLmNwY2Ru/LmNvbS9yZWNpcGVz/L2NkZTBmNWQ1MmEy/MzM2OGUvNjgweDQ4/MmNxNzAvaHlkZXJh/YmFkaS1jaGlja2Vu/LW1hc2FsYS1yZWNp/cGUtbWFpbi1waG90/by5qcGc'
},
]

for item in tc_menu:
    doc = db.collection("Menu").document("Lunch").collection("Today's Choices").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)

for item in tc_menu:
    doc = db.collection("Menu").document("Dinner").collection("Today's Choices").document(item.get('name'))
    name = item.get('name')
    if name: 
        query = db.collection("Menu").where("name", "==", name).limit(1).get()
        if not query:
            doc.set(item)
            
class OrderItem(BaseModel):
    name: str
    quantity: int

    def __getitem__(self, key):
        return getattr(self, key)

class Order(BaseModel):
    regno: str
    items: List[OrderItem]

class Transaction(BaseModel):
    regno: str
    amount: int

app = FastAPI()

@app.get('/menu/breakfast')
def get_bf_menu():
    menu = db.collection("Menu").document("Breakfast")
    breakfast_veg_menu = menu.collection("Veg").stream()
    breakfast_nv_menu = menu.collection("Non-Veg").stream()
    breakfast_bev_menu = menu.collection("Beverages").stream()
    
    veg_items = [docu.to_dict() for docu in breakfast_veg_menu]
    nv_items = [docu.to_dict() for docu in breakfast_nv_menu]
    bev_items = [docu.to_dict() for docu in breakfast_bev_menu]
    
    return {
        "veg_menu": veg_items,
        "non_veg_menu": nv_items,
        "beverages_menu": bev_items
    }

@app.get('/menu/lunch')
def get_lu_menu():
    menu = db.collection("Menu").document("Lunch")
    lunch_veg_menu = menu.collection("Veg").stream()
    lunch_nv_menu = menu.collection("Non Veg").stream()
    dessert_menu = menu.collection("Dessert").stream()
    
    veg_items = [docu.to_dict() for docu in lunch_veg_menu]
    nv_items = [docu.to_dict() for docu in lunch_nv_menu]
    dessert_items = [docu.to_dict() for docu in dessert_menu]
    
    return {
        "veg_menu": veg_items,
        "non_veg_menu": nv_items,
        "dessert_menu": dessert_items
    }

@app.get('/menu/dinner')
def get_din_menu():
    menu = db.collection("Menu").document("Dinner")
    dinner_veg_menu = menu.collection("Veg").stream()
    dinner_nv_menu = menu.collection("Non Veg").stream()
    dessert_menu = menu.collection("Dessert").stream()
    
    veg_items = [docu.to_dict() for docu in dinner_veg_menu]
    nv_items = [docu.to_dict() for docu in dinner_nv_menu]
    dessert_items = [docu.to_dict() for docu in dessert_menu]
    
    return {
        "veg_menu": veg_items,
        "non_veg_menu": nv_items,
        "dessert_menu": dessert_items
    }

@app.post('/order/breakfast')
def bf_order(order: Order):
    global t_id

    regno = order.regno
    items = order.items
    rates = {}
    bf_menu = db.collection("Menu").document("Breakfast").collections()

    price = calc_price(regno, items, rates, bf_menu)

    return {"Price ": price}

@app.post('/order/lunch')
def lu_order(order: Order):
    global t_id

    regno = order.regno
    items = order.items
    rates = {}
    lu_menu = db.collection("Menu").document("Lunch").collections()

    price = calc_price(regno, items, rates, lu_menu)

    return {"Price ": price}

@app.post('/order/dinner')
def din_order(order: Order):
    global t_id

    regno = order.regno
    items = order.items
    rates = {}
    lu_menu = db.collection("Menu").document("Dinner").collections()

    price = calc_price(regno, items, rates, lu_menu)

    return {"Price ": price}

def calc_price(regno, items, rates, menu):
    global t_id
    try:

        for collection in menu:
            item_all = collection.stream()
            for item in item_all:
                item_data = item.to_dict()
                rates[item_data['name']] = item_data['rate']

        trans_data = {"items":{}, "price":0, "time":None}

        price = 0

        for item in items:
            name = item.name
            quantity = item.quantity
            if name in rates:
                trans_data["items"][name] = quantity
                price += quantity * rates[name]
            else:
                raise HTTPException(status_code=404, detail=rates)
    
        trans_data['price'] = price
        trans_data['time'] = firestore.SERVER_TIMESTAMP

        member = db.collection("Members").document(regno)

        if member.get().exists:
            trans = member.collection('Transactions').document()
            trans.set(trans_data)
            member.update({"credits": firestore.Increment(-price)})

        else:
            non_member = db.collection("Non-Members")
            reg = non_member.document(regno)
            trans = reg.collection('Transactions').document()
            trans.set(trans_data)
        return price
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def create_member(regno):    
    try:
        user = auth.get_user_by_email(regno+"@mail.com")
        return user.uid
    except auth.UserNotFoundError:
        user = auth.create_user(email=regno+"@mail.com", password = "123456")
        return user.uid

members = db.collection("Members").list_documents()
for doc in members:
    regno = doc.id
    custom_token = create_member(regno)

def generate_token(regno):
    try:
        return auth.create_custom_token(regno)
    except Exception as e:
        raise Exception(f"Failed to generate custom token: {str(e)}")

members = db.collection("Members").list_documents()
for doc in members:
    regno = doc.id
    custom_token = generate_token(regno)

# members = db.collection("Members").list_documents()
# for doc in members:
#     regno = doc.id
#     create_member(regno)

class User(BaseModel):
    regno: str
    password: str

def authenticate_user(regno: str, password: str) -> bool:
    try:
        member_doc = db.collection("Members").document(regno).get()
        if not member_doc.exists:
            create_member(regno)
        user = auth.get_user_by_email(regno + "@mail.com")
        uid = user.uid
        # auth.verify_password(uid, password)
        return True
    except auth.UserNotFoundError:
        create_member(regno)
        user = auth.get_user_by_email(regno + "@mail.com")
        uid = user.uid
        return True
    except auth.InvalidUidError:
        return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/login")
def login(user: User):
    regno = user.regno
    password = user.password

    if authenticate_user(regno, password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


