# Wiki Search Engine

A custom wikipedia search engine built with Python and MongoDB.

## Getting Started

These instructions will help you install and run the search engine on your local machine.

### Prerequisites

The things you need before installing the software.

* Python 3.8+
* MongoDB

### Installation

A step by step guide that will tell you how to get the development environment up and running.

1. Create and activate a python virtual environment using the following command:
```
python3 -m venv env
```

In Windows:
```
env\Scripts\activate
```

In UNIX/Linux:
```
source env/bin/activate
```

2. Install the python libraries from `requirements.txt`
```
pip install -r requirements.txt
```

After installing all the required libraries, we install the following NLTK pakages: corpora, punkt
```
import nltk
nltk.download()
```

3. Install the latest MongoDB stable release from https://www.mongodb.com/


## Usage

To run, just use

```
python CrawlerRunner.py
```

![demo](https://github.com/kpp16/SearchEngine/blob/main/ScreenShot.PNG)
