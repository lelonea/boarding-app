# Journey Sorting Application

This application sorts a set of unordered boarding cards for various transportation methods and generates a step-by-step journey guide from a starting point to the final destination.

## Features

- Sorts boarding cards from multiple transport methods (Train, Bus, Flight).
- Generates a detailed, ordered list of travel instructions.
- Handles additional information like seat assignments, gate numbers, and baggage details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or newer
- Git

### Installing

1. **Clone the repository**
   ```bash
   git clone git@github.com:lelonea/boarding-app.git
   ```
2. **Navigate to the project directory**
   ```bash
   cd boarding-app
   ```
3. **Checkout to the development branch**
   ```bash
   git checkout development
    ```


### Running tests
```bash
python3 -m unittest discover -s tests
```

## Usage

### Boarding Card Data Preparation

Create your boarding card data as dictionaries within a JSON file, ensuring each entry includes:
- `departure`: Start location.
- `destination`: End location.
- `transport_type`: "Train", "Bus", or "Flight".
- `transport_number`: E.g., "78A" (train) or "SK455" (flight).
- `seat`: Seat assignment, if any.
- `additional_info`: Dictionary for extra details like gate numbers.

### JSON Data File

Edit the provided `boarding_cards.json` in the project's root to reflect your journey data. This editable file streamlines the process of inputting and modifying journey details.

### Generate Journey Instructions

After customizing `boarding_cards.json`:

1. **Execute the script** to process the JSON data and output your journey instructions:
   ```python
   python run_from_json.py
   ```

This script reads your journey data, organizes the boarding cards, and displays a clear, ordered list of instructions for your travel.
