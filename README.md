# π Irrationality Visualization

This project visualizes the patterns created by the irrational number π (pi) using two rotating rods and a dynamically generated trace path.

## Overview

The animation is created with:
- Two rods, each rotating at different speeds.
- A trace path that dynamically follows the tip of the outer rod to form intricate patterns.
- Adjustable parameters, such as rotation speeds, rod lengths, and trace path thickness.

## How to Run

- Install Python 3.9 or later.
- Install Manim:

    ```bash
    pip install manim
    pip install numpy
    ```

- Download and install [FFmpeg](https://ffmpeg.org/download.html). Ensure the directory containing `ffmpeg.exe` is added to your **System Environment Variables**.
  
    #### Adding FFmpeg to System Environment Variables (Windows):
    1. Download FFmpeg and extract it to a folder (e.g., `C:\ffmpeg`).
    2. Press `Win + S`, type "Environment Variables," and select "Edit the system environment variables."
    3. In the System Properties window, click "Environment Variables."
    4. Under **System variables**, locate `Path`, select it, and click "Edit."
    5. Add the full path to the `bin` folder inside your FFmpeg directory (e.g., `C:\ffmpeg\bin`).
    6. Click "OK" to save changes and close all windows.

- Ensure `manim.exe` is added to your **User Environment Variables**:

    #### Adding Manim to User Environment Variables (Windows):
    1. Locate where `manim.exe` is installed (e.g., in your Python's `Scripts` directory).
    2. Open the Environment Variables editor as described above.
    3. Under **User variables**, locate `Path`, select it, and click "Edit."
    4. Add the full path to the directory containing `manim.exe` (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\Scripts`).
    5. Click "OK" to save and close all windows.

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pi-irrationality-visualization.git
    cd pi-irrationality-visualization
    ```

2. Run the visualization in the terminal:
    ```bash
    manim -pql main.py TwoRotatingRods
    ```

   - Use `-pql` (preview quality low) for a **faster render**.
   - Use `-pqh` (preview quality high) for a **slower render**, which will take more time but produce a higher-quality output.

**Note:** If you encounter errors, double-check that both FFmpeg and `manim.exe` paths are correctly added to the appropriate environment variables.

## Customization

You can modify the following parameters in `main.py`:

- `inner_rotation_speed`: Adjust the speed of the inner rod's rotation.
- `outer_rotation_speed`: Adjust the speed of the outer rod's rotation.
- `rod_length`: Change the length of both rods.
- `trace_thickness`: Set the thickness of the trace path.
