'''
The Template Design Pattern is a behavioral design pattern that defines the program skeleton of an algorithm in a method, 
called template method, which defers some steps to subclasses.
It lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure. 
This pattern is particularly useful when having a series of steps to execute, 
some of which are invariant (common across subclasses) while others are variable (specific to a subclass).
'''


from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Abstract class defining the template method and the skeleton of the algorithm."""
    
    def process_data(self):
        """Template method defining the skeleton of the algorithm."""
        self.load_data()
        self.validate_data()
        self.analyze_data()
        self.save_results()
    
    @abstractmethod
    def load_data(self):
        """Load data from a source. Implementation is specific to the source."""
        pass
    
    @abstractmethod
    def validate_data(self):
        """Validate the loaded data. Implementation varies with the data source."""
        pass
    
    def analyze_data(self):
        """Analyze the data. Assuming analysis is common across all data sources."""
        print("Analyzing data...")
    
    def save_results(self):
        """Save the analysis results. Assuming saving is common across all data sources."""
        print("Saving results...")


class CSVDataProcessor(DataProcessor):
    """Concrete class implementing the specific steps for CSV data processing."""
    
    def load_data(self):
        print("Loading data from CSV...")
    
    def validate_data(self):
        print("Validating CSV data...")


class APIDataProcessor(DataProcessor):
    """Concrete class implementing the specific steps for API data processing."""
    
    def load_data(self):
        print("Loading data from API...")
    
    def validate_data(self):
        print("Validating API data...")

# Example usage
csv_processor = CSVDataProcessor()
csv_processor.process_data()

api_processor = APIDataProcessor()
api_processor.process_data()