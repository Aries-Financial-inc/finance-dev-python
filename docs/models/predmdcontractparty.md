# PredMdContractParty

The candidate's party from the venue: `D` Democratic, `R` Republican, `I` independent, `O` any other. `null` on a contract that is not a candidate.

## Example Usage

```python
from finance_dev.models import PredMdContractParty

value = PredMdContractParty.D

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name  | Value |
| ----- | ----- |
| `D`   | D     |
| `R`   | R     |
| `I`   | I     |
| `O`   | O     |