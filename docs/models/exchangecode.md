# ExchangeCode

Two-to-three-letter exchange code identifying a global stock exchange (e.g. `US` = U.S. exchanges, `L` = London, `HK` = Hong Kong, `T` = Tokyo, `PA` = Paris). Used as the `exchange` query parameter for market-status and market-holiday endpoints. Other endpoints may return a different exchange-code format depending on the upstream data source.

## Example Usage

```python
from finance_dev.models import ExchangeCode

value = ExchangeCode.AD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `AD`  | AD    |
| `AS`  | AS    |
| `AT`  | AT    |
| `AX`  | AX    |
| `BA`  | BA    |
| `BC`  | BC    |
| `BD`  | BD    |
| `BE`  | BE    |
| `BH`  | BH    |
| `BK`  | BK    |
| `BO`  | BO    |
| `BR`  | BR    |
| `CA`  | CA    |
| `CN`  | CN    |
| `CO`  | CO    |
| `CR`  | CR    |
| `CS`  | CS    |
| `DB`  | DB    |
| `DE`  | DE    |
| `DU`  | DU    |
| `F`   | F     |
| `HA`  | HA    |
| `HE`  | HE    |
| `HK`  | HK    |
| `HM`  | HM    |
| `IC`  | IC    |
| `IR`  | IR    |
| `IS`  | IS    |
| `JK`  | JK    |
| `JO`  | JO    |
| `KL`  | KL    |
| `KQ`  | KQ    |
| `KS`  | KS    |
| `KW`  | KW    |
| `L`   | L     |
| `LS`  | LS    |
| `MC`  | MC    |
| `ME`  | ME    |
| `MI`  | MI    |
| `MT`  | MT    |
| `MU`  | MU    |
| `MX`  | MX    |
| `NE`  | NE    |
| `NL`  | NL    |
| `NS`  | NS    |
| `NZ`  | NZ    |
| `OL`  | OL    |
| `OM`  | OM    |
| `PA`  | PA    |
| `PK`  | PK    |
| `PM`  | PM    |
| `PR`  | PR    |
| `QA`  | QA    |
| `RG`  | RG    |
| `RO`  | RO    |
| `SA`  | SA    |
| `SC`  | SC    |
| `SG`  | SG    |
| `SI`  | SI    |
| `SN`  | SN    |
| `SR`  | SR    |
| `SS`  | SS    |
| `ST`  | ST    |
| `SW`  | SW    |
| `SX`  | SX    |
| `SZ`  | SZ    |
| `T`   | T     |
| `TA`  | TA    |
| `TG`  | TG    |
| `TL`  | TL    |
| `TO`  | TO    |
| `TW`  | TW    |
| `TWO` | TWO   |
| `US`  | US    |
| `V`   | V     |
| `VI`  | VI    |
| `VN`  | VN    |
| `VS`  | VS    |
| `WA`  | WA    |