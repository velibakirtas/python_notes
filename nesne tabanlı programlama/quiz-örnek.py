# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer        

# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.qIndex = 0
        
    def getQuestion(self):
        return self.questions[self.qIndex]        
    def display(self):
        question = self.getQuestion()
        print(f'soru {self.qIndex + 1}: {question.text}')
        
        for q in question.choices:
            print('-' + q)
            
        answer = input('cevap: ')            
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score +=1
            self.qIndex += 1
                    
        
    def loadQuestion(self):
        if len(self.questions) == self.qIndex:
            self.showScore
        else:
            self.display()             
    
    def showScore(self):
        pass                    
        
               
q1 = Question('en iyi programlama dili hangisidir?', ['C#', 'Python', 'Javascript', 'Java'], 'Python') 
q2 = Question('en popüler programlama dili hangisidir?', ['Javascript','C#', 'Python',  'Java'], 'Python')
q3 = Question('en çok kazandıra programlama dili hangisidir?', ['Python', 'C#', 'Javascript', 'Java'], 'Python')

questions = [q1, q2, q3]
sınav = Quiz(questions)
#quizi çalıştırdığımız anda init metodu ile score ve qIndex bilgisi 0'a eşitlenir
question = sınav.getQuestion
print(question)
#questions adında bir liste oluşturduk
# Quiz classına ait sınav adında bir obje oluşturduk
#init metoduyla objenin questions attributesine ulaştık
#yine init metodu aracılığıyla qIndex ile questions dizisinin ilk elemanına ulaştık(qIndex = 0)

print(q1.checkAnswer('Python'))
print(q2.checkAnswer('C#'))        

sınav.display()