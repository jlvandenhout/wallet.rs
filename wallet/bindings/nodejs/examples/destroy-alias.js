/**
 * This example will destroy an alias
 */
const getUnlockedManager = require('./account-manager');

async function run() {
    try {
        const manager = await getUnlockedManager();

        const account = await manager.getAccount('0');

        await account.sync();
        console.log('Balance before destroying:\n', await account.getBalance());

        // Replace with an existing alias ID in your account
        let aliasId =
            '0x08e6210d29881310db2afde095e594f6f006fcdbd06e7a83b74bd2bdf3b5190d0e0200000000';

        await account.destroyAlias(aliasId);

        // Wait for transaction inclusion
        await new Promise(resolve => setTimeout(resolve, 5000));

        await account.sync();
        console.log('Balance after destroying:\n', await account.getBalance());
    } catch (error) {
        console.log('Error: ', error);
    }
    process.exit(0);
}

run();
