from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widgetformatting
"""
<MyScreenManager>:
    StartScreen:
    CreateNewCharacterScreen:
    MainGameScreen:<StartScreen>:
    name: 'start'
    BoxLayout:
        orientation: 'vertical'
        Label:
            color: [1,0,0,1]
            text: root.instructions  
            font_size: 40 
        TextInput:
            id: save_code
            font_size: 28
        Button:
            text: 'Press me to go to the Game Screen'
            on_press: root.load_or_start_new(save_code.text)<CreateNewCharacterScreen>:
    name: 'character'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: instr
            size: self.texture_size
            text: root.instructions  
        TextInput:
            id: name
            font_size: 28
        Button:
            text: 'Enter a name for your character'
            on_press: root.create_character(name.text)<MainGameScreen>:
    name: 'game'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: display
            text: root.display
        BoxLayout:
            Button:
                text: 'Read a Book'
                on_press: root.read_a_book()
                on_press: root.add_time(25)   
            Button:
                text: 'Workout'
                on_press: root.workout() 
                on_press: root.add_time(15)            
"""
Builder.load_string(formatting)
class PlayerStatistics:
    def __init__(self, strength=0, wisdom=0, time=0):
        self.time: int = time
        self.name: str = ""
        self.strength: int = strength
        self.wisdom: int = wisdom
        self.attributeDict = {"STR": self.strength, "WIS": self.wisdom}
def create_from_save(self):
    class Dataimporter():
        def __init__(self, string):
            self.data = self.convertStringtoDict(string) @ staticmethod

        def convertStringtoDict(string: str) -> dict:
            """ I am given a string that contains text then a colon, then text then a colon then text
                I want to turn that into a dictionary"""
            string = string.replace("{", "")
            string = string.replace('}', "")
            string = string.replace("'", "")
            List = string.split(',')
            Dict = {}
            for element in List:
                (key, value) = element.split(':')
                Dict[key] = value
            print(Dict)
            return Dict @ staticmethod

        def convertDicttoString(data: dict) -> str:
            """ I am given a Dictionary that I want to convert into a String that contains text then a colon, then text then a colon then text
                where the text is a key and the number is the key's value """
            return str(data)

            class PlayerData:

        # Init normal values, as well as tracker variables for those values
        def __init__(self, savedatadict: dict = None):
            if savedatadict is not None:
                print(str(savedatadict))
                # Things I want to save?
                self.cookies: int = 0
                self.pointers: int = 0
                self.name: str = ""
            else:
                self.cookies = savedatadict.get('cookies')
                self.pointers = savedatadict.get('pointers')
                self.name = savedatadict.get('name')

        def SaveCurrentData(self):
            data = {'cookies': self.cookies, 'pointers': self.pointers, 'name': self.name}
            print(data)
            return dataclass
            MyScreenManager(ScreenManager, Widget):

        data = ObjectProperty(PlayerData)

        class WelcomeScreen(Screen):
            instructions = StringProperty(str('''
        Welcome to the Android's Cookie Clicker Clone! Hope you have a nice time.
        If it's your first time playing, press the button below to continue.
        If you wish to load a save, type your save code and continue
        '''))  # def SaveCurrentData(self):

        #     data = {'cookies': self.cookies, 'pointers': self.pointers, 'name': self.name}
        #     return data
        # Unfinished: Later issue
        def load_or_start_new(self, savedata=''):
            # For now we always start a new game
            if savedata != '':
                self.loadSave(savedata)
            else:
                self.createNewSave()
            pass  # Right now load and new do the same thing, but that might change in the future

        def loadSave(self, data_string: str):
            dataDict = Dataimporter.convertStringtoDict(data_string)  # Load in save info
            self.manager.LoadData(dataDict)
            self.manager.current = 'game'
            pass

            def createNewSave(self):
                self.manager.current = 'load'

            pass
            passclass
            LoadSaveScreen(Screen):

        defaultText = StringProperty(str('''
        Type in a name for yourself
        '''))
        failText = StringProperty(str('''
        Give yourself a name to continue to play you absolute dingus
        '''))
        data_stats: PlayerData = ObjectProperty(PlayerData)  # Load SaveData here

        def LoadData(self, data: dict):
            self.data_stats = PlayerData(data)
            self.manager.get_screen('game').display = str(self.data_stats)
            self.manager.get_screen('game').pointercosttext = str(self.data_stats.pointerCost)
            pass  # Create a new save data if text field isn't blank

        def createSaveData(self, username):
            if username != '':
                self.data_stats = PlayerData()
                self.data_stats.setName(username)
                self.manager.get_screen('game').display = str(self.data_stats)
                self.manager.get_screen('game').pointercosttext = str(self.data_stats.pointerCost)
                self.manager.current = 'game'
            # Display failText until textbox is no longer empty
            else:
                self.defaultText = self.failText
            pass
            pass
    def set_name(self, username):
        self.name = username
    def increment_Strength(self, amount=1):
        self.strength = self.strength + amount
        def increment(self, parameter, amount=1):
            if self.attributeDict.__contains__(parameter):
                self.attributeDict[parameter] = self.attributeDict[parameter] + amount
            else:
        print("That Parameter does not exist")
        def increment_Wisdom(self, amount=1):
        self.wisdom = self.wisdom + amount
        pass
def __str__(self):
        return str(
            "Name: " + self.name + "|" + "time: " + str(self.time)
            + "\n" + "Strength: " + str(self.strength)
            + "\n" + "Wisdom: " + str(self.wisdom)
        def increment_Time(self, amount=1):
            self.time = self.time + amount
        pass# Create the screen manager = sm
class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerStatistics)
    class StartScreen(Screen):
        instructions = StringProperty(str('''
    Welcome to this fun game!
    If you're new to the game or you want to start from the beginning just press the button!
    Otherwise, first paste in your save code, and then press the button to load the game.
    '''))
    def load_or_start_new(self, savedata=''):
        # For now we always start a new game
        if savedata != '':
            self.load_game(savedata)
        else:
            self.start_new_game()
        pass    # Right now load and new do the same thing, but that might change in the future
    def load_game(self, data):
        self.manager.current = 'character'
        pass
    def start_new_game(self):
        self.manager.current = 'character'
        pass
        passclass
        CreateNewCharacterScreen(Screen):
    instructions = StringProperty(str('''
        This world is unlike any world you've known before. Great Things await. But first, you'll need a name...
        '''))
    fail_instructions = StringProperty(str('''
        This world is unlike any world you've known before. Great Things await. But first, you'll need a name...
        FOOLISH MORTAL!!! ENTER A NAME FIRST BEFORE YOU CLICK THE BUTTON. 
        '''))
    data_stats: PlayerStatistics = ObjectProperty(PlayerStatistics)
    def create_character(self, username):
        if username != '':
            self.data_stats = PlayerStatistics()
            self.data_stats.set_name(username)
            self.manager.get_screen('game').display = str(self.data_stats)
            self.manager.current = 'game'
        else:
            self.instructions = self.fail_instructions
        pass
        passclass MainGameScreen(Screen):
    def get_data(self) -> PlayerStatistics:
        return self.manager.get_screen('character').data_stats    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")    # StringProperty("Name: " + "Dummy" + "\n" + "Strength: " + str(Strength))    def workout(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Strength(1)
        self.display = str(stats)
    def read_a_book(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Wisdom(1)
        self.display = str(stats)
    def add_time(self, amount):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Time(amount)
        self.display = str(stats)
        class GUIApp(App):
         def build(self):
            return MyScreenManager()# Entry point into the game
if __name__ == '__main__':
    GUIApp().run()