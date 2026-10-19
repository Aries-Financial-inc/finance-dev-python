# ErrorCode

A single structured error entry identifying a machine-readable code, a human-readable description, and optionally the field that caused it.


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `code`                                       | *Optional[str]*                              | :heavy_minus_sign:                           | Machine-readable error code                  | INVALID_PASSWORD                             |
| `description`                                | *Optional[str]*                              | :heavy_minus_sign:                           | Human-readable description of the error      | Password must be between 8 and 64 characters |
| `field`                                      | *Optional[str]*                              | :heavy_minus_sign:                           | Field name that caused the error             | password                                     |