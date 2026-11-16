# SenateControl

Which party holds the Senate majority (`SENM_1126`).


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          | Example                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `event_id`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  | HORC_1126                                                                            |
| `outcomes`                                                                           | List[[models.PredMdElectionMarketOutcome](../models/predmdelectionmarketoutcome.md)] | :heavy_check_mark:                                                                   | Sorted by `yesPrice`, highest first; untraded outcomes last.                         |                                                                                      |