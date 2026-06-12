def profit_loss(sp,cp):
    return sp - cp

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

value = profit_loss(selling_price, cost_price)

print(f"Cost Price    : ₹{cost_price:.2f}")
print(f"Selling Price : ₹{selling_price:.2f}")


if value > 0:
    profit_percentage = (value/cost_price) * 100
    print(f"Profit     : {value:.2f}")
    print(f"Profit %   : {profit_percentage:.2f}")
elif value < 0:
    loss_percentage = (abs(value)/cost_price) * 100
    print(f"Loss     : {abs(value):.2f}")
    print(f"Loss %   : {loss_percentage:.2f}")

else :
    print("You are at breakeven")
