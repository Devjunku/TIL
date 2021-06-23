## replace 메소드는 해당 객체에 저장이 안됨.
## 그니까 기억해라..
def trans_tune(melody):
    melody = melody.replace('C#', 'H')
    melody = melody.replace('D#', 'I')
    melody = melody.replace('F#', 'J')
    melody = melody.replace('G#', 'K')
    melody = melody.replace('A#', 'L')
    return melody

def solution(m, musicinfos):
    
    m = trans_tune(m)
    result = None
    music_dic = {}

    for music in musicinfos:
        s, e, title, melody = music.split(',')
        h1, m1 = s.split(':')
        h2, m2 = e.split(':')
        time = (int(h2) - int(h1)) * 60 + (int(m2) - int(m1))
        melody = trans_tune(melody)
        melody = melody * (time // len(melody)) + melody[0:time % len(melody)]
        music_dic[melody] = title

    for song in music_dic.keys():
        if m in song:
            if result == None:
                result = song
            else:
                if len(result) < len(song):
                    result = song
    
    if result != None:
        return music_dic[result]
    else:
        return '(None)'
    

if __name__ == '__main__':
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))