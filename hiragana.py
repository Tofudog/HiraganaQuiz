import kivy

from kivy.lang import Builder
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget


import glob
import random
import os

print(os.getcwd())
print(glob.glob("Images/*.jpg"))



# class Quiz(GridLayout):
    
#     def build(self):
#         self.title = "Hiragana Quiz"
#         #self.icon = ...
#         self.window = GridLayout()
#         self.window.rows = 5
#         self.window.cols = 3
        
        
#         ### row1
#         #maybe add jap. img.
#         self.window.add_widget(Label(text=''))
#         title_screen = "[u]Welcome to the Hiragana Quiz![/u]"
#         self.window.add_widget(
#             Label(text=title_screen, markup=True)
#             )
#         self.window.add_widget(Label(text=''))
#         ### end row1
        
#         ### row2
#         self.window.add_widget(Label(text=''))
#         letter_img = Image(source='Hiragana//a.jpg')
#         # need to add image into label
#         surr_box = Label(
#             outline_color='red', outline_width=1,
            
#             )
#         self.window.add_widget(
#             surr_box
#             )
#         self.window.add_widget(Label(text=''))
#         ### end row2
        
#         ### row3
#         # add on_press func.
#         start_button = Button(
#             text="Start", font_size=14, background_color='pink', color='white',
            
#             )
#         self.window.add_widget(start_button)
        
        
#         ### to be changed
#         answer_list = ['a', 'e', 'i', 'o']
        
#         answer_box = BoxLayout(orientation="horizontal")
#         answer_box.add_widget(
#                 Button(text='a', font_size=18, background_color='#FFFFFF', color='red',
#                         size_hint=(0.3, 0.2))
#                 )
#         answer_box.add_widget(
#         Button(text='a', font_size=18, background_color='#FFFFFF', color='red',
#                 size_hint=(0.3, 0.2))
#         )
#         answer_box.add_widget(
#         Button(text='a', font_size=18, background_color='#FFFFFF', color='red',
#                 size_hint=(0.3, 0.2))
#         )
#         answer_box.add_widget(
#         Button(text='a', font_size=18, background_color='#FFFFFF', color='red',
#                 size_hint=(0.3, 0.2))
#         )
        
        
        
#         # for ans in answer_list:
#         #     answer_box.add_widget(
#         #         Button(text=ans, font_size=18, background_color='#FFFFFF', color='red',
#         #                size=(55, 10))
#         #         )
            
#         self.window.add_widget(answer_box)
        
#         self.window.add_widget(Label(text=''))
#         ### end row3
        
        
#         ### row4
#         self.window.add_widget(Label(text=''))
#         self.window.add_widget(Label(text=''))
#         self.window.add_widget(Label(text='Timer: ()'))
#         ### end row4
#         return self.window


class Game:
    
    def __init__(self, imgs):
        self.imgs = imgs
        self.answers = {}
        for path in imgs:
            self.answers[path] = path.split('\\')[-1].split('.')[0]
        self.currImg = list(self.answers.keys())[0]
        self.currAns = self.answers[self.currImg]
        del(self.answers[self.currImg])
            
    def nextQuestion(self):
        question = random.choice(list(self.answers.keys()))
        #path, ans = zip(question, self.answers[question])
        self.currImg = question
        self.currAns = self.answers[question]
        del(self.answers[question])

        

Builder.load_file('hiragana.kv')
class Quiz(Widget):
    
    def startQuiz(self):
        print("Started!")
        self.ids.startButton.disabled = True
        self.game = Game(
            glob.glob("Images/*.jpg")
            )
        print(self.game.answers)
        
         
    
    def timer(self):
        pass
    
    def setAnswer(self, ans):
        if ans==self.game.currAns:
            self.ids.scoreTracker.text = str(eval(self.ids.scoreTracker.text)+1)
        print("You chose:", ans)
        print("The correct answer is:", self.game.currAns)
        print(ans==self.game.currAns)
        
    def clickNext(self):
        # mutator method for setting img & ans
        self.game.nextQuestion()
        # perhaps obtain a copy
        all_answers = list(self.game.answers.values())
        answer_list = [self.game.currAns, all_answers[0],
                       all_answers[1], all_answers[2]]
        random.shuffle(answer_list)
        for i in range(4):
            self.ids[f'response{i+1}'].text = answer_list[i]
        
        self.ids.letter_img.source = self.game.currImg
        
        


    
class MyWebsite(App):
    
    def build(self):
        return Quiz()
        


MyWebsite().run()






