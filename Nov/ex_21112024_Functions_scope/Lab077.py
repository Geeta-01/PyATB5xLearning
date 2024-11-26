public_toilet = "PB"

def home():
    private_toilet= "PT"
    public_toilet = "LPB" # local variable has high priority than global
    print(private_toilet)
    print(public_toilet)

home()