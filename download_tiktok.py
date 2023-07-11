# #13547a
# #80d0c7
# #0f172a s-9
# #475569 s-6
from datetime import datetime
import re

import clipboard
import requests
from flet import (
    flet,
    Page,
    Column,
    Row,
    alignment,
    padding,
    ResponsiveRow,
    border,
    Container,
    Text,
    margin,
    LinearGradient,
    PopupMenuButton,
    PopupMenuItem,
    icons,
    IconButton,
    transform,
    animation,
    Image,
    CircleAvatar,
    TextField,
    colors,
    ElevatedButton, TextButton, InputBorder, TextStyle

)


def main(page: Page):
    def page_resize(e):
        pw.value = f"{page.width} px"
        pw.update()

    page.on_resize = page_resize

    pw = Text(bottom=50, right=50, style="displaySmall")
    page.overlay.append(pw)

    #
    def download_video(e):
        url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
        video_url = url_tiktok_textField.value

        querystring = {"url": video_url}

        headers = {
            "X-RapidAPI-Key": "c222310903mshb5d1b8c262a58c6p16a432jsn6a46191623eb",
            "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring, allow_redirects=True)

        data = response.text
        video = data.replace('[', '')
        link = re.findall(r'{"video":"([^"]+)"', video)
        url_video = ''.join(link)

        now = datetime.now()
        name = f'tiktok_{now.strftime("%Y%m%d%H%M%S")}.mp4'

        r = requests.get(url_video)
        open(name, "wb").write(r.content)

    #
    def paste_click(e):
        url_tiktok = clipboard.paste()
        url_tiktok_textField.value = url_tiktok
        page.update()

    #
    def delete_click(e):
        url_tiktok_textField.value = ""
        page.update()

    #
    def on_button(e):
        if url_tiktok_textField.value() != "":
            url_delete.disabled = False
            url_delete.update()
            url_paste.disabled = True
            url_paste.update()
        else:
            url_paste.disabled = False
            url_paste.update()
            url_delete.disabled = True
            url_delete.update()

        return on_button

    #
    _nav = Container(
        ResponsiveRow([
            Column(col={"xs": 12, "sm": 12, "md": 12, "xl": 12},
                   controls=[
                       Container(
                           padding=20,
                           bgcolor="#DEDEDE",
                           content=Row([
                               CircleAvatar(
                                   width=60,
                                   height=60,
                                   bgcolor="white",
                                   content=
                                       Text("TD",
                                            size=30,
                                            weight="w900",
                                            color="black",
                                            text_align="center",
                                            ),

                               ),

                           ], alignment="spaceBetween")
                       )
                   ]
                   )
        ]),
    )

    # titles
    _title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 12, "sm": 10, "md": 10, "xl": 12},
                alignment=alignment.top_center,
                padding=30,
                content=Text('Tải Video TikTok Miễn Phí.',
                             size=40,
                             weight="w600",
                             text_align="center",
                             ),
            )
        ],
    )

    #
    url_tiktok_textField = TextField(
        border=InputBorder.NONE,
        content_padding=padding.only(
            top=0, bottom=0, right=20, left=20),
        hint_style=TextStyle(
            size=16, color='#9DB2BF'
        ),
        text_style=TextStyle(
            size=18,
            color='black',
        ),
        hint_text='Dán liên kết Tiktok vào đây',
        cursor_color='black',
        width=386,
        height=50,
        # content_padding=10,
        # focused_border_width=2,
        # label="Dán liên kết Tiktok vào đây",
        # border_color="black",
        # # border="none",
        # border_radius=10,
        # # hint_text=("Dán liên kết Tiktok vào đây"),
        # color='black',
        # width=540,
        # height=50,
        # bgcolor='white',
        col={"sm": 8, "md": 12, "lg": 10, "xl": 12},
    )

    #
    url_paste = Container(
        # col={"sm": 2, "md": 2, "lg": 2, "xl": 2},
        visible=True,
        height=49,
        width=70,
        bgcolor="blue600",
        border_radius=10,
        padding=0,
        content=TextButton("Paste", on_click=paste_click, height=50),
    )
    url_delete = Container(
        visible=False,
        height=49,
        width=70,
        bgcolor="blue600",
        border_radius=10,
        content=TextButton("Delete", on_click=delete_click, height=50)
    )
    url_download = Container(
        # col={"sm": 10, "md": 8, "lg": 1, "xl": 1},
        visible=True,
        height=50,
        width=90,
        bgcolor="blue600",
        border_radius=10,
        padding=0,
        content=TextButton("Download", on_click=download_video, height=50, width=70),
    )
    # url_download = ElevatedButton("Download", on_click=download_video, height=50)

    # _item_row = ResponsiveRow(
    #     # alignment="center",
    #     vertical_alignment="center",
    #     controls=[
    #         Container(
    #             col={"xs": 8, "sm": 6, "md": 8, "xl": 12},
    #             content=url_tiktok_textField,
    #         ),
    #     ],
    # )

    # url_responsive_paste = ElevatedButton("Paste", on_click=paste_click, height=50),

    # url_button = Row(
    #     alignment="center",
    #     vertical_alignment="center",
    # )
    # 7/6/23
    _item = [url_paste, url_delete]
    _item_row = ResponsiveRow(alignment="center")

    _container_input = Container(
        alignment=alignment.center,

        bgcolor="white",
        padding=2,
        border_radius=10,
        col={"sm": 10, "md": 10, "lg": 6, "xl": 5},
        content=Row([
            url_tiktok_textField,
            # on_button,
            url_paste,
            url_delete,
            # if url_tiktok_textField !="":
            #     url_delete.disabled=True
            # else:
            #     url_paste.disabled=True

        ], alignment="spaceBetween"),
        on_click=on_button,
    )

    #
    _container_download = Container(
        # alignment=alignment.center,
        bgcolor="white",
        padding=2,
        border_radius=10,
        col={"sm": 10, "md": 10, "lg": 1.2, "xl": 1},
        content=url_download
    )

    _container_item = Container(
        alignment=alignment.center,
        padding=20,
        content=_item_row
    )
    #
    # for item in _item:
    #     _container_input = Container(
    #         # alignment=alignment.center,
    #         bgcolor="white",
    #         padding=2,
    #         border_radius=10,
    #         col={"sm": 10, "md": 8, "lg": 5, "xl": 5},
    #         content=Container(
    #             content= item,
    #         )
    #
    #     )
    #     _item_row.controls.append(_container_input)

    _item_row.controls.append(_container_input)
    _item_row.controls.append(_container_download)

    # if url_tiktok_textField.value == "":
    #     url_button.controls.append(url_paste)

    # url_button.controls.append(url_delete)

    # url_button.controls.append(url_delete)
    #
    # if url_tiktok_textField.value != "":
    #     url_button.controls.append(url_delete)
    # url_button.controls.append(url_paste.visible(False))

    # url_button.controls.append(url_download)

    # url_container = Container(
    #     margin=20,
    #     width=790,
    #     height=55,
    #     padding=2,
    #     bgcolor="white",
    #     border_radius=10,
    #     # content=url_tiktok_textField,
    #    content=url_button
    # )

    # main column
    _main_col = Column(horizontal_alignment="center", scroll="auto")
    _main_col.controls.append(_nav)
    _main_col.controls.append(Container(padding=padding.only(top=75)))
    _main_col.controls.append(_title)
    # _main_col.controls.append(url_container)
    _main_col.controls.append(_container_item)

    # bg container
    _backround = Container(
        height=page.height,
        expand=True,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#0f172a"],
        ),
        content=_main_col,
    )

    page.add(_backround)
    page_resize(None)


if __name__ == "__main__":
    flet.app(target=main, view=flet.WEB_BROWSER)
