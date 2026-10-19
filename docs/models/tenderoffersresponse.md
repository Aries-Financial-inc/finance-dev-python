# TenderOffersResponse

Tender offers found for the requested security and date window.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `security`                                                                                 | [Optional[models.TenderOffersResponseSecurity]](../models/tenderoffersresponsesecurity.md) | :heavy_minus_sign:                                                                         | Security the tender offers relate to                                                       |
| `tender_offers`                                                                            | List[[models.TenderOffer](../models/tenderoffer.md)]                                       | :heavy_check_mark:                                                                         | List of tender offer records                                                               |