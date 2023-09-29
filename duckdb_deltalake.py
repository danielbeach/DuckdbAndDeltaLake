import duckdb as db
from deltalake import DeltaTable

def read_remote_delta_lake(path: str, key, secret):
    storage_options = {"AWS_ACCESS_KEY_ID": key, 
                       "AWS_SECRET_ACCESS_KEY": secret, 
                       "region": "us-east-1"}
    dt = DeltaTable(path, storage_options=storage_options)
    return dt.to_pyarrow_table()



def main():
    delta_path = "s3://confessions-of-a-data-guy/trip_data_delta"
    key=''
    secret=''
    dt = read_remote_delta_lake(delta_path, key, secret)
    con = db.connect()
    polars_results = con.execute("SELECT * FROM dt").pl()
    print(polars_results)


if __name__ == "__main__":
    main()