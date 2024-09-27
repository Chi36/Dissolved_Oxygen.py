{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMyFkQIbzNh/eifEUAI8tqU",
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
        "<a href=\"https://colab.research.google.com/github/Chi36/Dissolved_Oxygen.py/blob/main/Dissolved_Oxygen_Calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Question 1: The DO Level App. **\n",
        "This app calculates dissolved oxygen levels using the oxygen transfer rate and consumption rates. Then plot the dissolved oxygen (DO) concentration over time"
      ],
      "metadata": {
        "id": "8X7gsn5wL8nB"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BBWTK-nzLonp"
      },
      "outputs": [],
      "source": [
        "# App code to a file named OxygenRate.py\n",
        "\n",
        "# Import Python libraries\n",
        "import streamlit as st\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "# Define Function to calculate the oxygen transfer rate\n",
        "def calculate_do(initial_do, volumetric_mass_transfer_coefficient, saturation_concentration_of_oxygen, time_hours):\n",
        "    do_values = [initial_do]\n",
        "\n",
        "    transfer_rate = volumetric_mass_transfer_coefficient * (saturation_concentration_of_oxygen - initial_do)\n",
        "    consumption_rate = (saturation_concentration_of_oxygen - initial_do) / time_hours\n",
        "\n",
        "    for _ in range(time_hours):\n",
        "        do_change = transfer_rate - consumption_rate\n",
        "        do_values.append(do_values[-1] + do_change)\n",
        "\n",
        "    return do_values, consumption_rate\n",
        "\n",
        "# Title for the app\n",
        "st.title(\"Oxygen Transfer Rate Calculator\")\n",
        "\n",
        "# Inputs for the Rate app\n",
        "initial_do = st.number_input(\"Initial Dissolved Oxygen (mg/L)\", min_value=0.0, max_value=20.0, value=8.0)\n",
        "volumetric_mass_transfer_coefficient = st.number_input(\"Volumetric Mass Transfer Coefficient\", min_value=0.0, value=0.1)\n",
        "saturation_concentration_of_oxygen = st.number_input(\"Saturation Concentration of Oxygen (mg/L)\", min_value=0.0, max_value=20.0, value=9.0)\n",
        "time_hours = st.number_input(\"Time (hours)\", min_value=1, max_value=100, value=10)\n",
        "\n",
        "# Calculate the Dissolved Oxygen (DO) over time and consumption rate\n",
        "if st.button(\"Calculate\"):\n",
        "    do_values, consumption_rate = calculate_do(initial_do, volumetric_mass_transfer_coefficient, saturation_concentration_of_oxygen, time_hours)\n",
        "\n",
        "    st.write(f\"Consumption Rate: {consumption_rate} mg/L per hour\")\n",
        "\n",
        "    # Plotting the results using matplotlib\n",
        "    plt.plot(range(time_hours + 1), do_values)\n",
        "    plt.xlabel(\"Time (hours)\")\n",
        "    plt.ylabel(\"Dissolved Oxygen (mg/L)\")\n",
        "    plt.title(\"Dissolved Oxygen Over Time\")\n",
        "    st.pyplot(plt)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "3UyeytFSM6H6"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}