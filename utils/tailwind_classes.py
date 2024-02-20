"""Utils: Tailwind CSS Classes."""


def form_text(placeholder):
    """Utility classes for text input."""
    return {"class": "form__input-text", "placeholder": placeholder}


def form_text_readonly(placeholder):
    """Utility classes for text input readonly."""
    return {"class": "form__input-text--readonly", "placeholder": placeholder}


def form_number(placeholder):
    """Utility classes for number input."""
    return {"class": "form__input-number", "placeholder": placeholder}


def form_checkbox():
    """Utility classes for checkbox input."""
    return {"class": "form__input-checkbox"}


def form_file():
    """Utility classes for file input."""
    return {"class": "form__input-file"}


def form_select():
    """Utility classes for select."""
    return {"class": "form__input-select"}


def form_textarea():
    """Utility classes for text area."""
    return {"class": "form__input-textarea"}
