student_names = ["Andrew", "ARay", "AKRay", "Too Far!"]

for name in student_names:
    if name == "AKRay":
        print(f"Found him! {name}")
        break
    print(f"Currently testing {name}") #Break out of loop


for name in student_names:
    if name == "ARay":
        continue
        print(f"Found him! {name}")
    print(f"Currently testing {name}") #continue loop to skip remaining statements in loop and continue with next iteration
