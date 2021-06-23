def solution(m, musicinfos):
    m = m.replace('A#','H');
    m = m.replace('C#','I');
    m = m.replace('D#','J');
    m = m.replace('F#','K');
    m = m.replace('G#','L');
    answer = ''
    result = None
    dic = dict()
    for info in musicinfos:
        start, end, title, sound = info.split(',')
        hour1, min1 = start.split(':')
        hour2, min2 = end.split(':')
        time = (int(hour2)-int(hour1))*60 + int(min2)-int(min1)
        print(time)
        sound = sound.replace('A#','H');
        sound = sound.replace('C#','I');
        sound = sound.replace('D#','J');
        sound = sound.replace('F#','K');
        sound = sound.replace('G#','L');
        sound = sound*(time//len(sound))+sound[0:time%len(sound)]
        dic[sound] = title
    for song in dic.keys():
        if m in song:
            if result == None:
                result = song
            else:
                if len(result) < len(song):
                    result = song
    if result != None:
        return dic[result]
    else: return "(None)"


if __name__ == '__main__':
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))