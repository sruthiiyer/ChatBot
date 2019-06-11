import requests
import text2voice as t2v
import speech2txt as s2t

import speech_recognition as sr

while(True):
    
    x=" "
    
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('say something')
            
        audio=r.listen(source)
        
        print("HEARDDD")
    
        x=s2t.function(audio)
        
        print("Hey thereee")

    print(x)    


    url = "https://qnamakerimpiger.azurewebsites.net/qnamaker/knowledgebases/6daf928a-fb59-46b4-8ce3-7bd246bb3744/generateAnswer"

    qn = {"question":x}
    payload = str(qn)
    headers = {
    'Content-Type': "application/json",
    'Authorization': "EndpointKey 181b1a71-f529-4a62-b5af-818f8c300a66",
#    'User-Agent': "PostmanRuntime/7.13.0",
#    'Accept': "*/*",
#    'Cache-Control': "no-cache",
#    'Postman-Token': "5635bb3b-6af8-420e-b5ea-d7ba1252433a,ced1c1ca-9365-42cd-b424-e26bb9927f22",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
#
#print((response.text))

    ans=response.text
    s2="answer"
    final=ans[ans.find(s2,10)+len(s2)+3:ans.rfind('score',4)-3]
    print(final)
    with open("chatbot.txt","w") as file:
        file.write(final)
    file.close()
    t2v.voiceconvert("chatbot.txt")
    y=int(input("Do you want to ask another question(0/1):"))
    if(y==0):
        break;
    