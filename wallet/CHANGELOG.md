# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- ## Unreleased - YYYY-MM-DD

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security -->

## 1.0.0-rc.7 - 2023-XX-XX

### Changed

- Resync outputs if a transaction got confirmed between syncing outputs and pending transactions to prevent not having unspent outputs afterwards;

## 1.0.0-rc.6 - 2023-03-09

### Added

- `Default` to `FilterOptions`;
- `ParticipationEventRegistrationOptions` type;
- `AccountManager::update_node_auth()`;
- `Message::UpdateNodeAuth`;
- `event_ids` parameter to `Account::get_participation_overview()`;

### Changed

- Updated dependencies;
- `StorageAdapter::get` return type changed to `Result<Option<String>>`;
- `StorageManager::get_account_manager_data` return type changed to `Result<Option<AccountManagerBuilder>>`;
- `Features::{tag, metadata}` encoded as hex strings instead of utf-8 strings for NFT Outputs;
- Added `#[serde(rename = "transactionOptions")]` to `PrepareOutput::transaction_options`;
- `AccountMethod::RegisterParticipationEvent` renamed to `AccountMethod::RegisterParticipationEvents`,
  contains a `ParticipationEventRegistrationOptions` and expects a `ParticipationEvents` response;
- `AccountMethod::GetParticipationEventIds` now also contains a `Node`;
- Custom `Serialize` implementation for `Error`;
- Reduced `MIN_SYNC_INTERVAL`;
- Made `TransactionOptionsDto`, `ReturnStrategy` and `MintTokenTransactionDto` pub reachable;

### Removed

- `mnemonic` feature;
- `Error::RecordNotFound` variant;

### Fixed

- `Account::get_participation_overview()` with multiple events and different nodes;
- `prepare_nft_output` uses newly provided tag/metadata instead of previous ones from unspent output;
- `Account::claim_outputs()` when the account has no basic outputs available;
- SDR amount in `Account::prepare_output()`;
- Address for the amount of expired NFTs that get burned with `Account::burn_nft()`;

## 1.0.0-rc.5 - 2023-02-09

### Added

- `Account::get_participation_event_ids` method;
- `RequiredStorageDeposit::{alias(), basic(), foundry(), nft()}` getters;
- `TransactionOptionsDto`;
- `Transaction::inputs` and `TransactionDto::inputs` fields;
- Derive `Eq, PartialEq` for `Account` and `OutputData`;
- `AccountSyncOptions, AliasSyncOptions, NftSyncOptions`;
- `SyncOptions::{account, alias, nft}` fields;
- `{TransactionOptions, TransactionOptionsDto}::burn`;
- `Memory` and `Wasm` storage adapters;
- `ParticipationEventWithNodes`;
- Support for target `wasm32-unknown-unknown`;
- `Error::Participation`;

### Changed

- Use new Input Selection Algorithm;
- Updated dependencies;
- Message interface methods to accept `TransactionOptionsDto` instead of `TransactionOptions`;
- `send_message` to return Option which is None when no message response is received;
- Moved `init_logger` to message interface mod;
- Limit max parallel requests for incoming transactions;
- Move all participation methods from the AccountManager to the Account;
- `Account::get_participation_overview` sends requests now in parallel;
- `Account::{get_incoming_transaction_data(), incoming_transactions()}` return now `Transaction` instead of `(TransactionPayload, Vec<OutputWithMetadataResponse>)`;
- `AccountDto::incoming_transactions` from `(TransactionPayloadDto, Vec<OutputWithMetadataResponse>)` to `TransactionDto`;
- `Response::{IncomingTransactionData, IncomingTransactionsData}` contain `TransactionDto` instead of `IncomingTransactionDataDto`;
- Default `SyncOptions` don't sync alias and nft outputs anymore;
- `{OutputData, OutputDataDto}::metadata` type from `OutputMetadataResponse` to `OutputMetadataDto`;
- `RocksDb` storage is now an optional storage adapter;
- `Account::{register_participation_event(), get_participation_event(), get_participation_events()}` have `ParticipationEventWithNodes` instead of `(ParticipationEvent, Vec<Node>)` in their return type;
- `Response::{ParticipationEvents, ParticipationEvents}` contain `ParticipationEventWithNodes` instead of `(ParticipationEvent, Vec<Node>)`;
- Remove `Error` suffix on some `Error` variants;
- Exposed `FilterOptions` so it can be imported from `account::FilterOptions`;
- Only expose `MessageHandler` methods `SetStrongholdPassword`, `SetStrongholdPasswordClearInterval` and `StoreMnemonic` when `feature = "stronghold"` is enabled; 
- `Message::{GetAccount, VerifyMnemonic, SetClientOptions, SetStrongholdPassword, SetStrongholdPasswordClearInterval, StoreMnemonic, EmitTestEvent, Bech32ToHex, ClearListeners}` to named fields for better error messages;
- Made `AccountManager::stop_background_syncing()` async to await until syncing actually stopped;
- `OutputData::input_signing_data` returns `Result<Option<InputSigningData>>` instead of `Result<InputSigningData>>`;
- `OutputData::input_signing_data` accepts `Option<AliasTransition>` instead of `bool`;
- Made all fields of `ManagerOptions` pub;
- Renamed `WalletMessageHandler::handle()` to `WalletMessageHandler::send_message()`, removed the `response_tx` parameter and returned the `Response`;

