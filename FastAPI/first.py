from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

import firebase_admin
from firebase_admin import firestore, credentials

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
},
{
    'name' : 'Vada, Sambar, Chutney',
    'quantity' : '2 Pcs',
    'rate' : 22,
},
{
    'name' : 'Pongal/Kichadi/Upma',
    'quantity' : '200 gms',
    'rate' : 32,
},
{
    'name' : 'Poori Masala',
    'quantity' : '2 Pcs',
    'rate' : 34,
},
{
    'name' : 'Plain Dosa',
    'quantity' : '1 Pc',
    'rate' : 32,
},
{
    'name' : 'Uthappam',
    'quantity' : '1 Pc',
    'rate' : 32,
},
{
    'name' : 'Masala Dosa',
    'quantity' : '1 Pc',
    'rate' : 36,
},
{
    'name' : 'Bread + Butter + Jam',
    'quantity' : '2 Pcs',
    'rate' : 15,
},
{
    'name' : 'Ghee Roast',
    'quantity' : '1 Pc',
    'rate' : 50,
},
{
    'name' : 'Masala Ghee Roast',
    'quantity' : '1 Pc',
    'rate' : 60,
},
{
    'name' : 'Podi Dosa',
    'quantity' : '1 Pc',
    'rate' : 37,
},
{
    'name' : 'Chole Bhatura',
    'quantity' : '1 Pc',
    'rate' : 55,
},
{
    'name' : 'Aloo Paratha with Curd',
    'quantity' : '1 Pc',
    'rate' : 28,
},
{
    'name' : 'Corn Flakes with Milk',
    'quantity' : '50 gm',
    'rate' : 35,
},
{
    'name' : 'Chocos with Milk',
    'quantity' : '50 gm',
    'rate' : 45,
},
{
    'name' : 'Corn Cheese Dosa',
    'quantity' : '1 Pc',
    'rate' : 70,
},
{
    'name' : 'Pav Bhaji',
    'quantity' : '2 Pcs',
    'rate' : 38,
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
},
{
    'name' : 'Chicken Keema Dosa',
    'quantity' : '1 Pc',
    'rate' : 90,
},
{
    'name' : 'Chicken Cheese Dosa',
    'quantity' : '1 Pc',
    'rate' : 90,
},
{
    'name' : 'Chicken Curry Dosa',
    'quantity' : '1 Pc',
    'rate' : 90,
},
{
    'name' : 'Scrambled Eggs',
    'quantity' : '2 Pcs',
    'rate' : 27,
},
{
    'name' : 'Boiled Eggs',
    'quantity' : '2 Pcs',
    'rate' : 21,
},
{
    'name' : 'Banana Roti',
    'quantity' : '1 Pc',
    'rate' : 27,
},
{
    'name' : 'Bread Omelette',
    'quantity' : '2 eggs',
    'rate' : 27,
},
{
    'name' : 'Masala Omelette',
    'quantity' : '2 eggs',
    'rate' : 27,
},
{
    'name' : 'Cheese Omelette',
    'quantity' : '2 eggs',
    'rate' : 50,
},
{
    'name' : 'Egg Masala',
    'quantity' : '2 eggs',
    'rate' : 55,
},
{
    'name' : 'Fried Egg',
    'quantity' : '2 eggs',
    'rate' : 27,
},
{
    'name' : 'Spanish Omelette',
    'quantity' : '2 eggs',
    'rate' : 35,
},
{
    'name' : 'French Toast',
    'quantity' : '2 eggs',
    'rate' : 27,
},
{
    'name' : 'Egg Bhurji',
    'quantity' : '2 eggs',
    'rate' : 27,
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
},
{
    'name' : 'Coffee',
    'quantity' : '1 Cup',
    'rate' : 15,
},
{
    'name' : 'Milk',
    'quantity' : '1 Glass',
    'rate' : 15,
},
{
    'name' : 'Green Tea',
    'quantity' : '1 Cup',
    'rate' : 13,
},
{
    'name' : 'Ice Lemon Tea',
    'quantity' : '1 Cup',
    'rate' : 13,
},
{
    'name' : 'Masala Tea',
    'quantity' : '1 Cup',
    'rate' : 15,
},
{
    'name' : 'Ginger Tea',
    'quantity' : '1 Cup',
    'rate' : 15,
},
]

for item in breakfast_bev_menu:
    doc = db.collection("Menu").document("Breakfast").collection("Beverages").document(item.get('name'))
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

t_id = 1

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

@app.post('/order')
def order(order: Order):
    global t_id

    regno = order.regno
    items = order.items
    rates = {}

    price = calc_price(regno, items, rates)

    return {"Price ": price}


def calc_price(regno, items, rates):
    try:
        member = db.collection("Members").document(regno)
        menu = db.collection("Menu").stream()

        for doc in menu:
            item_coll = doc.reference.collections()
            for collection in item_coll:
                item_all = collection.stream()
                for item in item_all:
                    item_data = item.to_dict()
                    rates[item_data['name']] = item_data['rate']

        trans_data = {"items":{}, "price":0}
    
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
        trans = member.collection('Transactions').document(t_id)
        t_id += 1
        trans.set(trans_data)

        member.update({"credits": firestore.Increment(-price)})

        return price
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))