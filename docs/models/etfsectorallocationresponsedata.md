# EtfSectorAllocationResponseData

ETF sector exposure payload.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `sector_exposure`                                          | List[[models.SectorExposure](../models/sectorexposure.md)] | :heavy_minus_sign:                                         | List of sector exposures for the ETF.                      |
| `symbol`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | ETF ticker symbol.                                         |