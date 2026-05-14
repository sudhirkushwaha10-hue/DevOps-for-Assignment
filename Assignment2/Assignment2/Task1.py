# cost_price=float(input("enter the cost_price:"))
# selling_price=float(input("enter the selling_price:"))
# profit=selling_price-cost_price
# loss=cost_price-selling_price
# result=("profit", "loss") [cost_price>selling_price]
# print(result)


cost_price=float(input("enter the cost_price:"))
selling_price=float(input("enter the selling_price:"))
profit=selling_price-cost_price
loss=cost_price-selling_price
profit_percentage=profit/cost_price*100
loss_percentage=loss/cost_price*100
if selling_price>cost_price:
    print("profit is :",profit)
else:
    print("loss is:",loss)

if selling_price>cost_price:
    print("profit_percentage is:",profit_percentage)
else:
    print("loss_percentage is",loss_percentage)

