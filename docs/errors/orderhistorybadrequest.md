# OrderHistoryBadRequest

Bad request: missing or invalid `from`/`to`, range over 90 days, or invalid `order_by`, returned as a flat `ErrorResponse` (`error` string). Account-ID path validation failures return the nested error envelope.


## Supported Types

### `errors.ErrorResponse`

```python
value: errors.ErrorResponse = /* values here */
```

### `errors.AuthenticationErrorEnvelope`

```python
value: errors.AuthenticationErrorEnvelope = /* values here */
```

