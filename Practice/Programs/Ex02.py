#There are two friends, John and Smith,
# and the parameters j_angry and s_angry to indicate if each is angry.
# You are in trouble if both of them are angry or no one of them is angry.

def friends_in_trouble(j_angry, s_angry):
    if j_angry and s_angry:
        print("Since both of them are angry,\nso you are in trouble.")
    elif not(j_angry) and not(s_angry):
        print("Since both of them are angry,\nso you are in trouble.")
    else:
        print("Only one of them is angry,\nso we are not in trouble.")

friends_in_trouble(False, True)
