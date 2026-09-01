# SIMPLE FILE MANAGEMENT PROJECT

from pathlib import Path
import os, time, random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sort():
    pass

def main():
    print(f"{"WELCOME TO PyFileSort":=^20}")
    filepath = input('Enter the filepath in which you would want to manage your files >>>: ')
    print(sort(filepath))