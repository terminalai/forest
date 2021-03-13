from ._importable import LazyImport, _import_statements


### Standard Library
from .stdlib import *


### File I/O
from .fileio import *


### STEM
from .stem import *


### Array
from .array import *


### String
from .string import *


### Functions
from .func import *


### Temporal
from .temporal import *


### Google
from .ggl import *


smtplib = LazyImport("import smtplib", "LIBRARY smtplib — SMTP protocol client, derived from 'import smtplib', part of The Python Standard Library")






## Audio
playsound = LazyImport('from playsound import playsound', "FUNCTION playsound.playsound('/path.to/a/sound/file/you/want/to/play.mp3 | URL', block=True) — Function to playing sound file with filetype WAVE and MP3, derived from 'from playsound import playsound', from https://github.com/TaylorSMarks/playsound")
sa = LazyImport('import simpleaudio as sa', "PACKAGE sa derived from simpleaudio — A cross-platform dependency-free asynchronous simple audio playback Python extension, derived from 'import simpleaudio as sa', from https://github.com/hamiltron/py-simple-audio, Documentation: https://simpleaudio.readthedocs.io/en/latest/")
simpleaudio = LazyImport('import simpleaudio', "PACKAGE simpleaudio — A cross-platform dependency-free asynchronous simple audio playback Python extension, derived from 'import simpleaudio', from https://github.com/hamiltron/py-simple-audio, Documentation: https://simpleaudio.readthedocs.io/en/latest/")
fc = LazyImport("from simpleaudio import functionchecks as fc", "SUBPACKAGE fc derived from simpleaudio.functionchecks — Quick Function Check for simpleaudio package, derived from 'import simpleaudio.functionchecks as fc', from https://github.com/hamiltron/py-simple-audio, Documentation: https://simpleaudio.readthedocs.io/en/latest/")
winsound = LazyImport('import winsound', "LIBRARY winsound — Sound-playing interface for Windows, derived from 'import winsound', from The Python Standard Library")
#beep = LazyImport('from winsound import Beep as beep')
sd = LazyImport('import sounddevice as sd', "PACKAGE sd derived from sounddevice — Play and Record Sound with Python, derived from 'import sounddevice as sd', from https://github.com/spatialaudio/python-sounddevice, Documentation: https://python-sounddevice.readthedocs.io/en/0.3.15/")
sounddevice = LazyImport('import sounddevice', "PACKAGE sounddevice — Play and Record Sound with Python, derived from 'import sounddevice', from https://github.com/spatialaudio/python-sounddevice, Documentation: https://python-sounddevice.readthedocs.io/en/0.3.15/")
sf = LazyImport('import soundfile as sf', "PACKAGE sf derived from soundfile — SoundFile is an audio library based on libsndfile, CFFI and NumPy, derived from 'import soundfile as sf', from https://github.com/bastibe/SoundFile")
soundfile = LazyImport('import soundfile', "PACKAGE soundfile — SoundFile is an audio library based on libsndfile, CFFI and NumPy, derived from 'import soundfile', from https://github.com/bastibe/SoundFile")
AudioSegment = LazyImport('from pydub import AudioSegment', "CLASS pydub.AudioSegment — Classes that contain Audio Segments, derived from 'from pydub import AudioSegment', from https://github.com/jiaaro/pydub, Documentation: https://github.com/jiaaro/pydub/blob/master/API.markdown")
pydub = LazyImport('import pydub', "PACKAGE pydub — Manipulate audio with a simple and easy high level interface, derived from 'import pydub', from https://github.com/jiaaro/pydub, Documentation: https://github.com/jiaaro/pydub/blob/master/API.markdown")
playwav = LazyImport('from pydub.playback import play as playwav', "FUNCTION playwav derived from pydub.playback.play — Play WAV-based AudioSegment Objects, derived from 'from pydub.playback import play as playwav', from https://github.com/jiaaro/pydub, Documentation: https://github.com/jiaaro/pydub#playback")
wave = LazyImport('import wave', "LIBRARY wave — Read and write WAV files, derived from 'import wave', from The Python Standard Library")
pyaudio = LazyImport('import pyaudio', "PACKAGE pyaudio — Python Bindings for PortAudio, derived from 'import pyaudio', from https://github.com/jleb/pyaudio, Documentation: http://people.csail.mit.edu/hubert/pyaudio/docs/")



