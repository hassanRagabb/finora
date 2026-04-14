import json
from database import engine
from sqlalchemy import text

def seed_data():
    with open("D:/challengeAccepted/agentic/projects/FinoraLAST/smsm_github/db_snap.json") as f:
        data = json.load(f)
    
    with engine.connect() as conn:
        for row in data["companies"]["rows"]:
            conn.execute(text("""
                INSERT INTO companies (id, name, industry, currency, created_at)
                VALUES (:id, :name, :industry, :currency, :created_at)
                ON CONFLICT (id) DO NOTHING
            """), {
                "id": row[0], "name": row[1], "industry": row[2],
                "currency": row[3], "created_at": row[4]
            })
        
        for row in data["revenue"]["rows"]:
            conn.execute(text("""
                INSERT INTO revenue (id, company_id, amount, source, month, created_at)
                VALUES (:id, :company_id, :amount, :source, :month, :created_at)
                ON CONFLICT (id) DO NOTHING
            """), {
                "id": row[0], "company_id": row[1], "amount": row[2],
                "source": row[3], "month": row[4], "created_at": row[5]
            })
        
        for row in data["expenses"]["rows"]:
            conn.execute(text("""
                INSERT INTO expenses (id, company_id, amount, category, description, month, created_at)
                VALUES (:id, :company_id, :amount, :category, :description, :month, :created_at)
                ON CONFLICT (id) DO NOTHING
            """), {
                "id": row[0], "company_id": row[1], "amount": row[2],
                "category": row[3], "description": row[4], "month": row[5], "created_at": row[6]
            })
        
        conn.commit()
    
    print("Sample data inserted successfully!")

if __name__ == "__main__":
    seed_data()
