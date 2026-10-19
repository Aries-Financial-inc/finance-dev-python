# SymbolError

Error entry for a symbol that could not be resolved in a details request.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                | Example                                                                                    |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `error`                                                                                    | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Error detail as a string. Exact message content is not fixed and should not be hard-coded. | string                                                                                     |
| `symbol`                                                                                   | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | Symbol that had an error                                                                   | string                                                                                     |