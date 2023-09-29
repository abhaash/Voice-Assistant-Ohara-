import imp
from multiprocessing import connection


import sqlite3

def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection

def get_quetions_and_answers():
    