import numpy as np
buy_list = []
price_list = []
buy_num_each = []

buy_num = int(input("تعداد خرید را وارد کنید "))
#در نظر گرفتن موارد ابتدایی
for _ in range(buy_num):
    buy = input("خرید مورد نظر را وارد کنید")
    buy_each = int(input("تعداد خرید را وارد کنید "))
    price = float(input("قیمت خرید را وارد کنید "))
    price_list.append(price)
    buy_list.append(buy)
    buy_num_each.append(buy_each)
    print("لیست خرید ها: ", buy_list)
    print("لیست قیمت ها: ", price_list)
    print("لیست تعداد خرید ها: ", buy_num_each)
# تخفیف و مالیات
price_list = [price + 3.5 for price in price_list]

if buy_num > 5:
    off_price = [round(price * 0.25) for price in price_list]
    full_price = [buy_num_each[i] * off_price[i] for i in range(buy_num)]
    print("لیست قیمت ها با تخفیف: ", full_price)
else:
    print("تخفیف وجود ندارد")
    full_price = [buy_num_each[i] * price_list[i] for i in range(buy_num)]
    print(f"قیمت کل بدون تخفیف{full_price}")


print(f"your list of buys : {buy_list} and number of all of goods you buy is : {buy_num} and the total price of all of goods you buy is : {sum(full_price)} thanks for come to our shop")

total_price = sum(full_price)
a = total_price
b = 0
b += a
print("and the full salary for the shop is : ", b )
