import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "3e6abb80-74a9-11ec-9ed4-a70226fed41e6e6c5173-78ff-4053-8972-4956155ded1d"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
    question = input("> ")
    answer = classify(question)
    answerclass = answer["class_name"]

    if answerclass == "emasesa":
        print ("Vale, le ponemos en contacto con EMASESA")
        print (answerclass)
    elif answerclass == "emvisesa":
        print ("Vale, le ponemos en contacto con EMVISESA")
    elif answerclass == "lipasam":
        print ("Vale, le ponemos en contacto con LIPASAM")
    elif answerclass == "tussam":
        print ("Vale, le ponemos en contacto con TUSSAM")

print ("Bienvenido, ¿sobre que empresa pública desea realizar la consulta?")

while True:
   answer_question()