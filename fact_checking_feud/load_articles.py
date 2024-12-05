import os
import django
import csv
from core.models import Article

#for pushing articles to the table
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fact_checking_feud.settings')  # Ensure this matches your project name
django.setup()

def load_articles_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Article.objects.create(
                publisher=row['publisher'],
                title=row['headline'],
                content=row['body']
            )
    print("Articles loaded successfully!")

if __name__ == "__main__":
    load_articles_from_csv('cleaned_articles.csv')
