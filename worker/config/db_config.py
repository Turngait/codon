import os

db_config = {
  'mysql_users': os.environ['SQLLINK_USERS'],
  'mysql_users_data': os.environ['SQLLINK_USERS_DATA'],
  'mysql_codon': os.environ['SQLLINK_CODON_HEALTH'],
}