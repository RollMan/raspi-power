def find_optimized_register(r2, v_cc=12, v_G=11, r3=500000):
    r1 = ((v_cc - v_G)*r3 + (v_cc - v_G)*r2)/v_G
    return r1


print(find_optimized_register(10000))
