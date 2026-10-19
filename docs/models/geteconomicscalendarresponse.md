# GetEconomicsCalendarResponse

Economic calendar response for the requested date. Use it to show macroeconomic events that may affect markets.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `events`                                                                   | List[[models.EconomicsCalendarEvent](../models/economicscalendarevent.md)] | :heavy_minus_sign:                                                         | List of economic calendar events for the requested date                    |
| `important_dates`                                                          | List[*str*]                                                                | :heavy_minus_sign:                                                         | Optional list of notable dates                                             |