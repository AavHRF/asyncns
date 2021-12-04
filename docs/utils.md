# `utils` documentation

### `asyncns.utils.param_generator`:
**Class**: `asyncns.utils.param_generator.ParamGenerator`

**Class Methods**:  
`asyncns.utils.param_generator.ParamGenerator.dispatch_params()`

| Parameter   | Type  | Description                                                              |
|-------------|-------|--------------------------------------------------------------------------|
| action      | `str` | The action to perform. (add, edit, or delete) Required in all operations |
| title       | `str` | The title of the dispatch. Required in add or edit operations            |
| text        | `str` | The text of the dispatch. Required in add or edit operations             |
| category    | `int` | The category of the dispatch. Required in add or edit operations         |
| subcategory | `int` | The subcategory of the dispatch. Required in add or edit operations      |
| dispatch_id | `int` | The id of the dispatch. Required in edit and delete operations           |

Example:
```py
from asyncns.utils import ParamGenerator
generator = ParamGenerator()
params = generator.dispatch_params(
    action='add',
    title='Test',
    text='Test',
    category=1,
    subcategory=1,
)
```