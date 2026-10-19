# AccountItemStatus

Account status. **OPEN** = account open for trading; **SUSPENDED** = account suspended; **CLOSED** = account closed; **PENDING_APEX_VERIFICATION** = sent to Apex, awaiting verification; **CANCELED** = account canceled; **REJECTED** = application/account rejected.

## Example Usage

```python
from finance_dev.models import AccountItemStatus

value = AccountItemStatus.NEW

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                         | Value                        |
| ---------------------------- | ---------------------------- |
| `NEW`                        | NEW                          |
| `PENDING_PLAID_VERIFICATION` | PENDING_PLAID_VERIFICATION   |
| `PENDING_APEX_VERIFICATION`  | PENDING_APEX_VERIFICATION    |
| `READY_FOR_BACK_OFFICE`      | READY_FOR_BACK_OFFICE        |
| `BACK_OFFICE`                | BACK_OFFICE                  |
| `OPEN`                       | OPEN                         |
| `CANCELED`                   | CANCELED                     |
| `REJECTED`                   | REJECTED                     |
| `SUSPENDED`                  | SUSPENDED                    |
| `CLOSED`                     | CLOSED                       |
| `ERROR`                      | ERROR                        |
| `AWAITING_REVIEW`            | AWAITING_REVIEW              |
| `AWAITING_APEX`              | AWAITING_APEX                |
| `RETURNED_APEX`              | RETURNED_APEX                |
| `PENDING_CLOSE`              | PENDING_CLOSE                |
| `STERLING_PENDING`           | STERLING_PENDING             |