# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies first for better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Command to run the tests
CMD ["pytest", "--alluredir=allure-results", "--headless"]
