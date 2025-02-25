# Gamified Task Manager

## Overview

Gamified Task Manager is a modular task management platform designed to transform everyday productivity into an engaging, interactive experience. The application integrates multiple pre-designed productivity frameworks—such as the Eisenhower Matrix, GTD, Pomodoro Technique, and Atomic Habits—allowing users to mix and match modules according to their preferences. Users can also extend the platform by creating their own modules (for now, this can only be done by modifying the source code).

Tasks in the system are versatile:
- **Global Tasks:** Visible across all modules.
- **Selected Tasks:** Displayed only in user-specified modules.
- **Local Tasks:** Restricted to the module where they were created.

---

## Key Features

- **Modular Productivity Frameworks:**  
  Utilize frameworks like Eisenhower Matrix, GTD, Pomodoro, and Atomic Habits in a plug-and-play fashion.

- **Custom Module Support:**  
  Users can create and integrate custom modules to suit their workflow (for now, by coding directly into the source).

- **Flexible Task Scoping:**  
  Define tasks as global, selected, or local, so they appear in all, some, or only the originating module.

- **Gamification (Planned):**  
  Future releases will integrate game-like mechanics to motivate productivity and task completion.

---

## Technology Stack

- **Primary Language:** Python
- **Web Framework:** To be decided
- **Desktop UI (Optional):** To be decided
- **Database:** To be decided
- **Documentation:** Sphinx (for auto-generating documentation from docstrings)

---

## Design & Architecture

Our application is built following a **Modular MVC Architecture with a Plugin System**:

- **Model:**  
  *Strictly* anages data (tasks, users, modules) and logic.

- **View:**  
  Renders the user interface. Depending on the chosen approach, this could be a web interface (HTML/CSS/JS via Flask) or a desktop UI (using PyQt).

- **Controller:**  
  Coordinates the interaction between models and views, handling user input and routing it appropriately.

- **Module/Plugin System:**  
  - A `BaseModule` abstract class will define the interface for all modules.
  - Each productivity module (e.g., Eisenhower Matrix, Pomodoro) will extend `BaseModule` and implement its own logic for task filtering and display.
  - The app will dynamically load modules from a dedicated `modules/` directory.

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Virtual environment tools (e.g., `venv`).
- Git for version control.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Eureka401/-gamified-task-manager.git
   cd -gamified-task-manager
