## Coffee Shop Order Program ##
## Author: Cynthia Hu
## Date: 10/28/2016
## Notes: This program enables the user to order multiple products within one order from the coffee shop. It provides
## three payment options. It also enables the user to quit during the process and have opportunites to reenter choice 
## if there is any input error.
## please execute .py: python CoffeeShopOrdering.py


##### Define Classes ######
class products:
    """products class contains information about the product customer ordered, including name, price
    and other attributes. This information will be used in Payment class."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.amount = self.price * self.quantity    
        self.ordered ={'name': self.name, 'quantity': self.quantity, 'amount': self.amount}
    
    def get_order(self):
        return self.ordered
    
class coffee(products):
    """coffee class is a children of products class and could have more attributes for specific product"""
    def __init__(self, name, price, quantity, size=None, flavor=None):
        super().__init__(name, price, quantity)
        self.size = size
        self.flavor = flavor
		
    def get_size(self):
        return self.size

    def get_flavor(self):
        return self.flavor

class payment:
    """payment class contains information about payment option, amount due and points. 
    It also prints the order and payment information to the end users."""
    def __init__(self, total_order, earn_point = 'Y'): #total_order is a list of dictionaries
        self.option = None
        self.total_order = total_order
        self.total_amount = 0
        
        for i in range(len(total_order)):
            self.total_amount += self.total_order[i]['amount']
        self.earn_point = earn_point
        if self.earn_point == 'Y':
            self.points_earned = self.total_amount // 10 + 1
        else:
            self.points_earned = 0
        
    # return order information and payment confirmation to the customer
    def pay(self):
        print("============================================")
        print("You have ordered: ")
        for i in range(len(total_order)):
            print(self.total_order[i]['name'] + ' *' + str(self.total_order[i]['quantity']) + '        ' + ("{:.2f}".format(self.total_order[i]['amount'])))
        print("--------------------------------------------")
        print("Total Amount Due : " + ("{:.2f}".format(self.total_amount)))
        print()
        
        # all three methods allow the user to earn points.
        if self.earn_point == 'Y':
            print("You have earned ",self.points_earned,' points.')
            print("Your point balance is: ",self.point_balance)      
        print()

# for each payment option, define a subclass of payment class mainly to customize printing payment confirmation.
class cash(payment):
    """cash class is a children of payment class and print additional information related to cash payment option."""
    
    def __init__(self,total_order, earn_point = 'Y'):
        super().__init__(total_order, earn_point)
        self.option = 'Cash'
        # call the update_points function within each children class as parent class is used to print amount due 
        # before payment option is chosen. And there is no need to update points when the parent class is called.
        self.point_balance = update_points(self.option,self.earn_point,first_name, self.points_earned)
        
    def pay(self, cash_paid):
        if cash_paid < self.total_amount:
            print("You have paid less cash than total order amount. Please pay additional: ", self.total_amount - cash_paid)

        super().pay()
        print("Payment Amount: " ,("{:.2f}".format(cash_paid)))
        print('Paid by Cash')
        print("Your Change: ",("{:.2f}".format(cash_paid - self.total_amount)))

class card(payment):
    """card class is a children of payment class and print additional information 
    related to credit/debit card payment option."""
    
    def __init__(self,total_order, earn_point = 'Y'):
        super().__init__(total_order, earn_point)
        self.option = 'Credit/Debit card'
        self.point_balance = update_points(self.option,self.earn_point,first_name, self.points_earned)
        
    def pay(self):
        super().pay()
        print("Payment Amount: " ,("{:.2f}".format(self.total_amount)))
        print('Paid by Credit/Debit Card')
        print("Your Change: ",("{:.2f}".format(0)))
                  
class point(payment): 
    """point class is a children of payment class and print additional information 
    related to point payment option."""
    
    def __init__(self, total_order, earn_point = 'Y'):
        super().__init__(total_order, earn_point)
        self.option = 'Points'
        # every 1 point worths $1; spend every $10 can earn 1 point but each order at least earns 1 point.
        self.points_redeemed = int(self.total_amount)
        self.point_balance = update_points(self.option,self.earn_point,first_name, self.points_earned, self.points_redeemed)

    # return order iymennformation, points redeemed and remained information to the customer
    def pay(self):
        if self.point_balance < self.points_redeemed:
            raise Exception("You don't have enough points to redeem. Please select other payment option.")
        super().pay()
        print(self.points_redeemed, " points have been redeemed.")
      
    
##### Define Functions ######     
def update_points(option,earn_point,first_name, points_earned, points_redeemed=None): 
    """ update_points function is to extract and update point balance for the customer"""
    
    if first_name.capitalize() not in customer:
        if earn_point.upper() == 'Y':
            point_balance = points_earned
        else:
            point_balance = 0
        customer_points[first_name.capitalize()] = point_balance
    else:
        point_balance = customer_points[first_name.capitalize()]
        
        if earn_point.upper() == 'Y':
            if option=='Points':
                point_balance = point_balance + points_earned - points_redeemed
            else:
                point_balance = point_balance + points_earned
        else:
            point_balance = point_balance
            
        # update customer data with new balance
        customer_points[first_name.capitalize()] = point_balance
    return point_balance

def display_order(category, product,size=None,flavor=None):
    """display_order funciton is to return the full name of the product ordered.
    The full name is input parameter of product class."""
    
    if category =='1': #coffee
        name = size_list[size] + ' ' + coffee_list[product] + ' with ' + flavor_list[flavor]
    else:
        name = bakery_list[product] 
    return name

def order_price(category, product,size=None,flavor=None):
    """order_price function is to extract and calculate price of the product ordered.
    It's the price for the full name product, including size and flavor for the coffee.
    price is the input paramter of product class."""
    
    if category =='1': #coffee
        price = coffee_price[coffee_list[product]]+size_price[size_list[size]]+flavor_price[flavor_list[flavor]]
    else:
        price = bakery_price[bakery_list[product]] 
    return price

	
##### initialize customer database ######    
import numpy as np
count=0
customer = ['Christopher','Cynthia','Sarah','Francisco','Robert', 'Tom','Jessica','David', 
            'Alice','Heather','Michael','Scott','Justin']
			
# use random funtion to initialize the customer points for current customers
while count == 0:
    customer_points = {}
    init_bal = list(np.random.randint(30,size=(len(customer),)))
    for i in range(len(customer)):
        customer_points[customer[i]]=init_bal[i]
    count +=1

	
##### populate product lists ###### 
# product price dictionary
coffee_price={'Latti':3.5, 'Mocha': 3.8, 'Cappuccino': 3.6, 'Black Coffee': 2.5, 'Iced Coffee': 3}
size_price={'Small':-0.5, 'Medium':0, 'Large':1}
flavor_price ={'Milk': 0, 'Soymilk': 0.5, 'Vanilla': 0.5, 'Caramel': 0.5, 'Chocolate': 0.5}
bakery_price={'Banana Bread': 1.6, 'Donut':1, 'Sandwich':4, 'Bagel': 1.8, 'Croissant': 1.5, 'Blueberry Muffin':2}

# product list for user interface
category_list={'1':'Coffee', '2':'Bakery'}
coffee_list={'1':'Latti','2':'Mocha','3':'Cappuccino','4':'Black Coffee', '5': 'Iced Coffee'}
size_list ={'1':'Small','2':'Medium','3':'Large'}
flavor_list={'1':'Milk','2':'Soymilk','3':'Vanilla','4':'Caramel','5':'Chocolate'}
bakery_list={'1':'Banana Bread','2': 'Donut','3': 'Sandwich','4': 'Bagel','5': 'Croissant','6':'Blueberry Muffin'}

# valid inputs from users
# 0 means skip or quit
valid_category = '0' + ''.join(list(category_list.keys()))
valid_coffee = '0' + ''.join(list(coffee_list.keys()))
valid_size = '0' + ''.join(list(size_list.keys()))
valid_flavor = '0' + ''.join(list(flavor_list.keys()))
valid_bakery = '0' + ''.join(list(bakery_list.keys()))

valid_category_ls = [int(i) for i in valid_category]
valid_category_ls.sort()
valid_coffee_ls = [int(i) for i in valid_coffee]
valid_coffee_ls.sort()
valid_size_ls = [int(i) for i in valid_size]
valid_size_ls.sort()
valid_flavor_ls = [int(i) for i in valid_flavor]
valid_flavor_ls.sort()
valid_bakery_ls = [int(i) for i in valid_bakery]
valid_bakery_ls.sort()


##### User Interface ###### 
print("****************************************************************")
print("******                                                    ******")
print("******         Welcome to Nolan's Coffee Shop             ******")
print("******                                                    ******")
print("****************************************************************")
print()
print("====You can enter 0 to skip any of the steps below or quit.====")
print()
# initialize variables
# category=0
coffee_order={}
bakery_order={}
quantity = 1
earn_point = 'Y'
total_order=[]
order_num = 0

# get user inputs. Keep asking for inputs from customers until customers choose to quit or skip
while True:
    while True:
        category=input("What would you like to order? Please enter a number: 1- Coffee, 2-Bakery    ")
        print()
        if category not in valid_category:
            print("Please enter a number in ", valid_category_ls)
            continue
        break
    
    if category == '0':
        break
        
    elif category =='1': # coffee
        while True:
            product=input("Please enter a number for the coffee: 1-Latti, 2-Mocha, 3-Cappuccino, 4-Black Coffee, 5-Iced Coffee    ")
            print()
            if product not in valid_coffee:
                print("Please enter a number in ", valid_coffee_ls)
                continue
            break
        if product == '0':
            break
        else:     
            while True:
                size=input("Please enter a number for the size: 1-Small, 2-Medium, 3-Large    ")
                print()
                if size not in valid_size:
                    print("Please enter a number in ", valid_size_ls)
                    continue
                break
            if size == '0':
                break
            else:
                while True:
                    flavor=input("Please enter a number for the flavor: 1-Milk, 2-Soymilk, 3-Vanilla, 4-Caramel, 5-Chocolate    ")
                    print()
                    if flavor not in valid_flavor:
                        print("Please enter a number in ", valid_flavor_ls)
                        continue
                    break
                if flavor == '0':
                    break
                else:
                    # if the user complete above steps, then complete one order and generate the product information
                    name = display_order(category,product,size,flavor)
                    price = order_price(category,product,size,flavor)
                    order_num += 1
                    # add this order to total_order list
                    current_order = coffee(name, price, quantity)
                    total_order.append(current_order.get_order())
    
    elif category =='2': #bakery
        while True:
            product=input("Please enter a number for the bakery: 1-Banana Bread, 2-Donut, 3-Sandwich, 4-Bagel, 5-Croissant, 6-Blueberry Muffin    ")
            print()
            if product not in valid_bakery:
                print("Please enter a number in ", valid_bakery_ls)
                continue
            break
        if product == '0':
            break
        else:
            # if the user didn't quit, then populate the product name
            name = display_order(category,product)
            price = order_price(category,product)
            order_num += 1
            # add this order to total_order list
            current_order = coffee(name, price, quantity)
            #total_order.append(current_order.ordered)
            total_order.append(current_order.get_order())
        
    else:
        print("We are sorry that something went wrong.")
        break

# if the user completes one product ordering then ask for inputs for payment
if order_num == 0:
    print()
    print("Thank you for visiting us!")
else:
    # get customer name and update customer database for point calculation
    first_name = input("Please enter your first name to earn the points: ")
    if first_name == '0':
        earn_point = 'N'
    else:
        # if new customer, then add it to the customer list and initialize point balance as 0
        if first_name.capitalize() not in customer:
            customer_points[first_name.capitalize()] =0

    # use cash payment class to print total amount due before asking the user to choose a payment mehtod
    temp = payment(total_order, earn_point) # call the update_points() 1st time
    print("-------------------------------------")
    print("Total Amount Due is ", ("{:.2f}".format(temp.total_amount)))   
    print("-------------------------------------")
    # cannot enter 0 to skip this step
    valid_payment = '123'
    
    while True:
        while True:
            pay_method = input("Please choose payment type: 1- Cash; 2- Credit/Debit card; 3- Points    ")
            print()
            if pay_method not in valid_payment:
                print("You cannot skip this step. Please enter a number in ", [int(i) for i in valid_payment])
                continue
            break

        # cash payment
        if pay_method == '1':
            while True:
                try:
                    cash_paid = float(input("Please enter the amount of cash you paid: "))
                    print()
                    break
                except:
                    print("Please enter only numeric.")
                    continue

            cash_payment = cash(total_order, earn_point)
            try:
                cash_payment.pay(cash_paid)
                break
            except Exception as e:
                print(str(e))
                continue


        # credit/debit card payment    
        elif pay_method == '2':
            card_payment = card(total_order, earn_point)
            card_payment.pay()
            break

        # use point to redeem
        elif pay_method == '3':
            point_payment = point(total_order, earn_point)
            
            try:
                point_payment.pay()
                break
            except Exception as e:
                print(str(e))
                continue
    print("--------------------------------------------")
    print("Thank you for shopping with us!")
