# WatchlistResponse

Response body containing the user's saved watchlists.


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                  | *Optional[int]*                                                                                            | :heavy_minus_sign:                                                                                         | User ID that owns these watchlists. Use it to confirm the response belongs to the expected connected user. |
| `watchlist`                                                                                                | List[[models.Watchlist](../models/watchlist.md)]                                                           | :heavy_minus_sign:                                                                                         | Saved watchlists for the user. Render each item as a named list of symbols.                                |