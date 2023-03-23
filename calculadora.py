{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPBCvZt39XreN70k6pfTKbA",
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
        "<a href=\"https://colab.research.google.com/github/Pariasjulian/Procesamiento_Digital_img/blob/main/calculadora.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#class calculadora:\n",
        "def __init__(self, n1, n2):\n",
        "        self.n1 = float(n1)\n",
        "        self.n2 = float(n2)\n",
        "\n",
        "def sumar(self, n1, n2):\n",
        "        suma = self.n1 + self.n2\n",
        "        print(\"el resultado de la suma es: \", suma)\n",
        "\n",
        "def restar(self, n1, n2):\n",
        "        resta = self.n1 - self.n2\n",
        "        print(\"el resultado de la resta es: \", resta)\n",
        "\n",
        "def multiplicar(self, n1, n2):\n",
        "        multiplicacion = self.n1 * self.n2\n",
        "        print(\"el resultado de la multiplicación es: \", multiplicacion)\n",
        "\n",
        "def dividir(self, n1, n2):\n",
        "        division = self.n1 / self.n2\n",
        "        print(\"el resultado de la división es: \", division)"
      ],
      "metadata": {
        "id": "re_a15zfIYmD"
      },
      "execution_count": 16,
      "outputs": []
    }
  ]
}