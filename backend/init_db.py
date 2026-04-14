from database import engine, Base
from sqlalchemy import text

def init_db():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS companies (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                industry VARCHAR(255),
                currency VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies(id),
                full_name VARCHAR(255),
                email VARCHAR(255),
                role VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS revenue (
                id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies(id),
                amount DECIMAL(15, 2),
                source VARCHAR(255),
                month DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS expenses (
                id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies(id),
                amount DECIMAL(15, 2),
                category VARCHAR(100),
                description TEXT,
                month DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS kpis (
                id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies(id),
                month DATE,
                revenue DECIMAL(15, 2),
                expenses DECIMAL(15, 2),
                net_profit DECIMAL(15, 2),
                profit_margin DECIMAL(5, 2),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS ai_insights (
                id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies(id),
                agent VARCHAR(100),
                insight_type VARCHAR(100),
                title VARCHAR(500),
                body TEXT,
                severity VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        conn.commit()
    
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()
