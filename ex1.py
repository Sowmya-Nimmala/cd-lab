{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOmMXx3LZojF+pMMLTpyI3L",
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
        "<a href=\"https://colab.research.google.com/github/Sowmya-Nimmala/cd-lab/blob/main/ex1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n3Hsc024pYXZ",
        "outputId": "54bcea44-2ecd-4a45-e282-6edbb417737b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Keywords:  ['int', 'return']\n",
            "Operators:  []\n",
            "Delimiters:  ['{', '}']\n",
            "Identifiers:  ['#include', '<stdio.h>', 'main()', '//', 'printf()', 'displays', 'the', 'string', 'inside', 'quotation', 'printf(\"Hello,', 'World!\");', '0;']\n",
            "Numbers:  []\n"
          ]
        }
      ],
      "source": [
        "keywords = {\"auto\",\"break\",\"case\",\"char\",\"const\",\"continue\",\"default\",\"do\",\n",
        "\"double\",\"else\",\"enum\",\"extern\",\"float\",\"for\",\"goto\",\n",
        "\"if\",\"int\",\"long\",\"register\",\"return\",\"short\",\"signed\",\n",
        "\"sizeof\",\"static\",\"struct\",\"switch\",\"typedef\",\"union\",\n",
        "\"unsigned\",\"void\",\"volatile\",\"while\",\"printf\",\"scanf\",\"%d\",\"include\",\"stdio.h\",\"main\"}\n",
        "\n",
        "operators = {\"+\",\"-\",\"*\",\"/\",\"<\",\">\",\"=\",\"<=\",\">=\",\"==\",\"!=\",\"++\",\"--\",\"%\"}\n",
        "\n",
        "delimiters = {'(',')','{','}','[',']','\"',\"'\",';','#',',',''}\n",
        "\n",
        "def detect_keywords(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word in keywords:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn list(set(arr))\n",
        "\n",
        "def detect_operators(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word in operators:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn list(set(arr))\n",
        "\n",
        "def detect_delimiters(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word in delimiters:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn list(set(arr))\n",
        "\n",
        "def detect_num(text):\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\ttry:\n",
        "\t\t\ta = int(word)\n",
        "\t\t\tarr.append(word)\n",
        "\t\texcept:\n",
        "\t\t\tpass\n",
        "\treturn list(set(arr))\n",
        "\"\"\"\n",
        "this is original function for detecting identifier\n",
        "def is_identifier(token):\n",
        "    if token[0] in numbers or token in keywords:\n",
        "        return False\n",
        "    else:\n",
        "        return identifier(token)\n",
        "\n",
        "def identifier(token):\n",
        "    if len(token)<2 and (token[0] in alphabets or token[0] in numbers or token[0] == \"_\"):\n",
        "        return True\n",
        "    elif token[0] in alphabets or token[0] in numbers or token[0] == \"_\":\n",
        "        return identifier(token[1:])\n",
        "    else:\n",
        "        return False\n",
        "\"\"\"\n",
        "def detect_identifiers(text):\n",
        "\tk = detect_keywords(text)\n",
        "\to = detect_operators(text)\n",
        "\td = detect_delimiters(text)\n",
        "\tn = detect_num(text)\n",
        "\tnot_ident = k + o + d + n\n",
        "\tarr = []\n",
        "\tfor word in text:\n",
        "\t\tif word not in not_ident:\n",
        "\t\t\tarr.append(word)\n",
        "\treturn arr\n",
        "\n",
        "with open('e1-example.txt') as t:\n",
        "\ttext = t.read().split()\n",
        "\n",
        "print(\"Keywords: \",detect_keywords(text))\n",
        "print(\"Operators: \",detect_operators(text))\n",
        "print(\"Delimiters: \",detect_delimiters(text))\n",
        "print(\"Identifiers: \",detect_identifiers(text))\n",
        "print(\"Numbers: \",detect_num(text))"
      ]
    }
  ]
}