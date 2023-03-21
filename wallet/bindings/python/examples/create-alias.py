from iota_wallet import IotaWallet

# In this example we will mint native tokens

wallet = IotaWallet('./alice-database')

account = wallet.get_account('Alice')

# Sync account with the node
response = account.sync()
print(f'Synced: {response}')

wallet.set_stronghold_password("some_hopefully_secure_password")

transaction = account.create_alias_output(None, None)

print(f'Sent transaction: {transaction}')
