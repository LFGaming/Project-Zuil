keuzen = str(input("Is deze feedback goed gekeurd? "))

def moderation():
    with open('feedback_check.txt', 'r') as f:
        z = f.readlines()
        for n in z[2:]:
            print(n.strip())
        if keuzen == "goed":
            with open('feedbacks.txt', 'a') as t:
                t.write(n)

r = moderation()