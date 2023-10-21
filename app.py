from flet import *

import yt_dlp
import time
import os
from moviepy.editor import AudioFileClip


def main(page:Page):
    page.title="M99"
    page.bgcolor=colors.BLACK26
    page.window_width=320
    page.window_height=600
    page.update()
    page.window_center()

    Listtype=["MP3","MP4"]

    # def oncharge(e):
    #     t1.value="correct link"
    #     page.update()
    def getlink():
        return link.value
    def gettype():
        return drop.value



    def download(e):

        url=getlink()
        tp=gettype()

        if tp.lower()=="mp3":
            ytb={
                'format':'bestaudio/best',
                'outtmpl':'%(title)s.%(ext)s',
            }
        elif tp.lower()=="mp4":
            ytb={
                'format':"best",
                'outtmpl':'%(title)s.%(ext)s',
            }
        with yt_dlp.YoutubeDL(ytb) as down:
                
                info=down.extract_info(url)
                # place=os.path.join(os.path.expanduser("-"), "Downloads")
                down.download(url)
                name=f"{info.get('title')}.webm"
                mp3_output=f"{info.get('title')}.mp3"
                time.sleep(3)
                if os.path.exists(name):
                    audio=AudioFileClip(name)
                    audio.write_audiofile(mp3_output)
                    os.remove(name)
    
    link=TextField(
            height=50,
            border_color="white",
            focused_border_color=colors.BLUE_200,
            label="enter url of video",
            prefix_icon=icons.LINK,
            )
    t1=Text(color=colors.GREEN_100)
    c=Column(
        controls=[
            Row(controls=[
            Text("M99",size=40,color=colors.BLUE_300),
            Text("Downloader",size=30),
            ],
            alignment="center"
            ),
            link,
            t1,
        ],spacing=100
    )

    btn1=Row(controls=[
            ElevatedButton(
                text="Download",
                color=colors.BLACK,
                bgcolor=colors.WHITE,
                icon=icons.DOWNLOAD,
                on_click=download,
                height=45
                
            ),],alignment="center")


    drop=Dropdown(
            hint_text="Mp3/Mp4",
            border_color=colors.WHITE,
            options=[
                dropdown.Option(Listtype[0]),
                dropdown.Option(Listtype[1]),
                    ],
            )
    
    row1=Row(
        [
            Container
            (
        width=150,
        content=drop,
            )
        ],
        alignment="center"
    )

    page.add(c)

    page.add(row1)
    page.add(btn1)


if "__main__"==__name__:
    app(main)