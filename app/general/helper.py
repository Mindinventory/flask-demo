def getting_schema_error(e):
    """
    Give error message from the schema 
    """
    error_messages = []
    for field, errors in e.messages.items():
        for error in errors:
            error_messages.append(f"{field}: {error}")
    if error_messages:
        return error_messages[0]