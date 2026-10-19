# StockLastQuoteResponseResults

Last NBBO quote object


## Fields

| Field                   | Type                    | Required                | Description             |
| ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| `ask_exchange`          | *Optional[int]*         | :heavy_minus_sign:      | Ask exchange ID         |
| `ask_price`             | *Optional[float]*       | :heavy_minus_sign:      | Ask price               |
| `ask_size`              | *Optional[int]*         | :heavy_minus_sign:      | Ask size                |
| `bid_exchange`          | *Optional[int]*         | :heavy_minus_sign:      | Bid exchange ID         |
| `bid_price`             | *Optional[float]*       | :heavy_minus_sign:      | Bid price               |
| `bid_size`              | *Optional[int]*         | :heavy_minus_sign:      | Bid size                |
| `conditions`            | List[*int*]             | :heavy_minus_sign:      | Quote conditions        |
| `indicators`            | List[*int*]             | :heavy_minus_sign:      | Quote indicators        |
| `participant_timestamp` | *Optional[int]*         | :heavy_minus_sign:      | Participant timestamp   |
| `sequence_number`       | *Optional[int]*         | :heavy_minus_sign:      | Sequence number         |
| `sip_timestamp`         | *Optional[int]*         | :heavy_minus_sign:      | SIP timestamp           |
| `tape`                  | *Optional[int]*         | :heavy_minus_sign:      | Tape                    |
| `ticker`                | *Optional[str]*         | :heavy_minus_sign:      | Ticker symbol           |
| `trf_timestamp`         | *Optional[int]*         | :heavy_minus_sign:      | TRF timestamp           |