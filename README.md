# ML Algorithms From Scratch

This repository contains Python implementations of fundamental machine learning algorithms developed from scratch. The primary objective is to provide a clear understanding of the inner workings of these algorithms without relying on high-level libraries. Each algorithm is explained intuitively before diving into the code. These explanations provide a conceptual understanding of the algorithm's logic, helping to grasp the core ideas before looking at the implementation details.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Implemented Algorithms](#implemented-algorithms)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

## Introduction

Understanding machine learning algorithms at a granular level is crucial for grasping their mechanics and effectively applying them. This project offers straightforward implementations of various machine learning algorithms using Python and foundational libraries like NumPy.

## Project Structure

- **models**: Contains subfolders for different types of learning:
  - **Deep Learning**: Implementations of neural networks and related algorithms.
  - **Supervised Learning**: Algorithms like Linear Regression, Logistic Regression, Decision Trees, etc.
  - **Unsupervised Learning**: Algorithms like k-Means Clustering and Principal Component Analysis.
- **utils**: Contains utility functions and helper scripts used across different models.
- **README.md**: Documentation file for the project.
- **requirements.txt**: Lists the dependencies required to run the project.
- **setup.py**: A script for packaging and installing the project.
  
## Implemented Algorithms

The repository includes implementations of the following algorithms:

- **Supervised Learning:**
  - Linear Regression
  - Logistic Regression
  - Support Vector Machines
  - k-Nearest Neighbors (KNN)
  - Linear Discriminant Analysis (LDA)
  - Naive Bayes
  - Decision Trees
  - Random Forest
  - Adaboost
  - LightGBM
  - XGBoost
  - Perceptron
    
- **Unsupervised Learning:**
  - k-Means Clustering
  - Principal Component Analysis (PCA)
  - Long Short-Term Memory (LSTM)
  - Convolutional Neural Network (CNN)
  - Generative Adversarial Network (GAN)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ska-1/ML-algorithms-from-scratch.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd ML--Code-from-Scratch
   ```

3. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each algorithm is provided within an interactive Jupyter Notebook, making it easier to work with and understand. To run any notebook, use the following command:

```bash
jupyter notebook
```
This will open the Jupyter Notebook interface in your web browser. Navigate to the desired notebook and run the cells sequentially to see the implementation and results.
For a comprehensive understanding, refer to the docstrings and comments within each implementation.

## Contributing

Contributions to enhance this project are welcome. To contribute:

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature-branch-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -m 'Add new feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature-branch-name
   ```
5. **Open a Pull Request.**

Please ensure that your contributions align with the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## References

For further reading and understanding, consider the following resources:

- [Machine Learning From Scratch by Erik Lindernoren](https://github.com/eriklindernoren/ML-From-Scratch)
- [Dive into Deep Learning](https://d2l.ai/d2l-en.pdf)

---
