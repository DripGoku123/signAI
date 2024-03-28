import sqlite3
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import pickle
def insert_data(data):
    conn = sqlite3.connect("baza.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tabela (
    x TEXT,
    y TEXT,
    inde INTEGER
)""")
    cursor.execute("INSERT INTO tabela (x,y,inde) VALUES (?,?,?)",data)
    conn.commit()

def train():
    conn = sqlite3.connect('baza.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT x,y,inde FROM tabela ORDER BY inde ASC")
    rows = cursor.fetchall()
    conn.close()
    data,inde=[],[]
    for r in rows:
        g = eval(r[0])
        for rr in eval(r[1]):
            g.append(rr)
        data.append(g)
        inde.append(r[2])
    for d in data:
        for _ in range(800-len(d)):
            d.append(0)
            
    print(data)
    print()
    print(inde)
    model=XGBClassifier(eta=0.1,min_child_weight=2,colsample_bytree=0.9,reg_alpha=0.1,reg_lambda=0.8, max_depth=8, gamma=0)
    X_train, _, y_train, _ = train_test_split(data, inde, test_size=0.1)
    model.fit(X_train,y_train)
    with open("model.pkl","wb") as f:
        pickle.dump((model),f)
def predict(data):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model.predict(data)


