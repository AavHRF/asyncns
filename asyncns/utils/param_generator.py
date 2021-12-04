class ParamGenerator:

    def __init__(self):
        self.params = {}

    def dispatch_params(
            self,
            action: str,
            title: str = None,
            text: str = None,
            category: int = None,
            subcategory: int = None,
            dispatch_id: int = None,
    ) -> dict:
        """
        A method to generate dispatch parameters that is somewhat more intuitive than making a dictionary.
        Function parameters are mapped to the keys in the dictionary.

        | Parameter | Description |
        | --------- | ----------- |
        | action | The action to perform. (add, edit, or delete) Required in all operations|
        | title | The title of the dispatch. Required in add or edit operations |
        | text | The text of the dispatch. Required in add or edit operations |
        | category | The category of the dispatch. Required in add or edit operations |
        | subcategory | The subcategory of the dispatch. Required in add or edit operations |
        | dispatch_id | The id of the dispatch. Required in edit and delete operations |

        :param action: str
        :param title: str
        :param text: str
        :param category: int
        :param subcategory: int
        :param dispatch_id: int
        :return: params
        :rtype: dict
        """
        if action.lower() == "add":
            self.params = {
                "dispatch": "add",
                "title": title,
                "text": text,
                "category": category,
                "subcategory": subcategory,
            }
        elif action.lower() == "edit":
            self.params = {
                "dispatch": "edit",
                "dispatch_id": dispatch_id,
                "title": title,
                "text": text,
                "category": category,
                "subcategory": subcategory,
            }
        elif action.lower() == "remove":
            self.params = {
                "dispatch": "remove",
                "dispatch_id": dispatch_id,
            }
        else:
            raise ValueError(f"Unknown action: {action}")

        return self.params