### Auto-complete
jedi = LazyImport("import jedi", "PACKAGE jedi — Awesome autocompletion, static analysis and refactoring library for Python, derived from 'import jedi', from https://github.com/davidhalter/jedi, Documentation: https://jedi.readthedocs.io/en/latest/")
setup_readline = LazyImport("from jedi.utils import setup_readline", "FUNCTION setup_readline — Function that sets up readline to use Jedi in a Python interactive shell, derived from 'from jedi.utils import setup_readline', from https://github.com/davidhalter/jedi, Documentation: https://jedi.readthedocs.io/en/latest/docs/usage.html")
readline = LazyImport("import readline", "LIBRARY readline — GNU readline interface, derived from 'import readline', from The Python Standard Library")
rlcompleter = LazyImport("import rlcompleter", "LIBRARY rlcompleter — Completion function for GNU readline, derived from 'import rlcompleter', from The Python Standard Library")



### GUI
from .gui import *



### Web Stuff
urllib2 = LazyImport("import urllib.request as urllib2", "LIBRARY urllib2 derived from urllib.request — Extensive library for opening URLs, derived from 'import urllib.request as urllib2', from The Python Standard Library")
urllib = LazyImport("import urllib", "LIBRARY urllib — URL handling modules, derived from 'import urllib', from The Python Standard Library")
urlopen = LazyImport("from urllib.request import urlopen", "FUNCTION urllib.request.urlopen(url...) — Opens the URL url which can be either a string or a Request object, derived from 'from urllib.request import urlopen', from The Python Standard Library")
requests = LazyImport("import requests", "PACKAGE requests — A simple, yet elegant HTTP library, derived from 'import requests', from https://github.com/psf/requests, Documentation: https://requests.readthedocs.io/en/master/")
BeautifulSoup = LazyImport("from bs4 import BeautifulSoup", "CLASS bs4.BeautifulSoup — HTML/XML Formatter on Python, derived from 'from bs4 import BeautifulSoup', from https://www.crummy.com/software/BeautifulSoup/, Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
scrapy = LazyImport("import scrapy", "PACKAGE scrapy — A fast high-level web crawling & scraping framework for Python, derived from 'import scrapy', from https://github.com/scrapy/scrapy, Documentation: https://docs.scrapy.org/en/latest/index.html")

newspaper = LazyImport("import newspaper", "PACKAGE newspaper — News, full-text, and article metadata extraction in Python 3, derived from 'import newspaper', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/")
Article = LazyImport("from newspaper import Article", "CLASS newspaper.Article — Article scraping and curation, derived from 'from newspaper import Article', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#news-articles")
fulltext = LazyImport("fromn newspaper import fulltext", "FUNCTION newspaper.fulltext — Extract full text from an article, derived from 'from newspaper import fulltext', from https://github.com/codelucas/newspaper, Documentation: https://newspaper.readthedocs.io/en/latest/")
wikipedia = LazyImport("import wikipedia", "PACKAGE wikipedia — A Pythonic wrapper for the Wikipedia API, derived from 'import wikipedia', from https://github.com/goldsmith/Wikipedia, Documentation: https://wikipedia.readthedocs.io/en/latest/")


webbrowser = LazyImport("import webbrowser", "LIBRARY webbrowser — Convenient Web-browser controller, derived from 'import webbrowser', from The Python Standard Library")
wb = LazyImport("import webbrowser as wb", "LIBRARY wb derived from webbrowser — Convenient Web-browser controller, derived from 'import webbrowser as wb', from The Python Standard Library")
openweb = LazyImport("from webbrowser import open as openweb", "FUNCTION openweb derived from webbrowser.open — Display url using the new default browser, derived from 'from webbrowser import open as openweb', from The Python Standard Library")

fastapi = LazyImport("import fastapi")
FastAPI = LazyImport("from fastapi import FastAPI")
pydantic = LazyImport("import pydantic")
tornado = LazyImport("import tornado")
sanic = LazyImport("import sanic")
Sanic = LazyImport("from sanic import Sanic")




### Data Wrangling

dask = LazyImport("import dask", "PACKAGE dask — Parallel computing with task scheduling, derived from 'import dask', from https://github.com/dask/dask, Documentation: https://dask.org/")
dd = LazyImport("from dask import dataframe as dd", "SUBPACKAGE dd derived from dask.dataframe — Dataframes implementing the Pandas API, derived from 'from dask import dataframe as dd', from https://github.com/dask/dask, Documentation: https://dask.org/")
da = LazyImport("from dask import array as da", "SUBPACKAGE da derived from dask.array — Arrays implementing the Numpy API, derived from 'from dask import array as da', from https://github.com/dask/dask, Documentation: https://dask.org/")

pyspark = LazyImport("import pyspark", "PACKAGE pyspark — Python API for Apache Spark, derived from 'import pyspark', from https://github.com/apache/spark/tree/master/python, Documentation: https://spark.apache.org/docs/latest/api/python/pyspark.html")
spark = LazyImport("import pyspark as spark", "PACKAGE spark derived from pyspark — Python API for Apache Spark, derived from 'import pyspark as spark', from https://github.com/apache/spark/tree/master/python, Documentation: https://spark.apache.org/docs/latest/api/python/pyspark.html")
SparkContext = LazyImport("from pyspark import SparkContext", "CLASS pyspark.SparkContext — Main entry point for Spark functionality, derived from 'from pyspark import SparkContext', from https://github.com/apache/spark/tree/master/python, Documentation: https://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext")


### Data Visualization and Plotting
matplotlib = LazyImport("import matplotlib", "PACKAGE matplotlib — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/contents.html")
mpl = LazyImport("import matplotlib as mpl", "PACKAGE mpl derived from matplotlib — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib as mpl', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/contents.html")
plt = LazyImport("import matplotlib.pyplot as plt", "SUBPACKAGE plt derived from matplotlib.pyplot — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'import matplotlib.pyplot as plt', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/api/index.html#the-pyplot-api")
pyplot = LazyImport("from matplotlib import pyplot", "SUBPACKAGE matplotlib.pyplot — A comprehensive library for creating static, animated, and interactive visualizations in Python, derived from 'from matplotlib import pyplot', from https://github.com/matplotlib/matplotlib, Documentation: https://matplotlib.org/api/index.html#the-pyplot-api")
pylab = LazyImport("import pylab", "PACKAGE pylab - A procedural interface to the Matplotlib object-oriented plotting library, derived from 'import pylab', from https://github.com/matplotlib/matplotlib, Documentation: https://scipy.github.io/old-wiki/pages/PyLab")
pl = LazyImport("import pylab as pl", "PACKAGE pylab - A procedural interface to the Matplotlib object-oriented plotting library, derived from 'import pylab as pl', from https://github.com/matplotlib/matplotlib, Documentation: https://scipy.github.io/old-wiki/pages/PyLab")


matkinter = LazyImport("import matkinter", "MODULE matkinter — A library for tkinter data visualizations, derived from 'import matkinter', self-created")

seaborn = LazyImport("import seaborn", "PACKAGE seaborn — A Python visualization library based on matplotlib, derived from 'import seaborn', from https://github.com/mwaskom/seaborn, Documentation: https://seaborn.pydata.org/")
sns = LazyImport("import seaborn as sns", "PACKAGE sns derived from seaborn — A Python visualization library based on matplotlib, derived from 'import seaborn as sns', from https://github.com/mwaskom/seaborn, Documentation: https://seaborn.pydata.org/")
eli5 = LazyImport("import eli5", "PACKAGE eli5 — A library for debugging/inspecting machine learning classifiers and explaining their predictions, derived from 'import eli5', from https://github.com/TeamHG-Memex/eli5/, Documentation: http://eli5.readthedocs.io/")

plotly = LazyImport("import plotly", "PACKAGE plotly — The interactive open-source browser-based graphing library for Python (includes Plotly Express), derived from 'import plotly', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
py = LazyImport("import plotly as py", "PACKAGE py derived from plotly — The interactive open-source browser-based graphing library for Python (includes Plotly Express), derived from 'import plotly as py', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
go = LazyImport("import plotly.graph_objs as go", "SUBPACKAGE go derived from plotly.graph_objs — Graph Objects, derived from 'import plotly.graph_objs as go', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
px = LazyImport("import plotly.express as px", "SUBPACKAGE px derived from plotly.express — Plotly Express, derived from 'import plotly.express as px', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
pio = LazyImport("import plotly.io as pio", "SUBPACKAGE pio derived from plotly.io — File IO for Plotly, derived from 'import plotly.io as pio', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
py1 = LazyImport("import plotly.plotly as py1", "SUBPACKAGE py1 derived from plotly.plotly — Plotly inbuilt subpackage, derived from 'import plotly.plotly as py1', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")
plottools = LazyImport("from plotly import tools as plottools", "SUBPACKAGE plottools derived from plotly.tools — Tools for plotly, derived from 'import plotly.tools as plottools', from https://github.com/plotly/plotly.py, Documentation: https://plotly.com/python/")

dash = LazyImport("import dash", "PACKAGE dash — A Python framework for building analytical web applications, derived from 'import dash', from https://github.com/plotly/dash, Documentation: http://dash-docs.herokuapp.com/")
dhc = LazyImport("import dash_html_components as dhc", "SUBPACKAGE dhc derived from dash.dash_html_components — A Python framework for composing a HTML layout using Python structures, derived from 'import dash.dash_html_components as dhc', from https://github.com/plotly/dash, Documentation: http://dash-docs.herokuapp.com/dash-html-components")
dcc = LazyImport("import dash_core_components as dcc", "SUBPACKAGE dcc derived from dash.dash_core_components — A core set of components, derived from 'import dash.dash_core_components as dcc', from https://github.com/plotly/dash, Documentation: http://dash-docs.herokuapp.com/dash-core-components")
dbc = LazyImport("import dash_bootstrap_components as dbc", "SUBPACKAGE dbc derived from dash.dash_bootstrap_components_components — A Python framework for composing a HTML layout using Python structures, derived from 'import dash.dash_bootstrap_components as dbc', from https://github.com/plotly/dash, Documentation: https://dash-bootstrap-components.opensource.faculty.ai/")

bokeh = LazyImport("import bokeh", "PACKAGE bokeh — Interactive Data Visualization in the browser, from Python, derived from 'import bokeh', from https://github.com/bokeh/bokeh, Documentation: https://docs.bokeh.org/en/latest/")

altair = LazyImport("import altair", "PACKAGE altair — Declarative statistical visualization library for Python, derived from 'import altair', from https://github.com/altair-viz/altair, Documentation: https://altair-viz.github.io/")
alt = LazyImport("import altair as alt", "PACKAGE alt derived from altair — Declarative statistical visualization library for Python, derived from 'import altair as alt', from https://github.com/altair-viz/altair, Documentation: https://altair-viz.github.io/")

pydot = LazyImport("import pydot", "PACKAGE pydot — Python interface to Graphviz's Dot language, derived from 'import pydot', from https://github.com/pydot/pydot")
pydot_ng = LazyImport("import pydot_ng", "PACKAGE pydot_ng — Python interface to Graphviz's Dot language, derived from 'import pydot_ng', from https://github.com/pydot/pydot-ng")

cf = LazyImport("import cufflinks as cf", "PACKAGE cf derived from cufflinks — Productivity Tools for Plotly + Pandas, derived from 'import cufflinks as cf', from https://github.com/santosjorge/cufflinks")
cufflinks = LazyImport("import cufflinks", "PACKAGE cufflinks — Productivity Tools for Plotly + Pandas, derived from 'import cufflinks', from https://github.com/santosjorge/cufflinks")


### Machine Learning
sklearn = LazyImport("import sklearn", "PACKAGE sklearn — Machine learning in Python, derived from 'import sklearn', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
OneHotEncoder = LazyImport("from sklearn.preprocessing import OneHotEncoder", "CLASS sklearn.preprocessing.OneHotEncoder — Encode categorical features as a one-hot numeric array, derived from 'from sklearn.preprocessing import OneHotEncoder', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
# , "CLASS sklearn. — , derived from 'from sklearn. import ', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
train_test_split = LazyImport("from sklearn.model_selection import train_test_split" , "FUNCTION sklearn.model_selection.train_test_split — Split arrays or matrices into random train and test subsets, derived from 'from sklearn.model_selection import train_test_split', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
cross_val_score = LazyImport("from sklearn.model_selection import cross_val_score" , "FUNCTION sklearn.model_selection.cross_val_score — Evaluate a score by cross validation, derived from 'from sklearn.model_selection import cross_val_score', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
StratifiedKFold = LazyImport("from sklearn.model_selection import StratifiedKFold" , "CLASS sklearn.model_selection.StratifiedKFold — Stratified K-Folds cross-validator, derived from 'from sklearn.model_selection import StratifiedKFold', from https://github.com/scikit-learn/scikit-learn, Documentation: https://scikit-learn.org/stable/modules/classes.html")
LogisticRegression = LazyImport("from sklearn.linear_model import LogisticRegression")
DecisionTreeClassifier = LazyImport("from sklearn.tree import DecisionTreeClassifier")
KNeighborsClassifier = LazyImport("from sklearn.neighbours import KNeighborsClassifier")
LinearDiscriminantAnalysis = LazyImport("from sklearn.discriminant_analysis import LinearDiscriminantAnalysis")
GaussianNB = LazyImport("from sklearn.naive_bayes import GaussianNB")
classification_report = LazyImport("from sklearn.metrics import classification_report")
confusion_matrix = LazyImport("from sklearn.metrics import confusion_matrix")
accuracy_score = LazyImport("from sklearn.metrics import accuracy_score")
make_scorer = LazyImport("from sklearn.metrics import make_scorer")
TSNE = LazyImport("from sklearn.manifold import TSNE")
svm = LazyImport("from sklearn import svm")
SVC = LazyImport("from sklearn.svm import SVC")
make_pipeline = LazyImport("from sklearn.pipeline import make_pipeline")
GradientBoostingClassifier = LazyImport("from sklearn.ensemble import GradientBoostingClassifier")
GradientBoostingRegressor = LazyImport("from sklearn.ensemble import GradientBoostingRegressor")
RandomForestClassifier = LazyImport("from sklearn.ensemble import RandomForestClassifier")
RandomForestRegressor = LazyImport("from sklearn.ensemble import RandomForestRegressor")
TfidfVectorizer = LazyImport("from sklearn.feature_extraction.text import TfidfVectorizer")
datasets = LazyImport("from sklearn import datasets")
load_iris = LazyImport("from sklearn.datasets import load_iris")
Iris = LazyImport("from sklearn.datasets import load_iris as Iris")
load_diabetes = LazyImport("from sklearn.datasets import load_diabetes")
Diabetes = LazyImport("from sklearn.datasets import load_diabetes as Diabetes")
load_digits = LazyImport("from sklearn.datasets import load_digits")
Digits = LazyImport("from sklearn.datasets import load_digits as Digits")
load_boston = LazyImport("from sklearn.datasets import load_boston")
Boston = LazyImport("from sklearn.datasets import load_boston as Boston")
load_breast_cancer = LazyImport("from sklearn.datasets import load_breast_cancer")
BreastCancer = LazyImport("from sklearn.datasets import load_breast_cancer as BreastCancer")




make_biclusters = LazyImport("from sklearn.datasets import make_biclusters")
make_blobs = LazyImport("from sklearn.datasets import make_blobs")
make_checkerboard = LazyImport("from sklearn.datasets import make_checkerboard")
make_circles = LazyImport("from sklearn.datasets import make_circles")
make_classification = LazyImport("from sklearn.datasets import make_classification")
make_regression = LazyImport("from sklearn.datasets import make_regression")

#diabetes = load_diabetes()
#digits = load_digits()
#iris = load_iris()
#iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
#diabetes_df = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)


creme = LazyImport("import creme")
Pipeline = LazyImport("from creme.compose import Pipeline")
preprocessing = LazyImport("from creme import preprocessing")
StandardScaler = LazyImport("from creme.preprocessing import StandardScaler")
KMeans = LazyImport("from creme.cluster import KMeans")
BernoulliNB = LazyImport("from creme.naive_bayes import BernoulliNB")
ComplementNB = LazyImport("from creme.naive_bayes import ComplementNB")
MultinomialNB = LazyImport("from creme.naive_bayes import MultinomialNB")
Gaussian = LazyImport("from creme.proba import Gaussian")
Multinomial = LazyImport("from creme.proba import Multinomial")
Accuracy = LazyImport("from creme.metrics import Accuracy")
F1 = LazyImport("from creme.metrics import F1")
Precision = LazyImport("from creme.metrics import Precision")
MAE = LazyImport("from creme.metrics import MAE")
Recall = LazyImport("from creme.metrics import Recall")
OneVsRestClassifier = LazyImport("from creme.multiclass import OneVsRestClassifier")
OneVsAllClassifier = LazyImport("from creme.multiclass import OneVsRestClassifier as OneVsAllClassifier")
LinearRegression = LazyImport("from creme.linear_model import LinearRegression")
progressive_val_score = LazyImport("from creme.model_selection import progressive_val_score")
KNeighborsRegressor = LazyImport("from creme.neighbors import KNeighborsRegressor")
SGD = LazyImport("from creme.optim import SGD")
Stochastic = LazyImport("from creme.optim import SGD as Stochastic")
SoftmaxRegression = LazyImport("from creme.linear_model import SoftmaxRegression")

Airline = LazyImport("from creme.datasets import Airline")
Phishing = LazyImport("from creme.datasets import Phishing")
ChickWeights = LazyImport("from creme.datasets import ChickWeights")
Elec2 = LazyImport("from creme.datasets import Elec2")
MovieLens100K = LazyImport("from creme.datasets import MovieLens100K")
HTTP = LazyImport("from crem.datasets import HTTP")
Higgs = LazyImport("from creme.datasets import Higgs")
Bikes = LazyImport("from creme.datasets import Bikes")
MaliciousURL = LazyImport("from creme.datasets import MaliciousURL")
ImageSegments = LazyImport("from creme.datasets import ImageSegments")
SMSSpam = LazyImport("from creme.datasets import SMSSpam")
SMTP = LazyImport("from creme.datasets import SMTP")
Taxis = LazyImport("from creme.datasets import Taxis")
TREC07 = LazyImport("from creme.datasets import TREC07")
TrumpApproval = LazyImport("from creme.datasets import TrumpApproval")


torch = LazyImport("import torch")
tc = LazyImport("import tensor_comprehensions as tc")

# Gradient Boosting Decision Tree
xgb = LazyImport("import xgboost as xgb")
lgb = LazyImport("import lightgbm as lgb")

# Deep Learning
tf = LazyImport("import tensorflow as tf")
tensorflow = LazyImport("import tensorflow")
keras = LazyImport("import keras")
tfkeras = LazyImport("import tensorflow.keras as tfkeras")


### OCR
opencv = LazyImport("import cv2 as opencv", "PACKAGE opencv derived from cv2 — Open Source Computer Vision Library, derived from 'import cv2 as opencv', from https://github.com/opencv/opencv, Documentation: https://docs.opencv.org/master/")
cv2 = LazyImport("import cv2", "PACKAGE cv2 — Open Source Computer Vision Library, derived from 'import cv2', from https://github.com/opencv/opencv, Documentation: https://docs.opencv.org/master/")


# NLP
nltk = LazyImport("import nltk")
gensim = LazyImport("import gensim")
spacy = LazyImport("import spacy")


# ------ Sentiment Analysis --------
tweepy = LazyImport("import tweepy")
TextBlob = LazyImport("from textblob import TextBlob")


# Quantum
qiskit = LazyImport("import qiskit")
cirq = LazyImport("import cirq")
openfermion = LazyImport("openfermion")
pyscf = LazyImport("import pyscf")
larq = LazyImport("import larq")
pyquil = LazyImport("import pyquil")
pennylane = LazyImport("import pennylane")
qml = LazyImport("import pennylane as qml")
quantum_forest = LazyImport("import quantum_forest")
deepchem = LazyImport("import deepchem")
dc = LazyImport("import deepchem as dc")
projectq = LazyImport("import projectq")
strawberryfields = LazyImport("import strawberryfields")
sf = LazyImport("import strawberryfields as sf")
ops = LazyImport("from strawberryfields import ops")
qibo = LazyImport("import qibo")
QFT = LazyImport("from qibo.models import QFT")



### Music Theory
mingus = LazyImport("import mingus")



### Own Modules
pytools = LazyImport("import pytools")

#######################################
### Complementary, optional imports ###
#######################################
# Why is this needed? Some libraries patch existing libraries
# Please note: these imports are only executed if you already have the library installed
# If you want to deactivate specific complementary imports, do the following:
# - uncomment the lines which contain `.__on_import__` and the library you want to deactivate

pandas_profiling = LazyImport("import pandas_profiling")
pd.__on_import__(pandas_profiling)  # adds df.profile_report attribute to pd.DataFrame

eda = LazyImport("import edaviz as eda")
pd.__on_import__(eda)  # adds GUI to pd.DataFrame when IPython frontend can display it


##################################################
### dont make adjustments below this line ########
##################################################
def lazy_imports():
    return _import_statements(globals(), was_imported=False)


def active_imports():
    return _import_statements(globals(), was_imported=True)
