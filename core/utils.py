"""Global Utils."""

def form_text_input(placeholder):
    """Utility classes for text input."""
    return {
        'class': 'form-input',
        'placeholder': placeholder,
    }

def form_number_input():
    """Utility classes for number input."""
    return {
        'class': 'form-input',
    }

def form_checkbox_input():
    """Utility classes for checkbox input."""
    return {
        'class': 'w-4 h-4 border border-gray-300 cs-rounded dark:bg-primary focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800'
    }

def form_file_input():
    """Utility classes for file input."""
    return {
        'class': 'absolute inset-0 w-full h-full opacity-0 cursor-pointer'
    }

def form_select():
    """Utility classes for select."""
    return {
        'class': 'bg-neutral-100 dark:bg-neutral-900 w-full cs-rounded h-12 px-4 focus:outline-none focus:ring focus:ring-primary',
    }

def form_textarea():
    """Utility classes for text area."""
    return {
        'class': 'bg-neutral-100 dark:bg-neutral-900 w-full p-2 cs-rounded p-4',
    }
