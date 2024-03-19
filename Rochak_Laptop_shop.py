import datetime

# function which will read data from text file which contains all of the laptop details
def laptop_ko_details():
    laptops = {}
    with open('laptops.txt', 'r') as file:
        for line in file:
            Name, Brand, Price, Quantity, Processor, Graphics = line.strip().split(', ')
            laptops[Name.upper()] = {'Brand Name': Brand, 'price': float(Price.strip('$')),
                                    'quantity': int(Quantity), 'processor': Processor, 'graphics': Graphics}
    return laptops

# function which will works on basis of selling and updating stock after selling
def Laptop_For_Selling():
    laptops = laptop_ko_details()
    
    name_of_user = str(input("PLEASE ENTER YOUR NAME TO PROCEED FORWARD:"))
    if not name_of_user:
        print("╔══════════════════════════════════════════════════════════════════════════╗")
        print("║ ERROR: YOUR NAME CANNOT BE EMPTY, PLEASE ENETER A VALID NAME NEXT TIME!! ║")
        print("╚══════════════════════════════════════════════════════════════════════════╝")
        return
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  S.N   Name of laptops             Quantity      Price        ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    SN = 1
    for Name, specs in laptops.items():
        print(f"   {SN}     {Name:<30}{specs['quantity']}         ${specs['price']}")

        SN +=1
    print("╚═══════════════════════════════════════════════════════╝")
    laptop_name = input("ENTER THE NAME OF LAPTOP YOU WANT TO BUY: ")
    if not laptop_name:
        print("╔════════════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║ ERROR: NAME OF LAPTOP CANNOT BE EMPTY , PLEASE ENTER A VALID NAME FROM ABOVE LIST NEXT TIME !! ║")
        print("╚════════════════════════════════════════════════════════════════════════════════════════════════╝")
        return
    if laptop_name.upper() not in laptops:
        print("""
        f"ERROR: {laptop_name} NOT FOUND IN STOCK."
        """)
        return
    laptop = laptops[laptop_name.upper()]
    success = False
    while success == False:
        try:
            quantity = int(input("ENTER THE NUMBER OF QUANTITY YOU WANT TO BUY: "))
            if quantity<1:
                print("╔════════════════════════════════════════════╗")
                print("║  ERROR: PLEASE INPUT A VALID QUANTITY !!   ║")
                print("╚════════════════════════════════════════════╝")
                return
            success = True
        except:
            print("╔══════════════════════════════════════════════════╗")
            print("║ ERROR: ALPHABETS CANNOT BE TAKEN IN QUANTITY. !! ║")
            print("╚══════════════════════════════════════════════════╝")
            print("\t" * 8)
            return  
    if laptop['quantity'] < quantity:
        print("\t" * 8)
        print(f"ERROR : SORRY , NOT ENOUGH {laptop_name}  IN STOCK TO SELL {quantity} UNITS.")
        print("\t" * 8)
        return

    
    
    total_amount_without_shipping_cost= laptop['price'] * quantity
    shipping = str(input("DO YOU WANT TO GET YOUR LAPTOP SHIPPED?"))
    if(shipping.upper() == "YES"):
        shipping_cost = 50  
    else:
        shipping_cost = 0
    total_amount_with_shipping_cost = total_amount_without_shipping_cost + shipping_cost
    
    invoice = f"""
    
╔═══════════════════════════════════════════════════════════════╗
║                   ROCHAK-TOP-TECH HUB                         ║ 
║                    ITAHARI-4,SUNSARI                          ║ 
║                       025-586216                              ║ 
║===============================================================║ 
║                        INVOICE                                ║ 
║---------------------------------------------------------------║ 
║ DATE: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.
║ CUSTOMER NAME: {name_of_user.upper()} 
║---------------------------------------------------------------║ 
║ PRODUCT NAME:    {laptop_name.upper()}
║ QUANTITY:   {quantity}
║ AMOUNT: ${laptop['price']:.2f}
║---------------------------------------------------------------║ 
║ SUB-TOTAL AMOUNT:   ${total_amount_with_shipping_cost:.2f} 
║ SHIPPING CHARGE:   ${shipping_cost:.2f}║ 
║ TOTAL AMOUNT:      ${total_amount_with_shipping_cost:.2f} 
║---------------------------------------------------------------║ 
║               THANK YOU FOR YOUR BUSINESS!!                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    
             """
    print(invoice) 
    print("╔═════════════════════════════════════════════════════════════╗")
    print("║ INFORMATION MESSAGE : FOR INVOICE PLEASE CHECK TEXT FILE.   ║")
    print("╚═════════════════════════════════════════════════════════════╝")
    print("\t" * 8)
    with open("INVOICE_OF_SALE.txt","w", encoding="utf-8") as file:
        file.write(invoice)
    laptop['quantity'] -= quantity

    #updates stock if laptop is sold
    with open('laptops.txt', 'w') as file:
        for laptop_name, laptop_details in laptops.items():
            Name = laptop_name
            Brand = laptop_details['Brand Name']
            price = laptop_details['price']
            quantity = laptop_details['quantity']
            processor = laptop_details['processor']
            graphics = laptop_details['graphics']
            file.write(f"{Name}, {Brand}, ${price}, {quantity}, {processor}, {graphics}\n")
    

