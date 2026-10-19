<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from finance_dev import FinanceDev, models


with FinanceDev(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as fd_client:

    res = fd_client.accounts.get_account_positions(id="TEST-ACCOUNT-001")

    assert res.get_positions_response is not None

    # Handle response
    print(res.get_positions_response)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from finance_dev import FinanceDev, models

async def main():

    async with FinanceDev(
        security=models.Security(
            client_id="<YOUR_CLIENT_ID_HERE>",
            client_secret="<YOUR_CLIENT_SECRET_HERE>",
        ),
    ) as fd_client:

        res = await fd_client.accounts.get_account_positions_async(id="TEST-ACCOUNT-001")

        assert res.get_positions_response is not None

        # Handle response
        print(res.get_positions_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->