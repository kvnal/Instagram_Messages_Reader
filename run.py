import json
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def msg(filename):
    with open(filename,encoding="mbcs") as file:
        return json.loads(file.read())

def participants(msg):
    direct=[]
    for _ in range(len(msg)):
        name=msg[_]['participants']
        direct.append(name[0] if name[0] not in direct else name[1])
    return direct


def chats(msg,username2):
    for _ in range(len(msg)):
        if username2 in msg[_]['participants']:
            chatno=_
            break
        
    for _ in range(len(msg[chatno]['conversation'])-1,-1,-1):
        try:
            print(msg[chatno]['conversation'][_]['sender']+" : "+msg[chatno]['conversation'][_]['text'].translate(non_bmp_map)+" \n@ "+msg[chatno]['conversation'][_]['created_at'])
            print()
        except:
            print('*Not readable*')
            pass
    return 0        

if __name__ == "__main__":    
    try:
        if sys.argv[1]=='-p':
            for i,_ in enumerate(participants(msg(sys.argv[2]))):
                print("{}. {}".format(i,_))            
        elif sys.argv[1]=='-c':
            chats(msg(sys.argv[3]),sys.argv[2])
    except:
        print("Error!")
        pass

    pass