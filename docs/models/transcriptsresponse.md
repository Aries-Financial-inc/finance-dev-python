# TranscriptsResponse

List of available earnings call transcripts for a company.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `symbol`                                                                                 | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | Ticker symbol of the company.                                                            |
| `transcripts`                                                                            | List[[models.TranscriptsResponseTranscript](../models/transcriptsresponsetranscript.md)] | :heavy_minus_sign:                                                                       | Available earnings call transcripts.                                                     |