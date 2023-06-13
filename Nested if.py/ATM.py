Total_balance=40000
print("Welcome")
print("Please insert your card")
print("Hi please do not remove your card")
print("1. English" , "2. Hindi" , "3.Bengali")
lan=input("Select your language=")
if lan=="English" or lan=="Hindi":
    pin=int(input("Please enter your PIN  "))
    a=1924
    if pin==a:
        print("1.balance inquiry","2.Banking","3.Generate PIN")
        b=input("Please chose banking for cash withdrawal=")
        if b=="Banking":
            print("1.Deposit","2.Fast cash","3.Withdrawal")
            c=input("Please select Transaction=")
            if c=="Deposit":
                print("1.Other Account", "2.Cash Deposit", "3.Main Manu")
                d=input("Please select diposit Transaction=")
                if d=="Cash Deposit":
                    # print("Please wait")
                    print("1.Current", "2.Saving")
                    e=input("Plese select accout type=")
                    if e=="Saving":
                        print("Transaction is being processed")

                        cash=int(input("Please insert your cash="))
                        if cash>=500 or cash<=20000:
                            k=cash//20000
                            l=cash%20000
                            m=l//500
                            n=l%500
                            o=n//200
                            p=n%200
                            q=p//100
                            r=p%100
                            s=r//50
                            t=r%50
                            u=t//20
                            v=t%20
                            w=v//10
                            x=v%10
                            y=x//5
                            z=x%5
                            print("Note of 2000=",k,"Note of 500=",m,"Note of 200=",o,"Note of 100=",q,"Note of 50=",s,"Note of 20=",u,"Note of 10=",w,"Note of 5=",y)
                            print("1.Enter","2. Cancel")
                            f=input("Press ENTER to proceed or press Cancle to finish transaction=")
                            if f=="Enter":
                                print("Please wait")

                                print("1. Confirm","3. Cancel")

                                g=input("Enter your selection= ")
                                if g=="Confirm":
                                    print("Transaction compleate")
                                    print("Available Balance=",Total_balance+cash)
                                else:
                                    print("canceled")
                            else:
                                print("Finished Transaction")
                        else:
                                print("Enter valid amount") 
                    else:
                        print("Follow the instructions")
                else:
                    print("Follow the steps")
            elif c=="Withdrawal":
                print("1. KCC", "2. Current","3. Saving")
                h=input("Please select Account type=")
                if h=="Saving":
                    i=int(input("Please Enter Amount="))
                    if i>=500 and i<=20000:
                        print("1. Yes","2.No")
                        j=input("Enter yes or no =")
                        if j=="Yes":
                            print("Your transaction is being peocessed please wait.....")
                            print("Please colect cash")
                            print("Transaction coplete")
                            print("Available balance=", Total_balance-i)
                        else:
                            print("transaction Canceled")
                    else:
                        print("Enter correct amount")
                else:
                    print("Follow the Instructions")
            else:
                print("Error")
        else:
            print("Follow the given Instruction")
    else:
        print("Please enter correct PIN" )
else:
    print("Enter valid language")
        

                          

