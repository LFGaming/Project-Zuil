
def show():
    with open('feedbacks.txt', 'r') as f:
        print(f.read())
r = show()