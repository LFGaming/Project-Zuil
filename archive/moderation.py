import datetime

e = datetime.datetime.now()

keuzen = str(input("Is deze feedback goed gekeurd? "))

def moderation():
    with open('feedback_check.txt', 'r') as f:
        z = f.readlines()
        for n in z[2:]:
            print(n.strip())
            if keuzen == "goed":
                with open('feedbacks.txt', 'a') as t:
                    t.write(f"{n}")
                t.write(f" is goed gekeurd op: {str(e)}")

r = moderation()