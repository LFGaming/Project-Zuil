keuzen = str(input("Is deze feedback goed gekeurd? "))

def moderation():
    with open('feedback_check.txt', 'r') as f:
        print(f"{f}")
        if keuzen == "goed":
            with open('feedbacks.txt', 'a') as t:
                t.write(f"")