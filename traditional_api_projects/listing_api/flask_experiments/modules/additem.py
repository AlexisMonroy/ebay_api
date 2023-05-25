import os
import sqlite3
import requests
from flask import Flask, render_template, redirect, request
import datetime 
import xml.etree.ElementTree as ET
import sys

product_list = [(1,), (2,), (3,)]