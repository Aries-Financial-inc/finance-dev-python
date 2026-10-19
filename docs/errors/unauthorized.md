# Unauthorized

401 responses may use a flat `ErrorResponse` shape or a nested `error` object. Inspect `error`: if it is a string, use the flat shape; if it is an object, use the structured shape.


## Supported Types

### `errors.ErrorResponse`

```python
value: errors.ErrorResponse = /* values here */
```

### `errors.AuthenticationErrorEnvelope`

```python
value: errors.AuthenticationErrorEnvelope = /* values here */
```

