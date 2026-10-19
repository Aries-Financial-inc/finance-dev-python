# LobbyingResponse

US Senate and House lobbying activity reported for a company, as provided by Finnhub.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `data`                                                                 | List[[models.LobbyingResponseData](../models/lobbyingresponsedata.md)] | :heavy_minus_sign:                                                     | Lobbying records for the symbol.                                       |
| `symbol`                                                               | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Company ticker symbol.                                                 |