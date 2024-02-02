

import google.generativeai as genai

genai.configure(api_key="Google api key")

model = genai.GenerativeModel('gemini-pro')

state = 1
while(state):
    response = model.generate_content(input("enter the question"))
    print (response.text)
    in1 =int(input("true = 1 or false = 0"))
    state = in1
