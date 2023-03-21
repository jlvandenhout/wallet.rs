from iota_wallet import IotaWallet
import time

# In this example we will destroy an alias

wallet = IotaWallet('./alice-database')

account = wallet.get_account('Alice')

# Sync account with the node
response = account.sync()
print(f'Balance before destroying:\n{response}')

wallet.set_stronghold_password("some_hopefully_secure_password")

# TODO: replace with your own values.
alias_id = "0x08429fe5864378ce70699fc2d22bb144cb86a3c4833d136e3b95c5dadfd6ba0cef0500000000"

# Send transaction.
account.destroy_alias(alias_id)

# Wait a few seconds for the transaction to get confirmed
time.sleep(7)

# Sync account with the node
response = account.sync()
print(f'Balance after destroying:\n{response}')
