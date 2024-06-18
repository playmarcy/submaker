import re


with open("text.txt", "r", encoding="utf-8") as text, open(
    "subs.txt", "w", encoding="utf-8"
) as subs:
    time_bag = "01:00"
    text = text.read()
    text_2 = re.findall(r"(?=(^.+?\n[A-Z Ş]+\n.+?$))", text, flags=re.MULTILINE)
    for i in range(len(text_2)):
        string = text_2[i].split("\n")
        if not (string[0][:1] + string[0][3:]).isdigit():
            string[0] = time_bag
        try:
            endtime = text_2[i + 1].split("\n")[0]
            if not re.fullmatch(r"\d\d:\d\d", endtime):
                raise ValueError
            time_bag = endtime
        except:
            endtime = time_bag
        subs.write(
            f"Dialogue: 0,0:{string[0]}.00,0:{endtime}.00,Default,{string[1]},0,0,0,,{string[2]}\n"
        )
    print("done")
