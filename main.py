import subprocess, requests, time, os, sys, itertools, threading, getpass

HWID = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/G09hL38n')
USER_INPUT = input("본인의 HWID 를 입력하시오 : ")

try:
    if USER_INPUT in r.text:
        if len(USER_INPUT) <= 5:
            done = False
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break 
                    sys.stdout.write('\033[33m' + '\r인증 중 ' + c + '\033[0m')
                    sys.stdout.flush()
                    time.sleep(0.1)
            t = threading.Thread(target=animate)
            t.start()
            time.sleep(3)

            os.system('cls')

            done = True
            
            print('\033[91m' + '[에러!] 관리자에게 문의하시오.' + '\033[0m')
            print('\033[96m' + f'You Entered HWID : {USER_INPUT}' + '\033[0m')
            time.sleep(1)
            os._exit()

        else:
            pass

    else:
        done = False
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break 
                sys.stdout.write('\033[33m' + '\r인증 중 ' + c + '\033[0m')
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()

        # 프로세스 길이
        time.sleep(3)
        os.system('cls')
        done = True

        print('\033[91m' + '[에러!] 관리자에게 문의하시오.' + '\033[0m')
        print('\033[96m' + f'You Entered HWID : {USER_INPUT}' + '\033[0m')
        time.sleep(1)
        os._exit()

except:
    print('\033[91m' + '[에러!] 연결 실패.' + '\033[0m')
    time.sleep(5) 
    os._exit() 
    
os.system('title HWID authentication by BSJ')
print('\033[96m' + f'You Entered HWID : {USER_INPUT}' + '\033[0m')

# 로딩
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break 
        sys.stdout.write('\033[33m' + '\r인증 중 ' + c + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

# 프로세스 길이
time.sleep(3)
os.system('cls')
done = True

# 인증 완료
print('\033[91m' + 'HWID 인증 완료!' + '\033[0m')
time.sleep(2)
os.system('cls')

# 메인 프로그램
print('\033[94m' + "메인 프로그램 코드" + '\033[0m')







