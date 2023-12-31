# GTACC: Grade Trend Analysis and Counseling Cue

## Project Overview

GTACC is a predictive machine learning tool designed to analyze high school students' grade trends over time. It identifies significant changes in academic performance, potentially flagging students who may benefit from counseling. This project embodies a real-world application of artificial intelligence to foster timely academic support.

## Features

- **Grade Trend Analysis**: Automated analysis of students' grade progression.
- **Performance Prediction**: Utilizes Gradient Boosting Regressors to forecast future academic performance.
- **Counseling Trigger**: Algorithmically determines when a student's performance warrants counseling intervention.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/GTACC.git
   ```
2. Navigate to the cloned directory:
   ```
   cd GTACC
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place the student grade data CSV file in the `data` directory.
2. Run the analysis script:
   ```
   python analysis_script.py
   ```
3. Review the output for engagement metrics and counseling flags.

## Data

Your data should be structured as follows:

- **Student ID**: Unique identifier for each student.
- **Academic Year**: The school year of record.
- **Grade**: Numerical grade received in the course.

```csv
StudentID,AcademicYear,Term,Subject,Grade
S001,2020-2021,Fall,Math,85
...
```

## Contributing

1. Fork the project (click on the "Fork" button at the top of the page).
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/dhruvvaz/GTACC](https://github.com/your-username/GTACC)

