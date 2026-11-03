# Leader

The highest-priced outcome shown, to colour the race by. `null` while no outcome has traded.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `party`                                                                          | [Nullable[models.PredMdElectionRaceParty]](../models/predmdelectionraceparty.md) | :heavy_check_mark:                                                               | The leader's party. `null` when the venue has none for the candidate.            |                                                                                  |
| `symbol`                                                                         | *str*                                                                            | :heavy_check_mark:                                                               | N/A                                                                              | AXXTX_110326_JT                                                                  |
| `yes_price`                                                                      | *Nullable[Decimal]*                                                              | :heavy_check_mark:                                                               | The leader's `yesPrice`. Exact decimal string.                                   | 0.66                                                                             |