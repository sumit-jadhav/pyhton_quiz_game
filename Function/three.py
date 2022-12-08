def paint_cal(height,width,cover):
    number_cans=round((height*width)/cover)
    print(f"you will need {number_cans} cans of paint")

test_h=int(input("Height of wall:"))
test_w=int(input("Width of wall:"))
coverage=5
paint_cal(height=test_h,width=test_w,cover=coverage)