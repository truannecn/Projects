while True:
    temp = int(input("Please input an integer (negative to quit): "))

    
    # Check whether the input is a negative number
    if temp < 0:
        break
    
    # Start to work on persistence
    num = temp
    prod_count = 0
    print("\nMultiplicative loop:")
    while num // 10 > 0:
        product_num = 1
        prod_count += 1
        while num > 0:
            d = num % 10
            #print(d)
            product_num *= d
            num = num // 10
        print("Product:", product_num)
        
        num = product_num

        
    num = temp
    sum_count = 0
    print("\nAdditive loop:")
    while num // 10 > 0:
        sum_num = 0
        sum_count += 1
        while num > 0:
            d = num % 10
            #print(d)
            sum_num += d
            num = num // 10
        print("Sum:", sum_num)
        
        num = sum_num
        
    print("\nFor the integer:", temp)
    print("\tMultiplicative Persistence:", prod_count, " Multiplication root:", product_num)
    print("\tAdditive Persistence:", sum_count, " Additive root:", sum_num)
        
        
print("Thanks for playing! :)")