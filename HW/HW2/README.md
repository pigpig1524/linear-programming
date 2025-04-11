<style>
r { color: Red }
o { color: Orange }
g { color: Green }
</style>

<font size="+12"><center>
    [LUMI ROBOT] - API DOCUMENTS
</center></font>

# Description

# Base URL
```bash
https://lumi-robot-stag.proudmoss-baf97b94.japaneast.azurecontainerapps.io
```
# Endpoints

## `POST /api/ask`
Get LLM's response to user's query

### Version
`01-01-2025` - Inherit from code base

### Parameters
|   Field name   |  type  | required |               note            |
|----------------|--------|----------|-------------------------------|
|  `voice_code`  | string | <r>*</r> |                               |
|  `user_query`  | string | <r>*</r> | using underscore insted       |

### Response
<!-- ##### <g>200 - Successful</g> -->
#### <g>200 - Successful</g>

#### <r>422 - Validation error</r>


## `POST /api/getTour`
### Description



### Headers

### Parameters