from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

formatting = """
<MyScreenManager>:
    StartScreen:
    CreateNewCharacterScreen:
    MainGameScreen:
<StartScreen>:
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
            text: 'Click Here to Continue'
            on_press: root.load_or_start_new(save_code.text)
<CreateNewCharacterScreen>:
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
            text: 'Enter Name Here'
            on_press: root.create_character(name.text)
<MainGameScreen>:
    name: 'game'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: display
            text: root.display
        BoxLayout:
            Button:
                text: 'Rob'
                on_press: root.rob()
                on_press: root.add_rep(-15)   
            Button:
                text: 'Work'
                on_press: root.work() 
                on_press: root.add_rep(3)            
"""
Builder.load_string(formatting)


class PlayerStatistics:
    def __init__(self, COINS=0):
        self.name: str = ""
        self.coins: int = COINS
        self.attributeDict = {"COINS": self.coins}

    def create_from_save(self):
        pass

    def set_name(self, username):
        self.name = username

    def increment_Coins(self, amount=1):
        self.coins = self.coins + amount

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
            "Name: " + self.name + "|" + str(self.rep
                                             + "\n" + "Coins: " + str(self.coins))

    def increment_rep(self, amount=0):
        self.rep = self.rep + amount
        pass


class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerStatistics)


class StartScreen(Screen):
    instructions = StringProperty(str('''
   Welcome to Coin Kings. Do you have what it takes to become a master of money, ruler of riches, director of dough? 
    '''))

    def load_or_start_new(self, savedata=''):
        # For now we always start a new game
        if savedata != '':
            self.load_game(savedata)
        else:
            self.start_new_game()
        pass

    def load_game(self, data):
        self.manager.current = 'character'
        pass

    def start_new_game(self):
        self.manager.current = 'character'
        pass

    pass


class CreateNewCharacterScreen(Screen):
    instructions = StringProperty(str('''
        All great kings need a name. What is yours?
        '''))
    fail_instructions = StringProperty(str('''
        All great kings need a name. What is yours?
        I said all great kings need a name. ENTER A NAME
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

    pass


class MainGameScreen(Screen):
    def get_data(self) -> PlayerStatistics:
        return self.manager.get_screen('character').data_stats

    display = StringProperty("error")

    # StringProperty("Name: " + "Dummy" + "\n" + "Coins: " + str(Coins))
    def work(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Coins(1)
        self.display = str(stats)

    def rob(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Coins(1)
        self.display = str(stats)


class GUIApp(App):
    def build(self):
        return MyScreenManager()


# Entry point into the game
if __name__ == '__main__':
    GUIApp().run()