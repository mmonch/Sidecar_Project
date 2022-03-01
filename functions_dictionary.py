{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "functions_dictionary.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMiHXj6HnlHq4t/WQUzYirW",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mmonch/Sidecar_Project/blob/main/functions_dictionary.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import tqdm\n",
        "import unicodedata\n",
        "import re\n",
        "import contractions\n",
        "from fuzzywuzzy import fuzz\n",
        "from fuzzywuzzy import process\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "CzDQpXR0cSiz"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "gGQXJ0iFA1lb"
      },
      "outputs": [],
      "source": [
        "# preprocess and normalize Text\n",
        "\n",
        "# in case text not english\n",
        "def remove_accented_chars(text):\n",
        "  text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')\n",
        "  return text\n",
        "\n",
        "# preprocessing technical names, split strings\n",
        "def pre_process_technical_names(labels):\n",
        "  norm_docs = []\n",
        "  for string in labels:\n",
        "    string = string.replace(\"_\", \" \")\n",
        "    string = string.translate(string.maketrans(\"\\n\\t\\r\", \"   \"))\n",
        "    string = remove_accented_chars(string) \n",
        "    # and inset a space where a number follows a letter et vice versa\n",
        "    string = re.sub(r'(?<=\\d)(?=[^\\d\\s])|(?<=[^\\d\\s])(?=\\d)', ' ', string)\n",
        "    # insert space where an uppercase letter follows a lowercase letter\n",
        "    string = re.sub(r\"(?<![A-Z\\W])(?=[A-Z])\", \" \", string)\n",
        "    string = contractions.fix(string)\n",
        "    # where XXXX number to XXXX number replace - with to IN PROGRESS\n",
        "    string = string.replace(\"-\", \" to \")\n",
        "    # remove special characters or whitespaces\n",
        "    string = re.sub(r\"[^a-zA-Z0-9\\s]\", \"\", string, flags=re.I|re.A)\n",
        "    string = string.lower()\n",
        "    string = string.strip()\n",
        "    # split strings for this transformer model\n",
        "    string = string.split(\" \")\n",
        "    norm_docs.append(string)\n",
        "  return norm_docs\n",
        "  \n",
        "  # preprocessing business names, no split strings\n",
        "def pre_process_business_names(labels):\n",
        "  norm_docs = []\n",
        "  for string in labels:\n",
        "    string = string.replace(\"_\", \" \")\n",
        "    string = string.translate(string.maketrans(\"\\n\\t\\r\", \"   \"))\n",
        "    string = remove_accented_chars(string) \n",
        "    # and inset a space where a number follows a letter et vice versa\n",
        "    string = re.sub(r'(?<=\\d)(?=[^\\d\\s])|(?<=[^\\d\\s])(?=\\d)', ' ', string)\n",
        "    # insert space where an uppercase letter follows a lowercase letter\n",
        "    string = re.sub(r\"(?<![A-Z\\W])(?=[A-Z])\", \" \", string)\n",
        "    string = contractions.fix(string)\n",
        "    # where XXXX number to XXXX number replace - with to IN PROGRESS\n",
        "    string = string.replace(\"-\", \" to \")\n",
        "    # remove special characters or whitespaces\n",
        "    string = re.sub(r\"[^a-zA-Z0-9\\s]\", \"\", string, flags=re.I|re.A)\n",
        "    string = string.lower()\n",
        "    string = string.strip()\n",
        "    # no split for this transformer model\n",
        "    # string = string.split(\" \")\n",
        "    norm_docs.append(string)\n",
        "  return norm_docs"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Checks one string for a matching value in the dictionary, if no match is found, checks Levenshtein ratio.\n",
        "def Checkname(Name, dictionary):\n",
        "     key, wratio = process.extractOne(Name, dictionary.keys())\n",
        "     value = dictionary[key]\n",
        "     return  key, value, wratio"
      ],
      "metadata": {
        "id": "vvv-WR0EA-WP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Checks list of strings for matching value in the dictionary, if no match is found, checks Levenshtein ratio.\n",
        "match_list = []\n",
        "def Checknames(Names, dictionaries):\n",
        "    for names in Names:\n",
        "      matches = []\n",
        "      key, value, wratio = Checkname(names, dictionaries)\n",
        "      matches.append(names)\n",
        "      matches.append(key)\n",
        "      matches.append(value)\n",
        "      matches.append(wratio)\n",
        "      matches.append(fuzz.ratio(names, value))\n",
        "      matches.append(fuzz.partial_ratio(names, value))\n",
        "      matches.append(fuzz.token_sort_ratio(names, value))\n",
        "      match_list.append(matches)\n",
        "    return match_list"
      ],
      "metadata": {
        "id": "ZvS4j4EgBH1V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "is2ZLW08BJMI"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}