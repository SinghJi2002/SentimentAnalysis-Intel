# Intel Product Sentiment Analysis

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [Acknowledgements](#acknowledgements)

## Project Overview
The Intel Product Sentiment Analysis project aims to analyze customer sentiment towards Intel products using various machine learning and natural language processing techniques. This analysis helps in understanding customer opinions, improving product offerings, and enhancing customer satisfaction.

## Features
- Scraping customer reviews from Amazon.
- Preprocessing and cleaning of textual data.
- Sentiment analysis using machine learning models (e.g., LSTM, RoBERTa).
- Visualization of sentiment distribution.
- Comprehensive exploratory data analysis (EDA).

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SinghJi2002/intel-product-sentiment-analysis.git
    cd intel-product-sentiment-analysis
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Download necessary NLTK data:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    ```

## Usage
1. **Data Collection:**
    - Use the provided script to scrape Amazon reviews for Intel products.

2. **Preprocessing:**
    - Run the preprocessing script to clean and prepare the data for analysis.

3. **Sentiment Analysis:**
    - Train the sentiment analysis models using the training scripts provided. Select the best performing model.
    - Use the trained model to predict sentiments on intel data and further analyse them.

4. **Visualization:**
    - Generate visualizations to explore the sentiment distribution and other insights.

## Contributing
We welcome contributions from the community. Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.
