from kivy.app import App
from pytube import YouTube as Youtube
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class YoutubeDownloader(BoxLayout):
    youtubeurl = ObjectProperty(None)

    def Downloader(self):
        Youtube(self.youtubeurl.text).streams.get_highest_resolution().download("C:\\Users\\julio\\Videos")

class YoutubeAPP(App):
    pass


if __name__ == '__main__':
    YoutubeAPP().run()


    

