import pandas as pd

class DataImport:
    def import_csv(self, file_path):
        """Import data from a CSV file."""
        try:
            data = pd.read_csv(file_path)
            print("Data imported successfully.")
            return data
        except Exception as e:
            print(f"Error importing data: {e}")

    def import_excel(self, file_path):
        """Import data from an Excel file."""
        try:
            data = pd.read_excel(file_path)
            print("Data imported successfully.")
            return data
        except Exception as e:
            print(f"Error importing data: {e}")

if __name__ == "__main__":
    # Example usage
    data_importer = DataImport()
    data = data_importer.import_csv("data.csv")  # Change to your CSV file path
