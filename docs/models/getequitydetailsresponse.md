# GetEquityDetailsResponse

Wrapper for GET /v1/marketdata/equities/details: `data` for successful symbols, `errors` when applicable.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | List[[models.EquityDetailsDTO](../models/equitydetailsdto.md)]                | :heavy_minus_sign:                                                            | Symbols that returned a non-empty snapshot with valid quote data              |
| `errors`                                                                      | List[[models.SymbolError](../models/symbolerror.md)]                          | :heavy_minus_sign:                                                            | Per-symbol error entries when a requested symbol cannot be included in `data` |