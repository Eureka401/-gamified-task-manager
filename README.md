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

Our application is built following a **Modular MVU Architecture with a Plugin System**:

- **Model:**  
  *Strictly* manages the application's state and data (tasks, users, modules) along with the business logic. The Model is treated as immutable—each update produces a new version of the state.

- **View:**  
  Renders the user interface based solely on the current state (Model). The View is a pure function that translates the state into a visual representation. Depending on the implementation, this could be a web interface (HTML/CSS/JS via Flask) or a desktop UI (using PyQt).

- **Update:**  
  Acts as the central coordinator that handles user inputs (or messages). It receives a message along with the current state, computes the next state (Model) based on the logic, and returns this new state. The Update function is responsible for routing user interactions to the appropriate logic, triggering state transitions, and potentially invoking side effects (such as API calls or interactions with plugins).

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
- `tzdata` installed on your system (`pip -install tzdata`)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Eureka401/-gamified-task-manager.git
   cd -gamified-task-manager

---

### Contributing
Please adhere to the following guidelines:

- Coding Style: Follow PEP8 guidelines.
- Principles: SOLID, DRY, KISS, and YAGNI principles.
- Branching: Use feature branches and submit pull requests with clear, descriptive commit messages.
- Issues: Create GitHub Issues for new features, enhancements, or bug reports.
- Commits: Follow conventional commits like `feat: <describe the feature>` or `fix: <describe the fix>`

It is also highly encouraged for contributors to be adept in the following:
- SQL
- *To add on later*

---

### Documentation
Documentation is generated using Sphinx from our codebase docstrings and is located in the docs/ folder. For further details, please refer to the auto-generated documentation or the project wiki.


