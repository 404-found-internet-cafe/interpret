def check(item):
    LIKES = ["eyes", "dimples", "shirt", "fingers", "way that you smell"]

    if item in LIKES:
        return True
    else:
        return False
    
















































if __name__ == "__main__":
    while True:
        x = input("What do you like? ").lower()
        if check(x) == True:
            print("Same.")
        else:
            print("Nah.")
        print("\n")