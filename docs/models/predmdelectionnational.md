# PredMdElectionNational

The chamber-control markets. A market the venue does not list for the cycle is `null`.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `balance_of_power`                                                                      | [Nullable[models.BalanceOfPower]](../models/balanceofpower.md)                          | :heavy_check_mark:                                                                      | Which party controls each chamber: one outcome per Senate × House split (`FEDRO_1126`). |
| `house_control`                                                                         | [Nullable[models.HouseControl]](../models/housecontrol.md)                              | :heavy_check_mark:                                                                      | Which party controls the House (`HORC_1126`).                                           |
| `senate_control`                                                                        | [Nullable[models.SenateControl]](../models/senatecontrol.md)                            | :heavy_check_mark:                                                                      | Which party holds the Senate majority (`SENM_1126`).                                    |