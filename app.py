from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',top=toplist)

toplist=[
    ["chicken.jpg","Tandoori Chicken Full","₹ 349 - 15% Off","Excellent"],
    ["burger.jpg","Double Cheese Burger","₹ 69 - 10% Off","Excellent"],
    ["bread.jpg","Cheesy Bread Toast","₹ 199 - 20% Off","Excellent"],
    ["cake.jpg","Choco-Caramel Cake","₹ 49 - 35% Off","Excellent"]
]

dessertslist=[
    ["dessert1.jpg","Coffee Vanilla Cream","₹ 159 - 25% Off","Average"],
    ["dessert2.jpg","Choco Brownie Cream","₹ 79 - 30% Off","Good"],
    ["dessert3.jpg","ChocoFilled Doughnut","₹ 99 - 15% Off","Excellent"],
    ["dessert4.jpg","Red Cherry CupCakes","₹ 39 - 20% Off","Good"]
]

burgerslist=[
    ["burger1.jpg","Pepper Relish Burger","₹ 49 - 55% Off","Excellent"],
    ["burger2.jpg","Tomato Stuffed Burger","₹ 169 - 10% Off","Good"],
    ["burger3.jpg","Double Layer Burger","₹ 199 - 25% Off","Average"],
    ["burger4.jpg","Crunchy Burger Tower","₹ 69 - 15% Off","Good"]
]

drinkslist=[
    ["drink1.jpg","Violet Grape Drink","₹ 59 - 35% Off","Good"],
    ["drink2.jpg","Ginger Lime Juice","₹ 39 - 15% Off","Excellent"],
    ["drink3.jpg","Choco-Cream Shake","₹ 99 - 20% Off","Average"],
    ["drink4.jpg","Chocolate Cool Coffee","₹ 49 - 10% Off","Excellent"]
]

cakeslist=[
    ["cake1.jpg","Oreo ChocoNut Cake","₹ 349 - 15% Off","Average"],
    ["cake2.jpg","Caramel Filled Cake","₹ 269 - 20% Off","Good"],
    ["cake3.jpg","Brown Chocolate Cake","₹ 399 - 60% Off","Excellent"],
    ["cake4.jpg","Rainbow Nuts Cake","₹ 449 - 55% Off","Excellent"]
]

@app.route('/dishes')
def dishes():
    return render_template('dishes.html',top=toplist,desserts=dessertslist,burgers=burgerslist,drinks=drinkslist,cakes=cakeslist)

@app.route('/contact')
def login():
    return render_template('contact.html')


if __name__=='__main__':
    app.run(debug=True)