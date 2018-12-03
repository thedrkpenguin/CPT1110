class NotaCorrectAnswer(Exception):
    def __init__(self,answer,message):
        Exception.__init__(self,message)
        #self.answer = answer
        self.__answer = answer

    def get_answer(self):
        return answer 
        
try:
    answer_list = [1,2,3,4,5]
    
    answer = int(input("Enter an answer to my question: "))

    if answer not in answer_list:
        raise NotaCorrectAnswer(answer, "is not in the list")
    else:
        print(answer, "is in the list")

except NotaCorrectAnswer as incorrect:
    #print(incorrect.answer, incorrect)
    print(incorrect.get_answer(), incorrect)

except TypeError:
    print("Can't convert string to integer")

except ValueError:
    print("I need an integer please")
    
