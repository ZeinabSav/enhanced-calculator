import pandas as pd


def save_history(history):
    df = pd.DataFrame(history)
    df.to_csv("history.csv", index=False)


def load_history():
    try:
        df = pd.read_csv("history.csv")
        return df.values.tolist()
    except FileNotFoundError:
        return []
    except Exception:
        return []