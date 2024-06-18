import re

sub_data = """[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,10,1
Style: Main,Tahoma,22,&H00FFFFFF,&H000000FF,&H00000000,&H96000000,0,0,0,0,100,100,0,0,1,2.6,1,2,20,20,25,204
Style: Main_Top,Tahoma,22,&H00FFFFFF,&H000000FF,&H00000000,&H96000000,0,0,0,0,100,100,0,0,1,2.6,1,8,10,10,25,204
Style: Main_Italic,Tahoma,22,&H00FFFFFF,&H000000FF,&H00000000,&H96000000,0,-1,0,0,100,100,0,0,1,2.6,1,2,10,10,25,204
Style: Main_Top_Italic,Tahoma,22,&H00FFFFFF,&H000000FF,&H00000000,&H96000000,0,-1,0,0,100,100,0,0,1,2.6,1,8,10,10,25,204
Style: Main_Flashback,Tahoma,22,&H00FFFFFF,&H000000FF,&H00500000,&H96500000,0,0,0,0,100,100,0,0,1,2.6,1,2,20,20,25,204
Style: Main_Flashback_Italic,Tahoma,22,&H00FFFFFF,&H000000FF,&H00500000,&H96500000,0,-1,0,0,100,100,0,0,1,2.6,1,2,20,20,25,204
Style: SIGNS,Tahoma,22,&H00FFFFFF,&H00000002,&H00000000,&H00000000,-1,0,0,0,113.793,100,0,0,1,1,0,8,40,40,25,0
Style: Main_Flashback_Top,Tahoma,22,&H00FFFFFF,&H000000FF,&H00500000,&H96500000,0,0,0,0,100,100,0,0,1,2.6,1,8,10,10,25,204

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"""

file = input("Имя файла: ")

with open(f"{file}.txt", "r", encoding="utf-8") as text, open(
    f"{file}.ass", "w", encoding="utf-8"
) as subs:
    subs.write(sub_data)
    text = text.read().replace("\n\n", "\n").split("\n")
    for numb, string in enumerate(text):SW_EPS_24_ASR
        if numb % 2 == 0:
            time = re.findall(r":(\d\d:\d\d:\d\d)]", string)
            starttime = time[0]
            dot = starttime.rfind(":")
            starttime = starttime[:dot] + "." + starttime[dot + 1 :]
            try:
                endtime = time[1]
                dot = endtime.rfind(":")
                endtime = endtime[:dot] + "." + endtime[dot + 1 :]
            except:
                endtime = starttime
            name = re.findall(r"].*](.+?)$", string)
        if numb % 2 == 1:
            text = string
            if endtime == "00:00:00":
                endtime = starttime
            subs.write(
                f"Dialogue: 0,0:{starttime},0:{endtime},Default,{name[0]},0,0,0,,{text}\n"
            )
    print("done")
