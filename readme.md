# Apontamento Application

## Overview

The Apontamento Application is a desktop application designed for tracking production data, including defects and scrap types, in a manufacturing environment. It allows users to input various production metrics and view the last 10 registrations for easy monitoring and analysis.

## Technology Stack

- **Python**: The primary programming language used for developing the application.
- **PyQt5**: A set of Python bindings for Qt libraries, used for creating the graphical user interface (GUI).
- **SQLite**: A lightweight database engine used for storing production data locally.
- **datetime**: A built-in Python module for handling date and time operations.

## Features

- **Data Input**: Users can input various production metrics, including:
  - Date of the production entry
  - Shift (Turno)
  - Process (Processo)
  - Machine (Máquina)
  - Reference (Referência)
  - Quantity Produced (Quantidade Produzida)
  - Refugos (Scrap)
  - Defects (Defeitos) with associated types

- **Data Storage**: All input data is stored in a local SQLite database, allowing for persistent data management.

- **View Last Registrations**: Users can view the last 10 registrations in a dedicated window, providing quick access to recent production data.

- **Input Validation**: The application includes input validation to ensure that all required fields are filled out correctly before submission.

- **Clear Form**: Users can clear the input form after submitting data, making it easy to enter new records.

## Possible Further Improvements

- **User  Authentication**: Implement user authentication to restrict access to the application and maintain data integrity.

- **Data Visualization**: Add charts and graphs to visualize production metrics over time, helping users identify trends and patterns.

- **Export Functionality**: Implement functionality to export data to CSV or Excel formats for reporting and analysis.

- **Enhanced Error Handling**: Improve error handling to provide more informative messages and prevent application crashes.

- **Unit Testing**: Add unit tests to ensure the reliability and stability of the application.

- **Multi-language Support**: Implement multi-language support to cater to a broader audience.

- **Deployment**: Create an installer for easy deployment on different operating systems.

## Installation

To run the application, ensure you have Python and the required libraries installed. You can install the necessary packages using pip:

```bash
pip install PyQt5
git clone https://github.com/yourusername/apontamento.git
cd apontamento
python gui.py
´´´