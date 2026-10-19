# GetOptionDetailsResponse

Wrapper for GET /v1/marketdata/options/details: `data` for successful symbols, `errors` when applicable.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | List[[models.OptionDetailsDTO](../models/optiondetailsdto.md)]                | :heavy_minus_sign:                                                            | Option contracts that returned a pricing snapshot                             |
| `errors`                                                                      | List[[models.SymbolError](../models/symbolerror.md)]                          | :heavy_minus_sign:                                                            | Per-symbol error entries when a requested symbol cannot be included in `data` |