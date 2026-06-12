import os

os.system("python data_ingestion.py")
os.system("python data_cleaning.py")
os.system("python database_setup.py")

print("Pipeline Completed")