#function where distributor purchases laptops from manufacturers 
def purchasing_laptop():
    laptops = laptop_ko_details()
    name_of_distributor = str(input("ENTER NAME OF DISTRIBUTOR: "))
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  S.N   Name of laptops             Quantity      Price        ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    SN = 1
    for Name, specs in laptops.items():
        print(f"   {SN}     {Name:<30}{specs['quantity']}         ${specs['price']}")

        SN +=1
    print("╚═══════════════════════════════════════════════════════════════╝")
    laptop_name =  str(input("ENTER NAME OF LAPTOP: "))
    if laptop_name.upper() not in laptops:
        print("╔═════════════════════════════════════════════════════╗")
        print("║ ERROR: PLEASE ENTER A VALID NAME FROM THE LIST. !!  ║")
        print("╚═════════════════════════════════════════════════════╝")
        print("\t" * 8)
        return
    laptop = laptops[laptop_name.upper()]
    try:
        quantity = int(input("ENTER NUMBER OF LAPTOP :"))
        if quantity<1:
                print("╔════════════════════════════════════════════╗")
                print("║ ERROR: PLEASE ENTER A VALID QUANTITY. !!   ║")    
                print("╚════════════════════════════════════════════╝")
                print("\t" * 8)
                return
        elif quantity > laptop['quantity']:
            print("╔════════════════════════════════════════════╗")
            print("║ ERROR:  NOT ENOUGH STOCK AVAILABLE. !!     ║")    
            print("╚════════════════════════════════════════════╝")
            print("\t" * 8)
            return
    except ValueError:
        print("╔════════════════════════════════════════════╗")
        print("║  ERROR:  PROVIDE A VALID VALUE. !!         ║")    
        print("╚════════════════════════════════════════════╝")
        return
    total_prize_without_VAT = laptop['price'] * quantity
    VAT_amount = (0.13 * total_prize_without_VAT)
    total_prize_with_VAT = VAT_amount + total_prize_without_VAT

    laptop['quantity'] += quantity

    invoice = f"""
╔═══════════════════════════════════════════════════════════════╗
║                  ROCHAK-TOP-TECH HUB                          ║
║                   ITAHARI-4,SUNSARI                           ║
║                        025-586216                             ║
║===============================================================║
║                        INVOICE                                ║
║---------------------------------------------------------------║
║ DATE: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
║ DISTRIBUTOR NAME: {name_of_distributor.upper()}               
║---------------------------------------------------------------║
║ PRODUCT NAME:    {laptop_name.upper()}                        
║ QUANTITY NAME:   {quantity}                                   
║ AMOUNT: ${laptop['price']:.2f}                                
║---------------------------------------------------------------║
║ SUBTOTAL AMOUNT:   ${total_prize_without_VAT:.2f}             
║ SHIPPING CHARGE:   ${VAT_amount:.2f}                          
║ TOTAL AMOUNT:      ${total_prize_with_VAT:.2f}                
║---------------------------------------------------------------║
║                 THANKYOU FOR YOUR BUSINESS!                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(invoice);
    print("------------------------------------------------------------------------------")
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  INFORMATION MESSAGE : FOR INVOICE PLEASE CHECK TEXT FILE !!  ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("\t" * 8)
    with open(f"INVOICE_OF_PURCHASE.txt", "w", encoding="utf-8") as file:
        file.write(invoice)
        
     #this works on updating stock whenever laptop is sold 
    with open('laptops.txt', 'w') as file:
        for laptop_name, laptop_details in laptops.items():
            Name = laptop_name
            Brand = laptop_details['Brand Name']
            price = laptop_details['price']
            quantity = laptop_details['quantity']
            processor = laptop_details['processor']
            graphics = laptop_details['graphics']
            file.write(f"{Name}, {Brand}, ${price}, {quantity}, {processor}, {graphics}\n")
            
            
# function to check available laptops     
def laptops_available():
    laptops = laptop_ko_details()
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  S.N   Name of laptops             Quantity      Price        ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    SN = 1
    for Name, specs in laptops.items():
        print(f"   {SN}     {Name:<30}{specs['quantity']}         ${specs['price']}")

        SN +=1
    print("╚═══════════════════════════════════════════════════════════════╝")
    

#function to select what you want to do
def user_category_selection():
    while True:
        print("\t" * 8)
        print("******************************************************************************")
        print("""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║                  WELCOME TO ROCHAK-TOP-TECH HUB                    ║
║                                                                    ║
║====================================================================║
║ PLEASE SELECT A CATEGORY AS ( X/Y/S/Z ), ACCODING TO YOUR CHOICE:  ║
║                                                                    ║
║                   X = SALE LAPTOP                                  ║
║                   Y = PURCHASE LAPTOP                              ║
║                   S = AVAILABLE LAPTOPS                            ║    
║                   Z = EXIT SHOP                                    ║                                                                    
╚════════════════════════════════════════════════════════════════════╝ 
            
            """)
        option = input("ENTER ( X/Y/S/Z ) AS YOUR REQUIREMENTS: ")
        if option.upper() == "X":  
            Laptop_For_Selling()
        elif option.upper() == "Y":
            purchasing_laptop()
        elif option.upper() == "S":
            laptops_available()
        elif option.upper() == "Z":
            print("╔════════════════════════════════════════════════════════════════════════════╗")
            print("║                     THANKYOU !!  YOU HAVE EXITED                           ║")
            print("╚════════════════════════════════════════════════════════════════════════════╝")
            print("\t" * 8)
            print("*****************************************************************************")
            break;
        else:
            print("╔══════════════════════════════════════════════════════════════════════════════╗")
            print("║                 ENTER A VALID INPUT TO PROCEED FORWARD. !!                   ║")
            print("╚══════════════════════════════════════════════════════════════════════════════╝")
        
        
user_category_selection()





