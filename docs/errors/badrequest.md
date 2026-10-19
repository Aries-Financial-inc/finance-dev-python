# BadRequest

400 responses commonly use a nested `error` object (`type`, `code`, `message`, optional `details`). Some services still return flat `ErrorResponse` (`error` string, optional `codes`).


## Supported Types

### `errors.AuthenticationErrorEnvelope`

```python
value: errors.AuthenticationErrorEnvelope = /* values here */
```

### `errors.ErrorResponse`

```python
value: errors.ErrorResponse = /* values here */
```

