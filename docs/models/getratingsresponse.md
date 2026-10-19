# GetRatingsResponse

Response for GET /v1/analytics/ratings. Only non-empty fields appear in each rating; notes and ratings_accuracy are omitted when empty.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `ratings`                                  | List[[models.Rating](../models/rating.md)] | :heavy_minus_sign:                         | Array of analyst rating objects            |