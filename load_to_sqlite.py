import sqlite3
import pandas as pd
from pathlib import Path

# Proje klasörü
project_path = Path.home() / "Desktop" / "toy_store"
raw_path = project_path / "data" / "raw"
db_path = project_path / "data" / "toy_store.db"

# CSV dosyaları ve tablo adları
files = {
    "website_sessions": "website_sessions.csv",
    "website_pageviews": "website_pageviews.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "order_item_refunds": "order_item_refunds.csv",
    "products": "products.csv"
}

# Veritabanına bağlan
conn = sqlite3.connect(db_path)

# CSV'leri yükle
for table_name, file_name in files.items():
    file_path = raw_path / file_name
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"{table_name} yüklendi. Satır sayısı: {len(df)}")

conn.close()
print("Tüm tablolar başarıyla SQLite veritabanına aktarıldı.")