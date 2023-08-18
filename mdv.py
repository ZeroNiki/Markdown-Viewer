#!/usr/bin/python
import textual

from textual.app import App, ComposeResult
from textual.widgets import Footer, MarkdownViewer, Header
from argparse import ArgumentParser 

import os

filename = ArgumentParser(description="Read markdown files")
filename.add_argument("filename")

args = filename.parse_args()

with open(f"{os.getcwd()}/{args.filename}", "r") as file:
    lines = file.readlines()

    md = []
    for line in lines:
        md.append(line.replace("\n", ""))    

    PATH = '\n'.join(md) 
 
        
class MarkdownViewerApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"), 
        ("CTRL + C", "exit", "Exit"),            
    ]

    def compose(self) -> ComposeResult:
        #Yield Widgets
        yield Header(show_clock=True)
        yield Footer()
        yield MarkdownViewer(PATH, show_table_of_contents=True)
    

    def action_toggle_dark_mode(self):
        self.dark = not self.dark



if __name__ == "__main__":
    MarkdownViewerApp().run()

