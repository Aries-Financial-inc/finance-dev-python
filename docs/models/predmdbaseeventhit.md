# PredMdBaseEventHit

One base event with at least one matching contract. The index carries no display name; read it through /base-events/{baseEventId}.


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `base_event_id`                                                                                   | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `contracts_found`                                                                                 | *int*                                                                                             | :heavy_check_mark:                                                                                | Every matching contract under this hit. Read them with type=contracts and eventId or baseEventId. |
| `underlying_spec`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |