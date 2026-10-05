print ("Please, enter marks separated by commas")
marksRaw = input().split(",")
marks = []

for i in marksRaw:
    try:
        if (100 >= int(i) >= 0):
            marks.append(int(i))
    except ValueError:
        try: 
            if (100 >= float(i) >= 0):
                marks.append(float(i))
        except ValueError:
            continue

if not marks:
    print("No valid marks entered.")
else: 
    cnt = len(marks)
    avg = sum(marks)/cnt
    mx = max(marks)
    mn = min(marks)
    psrt = len([num for num in marks if num >= 50]) / cnt * 100
    print(f"Valid marks: {cnt}\nAverage: {avg:.2f}\nHighest: {mx}\nLowest: {mn}\nPass Rate: {psrt:.1f}%")
    