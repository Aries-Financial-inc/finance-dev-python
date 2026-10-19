# NewsTypeEnum

Source category of the news item. Pick one:
- `news` — Editorial news articles from journalists and news services.
- `press_release` — Official press releases issued directly by companies.

## Example Usage

```python
from finance_dev.models import NewsTypeEnum

value = NewsTypeEnum.NEWS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `NEWS`          | news            |
| `PRESS_RELEASE` | press_release   |