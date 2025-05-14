import os
import duckdb

tables = ['call_center',
		'catalog_page', 'catalog_returns',
		'catalog_sales',
		'customer', 'customer_address', 'customer_demographics',
		'date_dim', 'household_demographics', 'income_band', 'inventory', 'item', 'promotion', 'reason', 'ship_mode',
		'store', 'store_returns', 'store_sales',
		'time_dim', 'warehouse',
		'web_page', 'web_returns', 'web_sales', 'web_site'
		]

data_path = '/Users/Shared/dsb/data' # directory of data files
db_name = 'dsb' # database name

create_table = False # If create the tables

con = duckdb.connect("/Users/Shared/dsb/dsb.db")

# create tables
if create_table:
	sql_path = r'/Users/Shared/dsb/scripts/create_tables.sql'
	# TODO: Confirm
	with open(sql_path, 'r') as f:
		sql_script = f.read()
	con.sql(sql_script)

# insert tuples into tables
for table in tables:
	file_path = os.path.join(data_path, table + '.dat')
	con.execute('delete from ' + table + ';')
	con.read_csv(file_path)
	con.sql("copy " + table + " from '" + file_path + "' delimiter '|'")

con.close()
