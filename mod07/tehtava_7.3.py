def gallona(gallona):
    litra = gallona * 3.785
    return litra

bensiini_g = input("Anna bensiini gallonoina: ")

while bensiini_g != "":
    bensiini_g = float(bensiini_g)
    bensiini_l = gallona(bensiini_g)
    print(f"{bensiini_g} gallonaa bensiiniä on {bensiini_l:.4f} litraa.")
    bensiini_g = input("Anna bensiini gallonoina: ")