### Removed

- `clear_listeners` from the `WalletMessageHandler`;
- `IncomingTransactionDataDto` type;
- `SyncOptions::sync_aliases_and_nfts`;
- `{TransactionOptions, TransactionOptionsDto}::allow_burning`;
- Background task spawning to retry a transaction;
- `message_interface::send_message()`;

### Fixed

- Stop endlessly requesting inaccessible incoming transactions;
- Update addresses when a client config with a different HRP is passed;
- Return client errors from `Account::get_participation_overview()`;
- Stop endlessly waiting in `AccountManager::stop_background_syncing()` if background syncing wasn't started;

## 1.0.0-rc.4 - 2022-12-23

### Added

- `RequiredStorageDeposit` and `RequiredStorageDepositDto` types;
- `account/types/balance` module;
- `AccountBuilder::with_bech32_hrp()`;
- `Account::retry_transaction_until_included()`;
- `RetryTransactionUntilIncluded` to message interface account methods;
- `AccountMethod::RequestFundsFromFaucet` to message interface;
- `FilterOptions::output_types` field;
- `{NativeTokensBalance, NativeTokensBalanceDto}::metadata` field;
- `{Account, AccountDto}::native_token_foundries` field;
- `SyncOptions::sync_native_token_foundries` field;

### Changed

- `AccountBalance::required_storage_deposit` changed from `u64` to `RequiredStorageDeposit`;
- `AccountBalanceDto::required_storage_deposit` changed from `String` to `RequiredStorageDepositDto`;
- Move all balance related types to the `account/types/balance` module;
- `AccountBalanceDto`, `BaseCoinBalanceDto` and `NativeTokensBalanceDto` moved from `message_interface/dtos` to `account/types/balance`;
- `Account::vote(), AccountMethod::Vote()` parameters are now optional to support revoting;
- Fields of `Error::{ConsolidationRequired, InsufficientFunds, InvalidCoinType}` are now named;

### Removed

- `listen` from message interface;
- default bech32 HRP in account builder;
- `Copy` from `FilterOptions`;

## 1.0.0-rc.3 - 2022-11-24

### Added

- `IssuerFeature` and `SenderFeature` to `prepare_output()` options argument;
- Participation feature and functions;

### Changed

- Use `OutputWithMetadataResponse` instead of `OutputResponse`;
- `AccountHandle::build_transaction_essence` made async;
- `Error::ClientError` renamed to `Error::Client` and boxed;
- `WalletEvent::SpentOutput` boxed;
- Allow null nft ids in `prepare_output()` for minting;
- `TagFeature` & `MetadataFeature` encoded as hex strings instead of utf-8 strings;
- Call `try_get_outputs_metadata` instead of `try_get_outputs` when possible (more efficient);

### Removed

- `Error::IotaClientError` as it was a duplicate;

### Fixed

- Min storage deposit amount in `prepare_output()` with expiration unlock condition;
- NFT id in `prepare_output()` when the NFT output still has the null id;

## 1.0.0-rc.2 - 2022-10-28

### Added

- `GetAccountIndexes` and `AccountIndexes` to message interface;
- Missing serde rename for the `returnAddress` field of `AddressWithMicroAmountDto`;
- Check for parameters before creating the database;
- Transaction essence and payload length validation;

### Changed

- Updated dependencies;
- Derived `Serialize` for `Message` and `AccountMethod` instead of custom impl;
- Removed `AccountToCreate` struct and moved its field to `Message::CreateAccount`;

### Fixed

- NFT output claiming;
- Alias and NFT owned outputs syncing;
- Alias or nft addresses in address unlock condition;

## 1.0.0-rc.1 - 2022-09-28

First RC for the stardust implementation of the wallet.
