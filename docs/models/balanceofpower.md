# BalanceOfPower

Which party controls each chamber: one outcome per Senate × House split (`FEDRO_1126`).


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `event_id`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  | HORC_1126                                                                            |
| `outcomes`                                                                           | List[[models.PredMdElectionMarketOutcome](../models/predmdelectionmarketoutcome.md)] | :heavy_check_mark:                                                                   | Sorted by `yesPrice`, highest first; untraded outcomes last.                         |                                                                                      |