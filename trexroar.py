# python3.12 -m venv venv
# source venv/bin/activate
# pip3 install --user cowsay


import cowsay

def pythonsay(text):
    snake = """
       --..,_                     _,.--.
        \\ __  '``-..___..---'`   _.--*@\\`
           `--.._               _..--'
                `--.._______..--'
    """
    print(snake)
    cowsay.trex(text)

pythonsay('Hello from Python!')

