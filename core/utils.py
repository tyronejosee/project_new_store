"""Global Utils."""

def form_text_input(placeholder):
    """Utility classes for text input."""
    return {
        'class': 'bg-neutral-100 p-4 text-neutral-800 cs-rounded block w-full dark:bg-neutral-900 dark:text-neutral-200 dark:focus:ring-sky-500 dark:focus:border-sky-500',
        'placeholder': placeholder,
    }

def form_number_input(placeholder):
    """Utility classes for number input."""
    return {
        'class': 'bg-neutral-100 p-4 text-neutral-800 cs-rounded block w-full dark:bg-neutral-900 dark:text-neutral-200 dark:focus:ring-sky-500 dark:focus:border-sky-500',
        'placeholder': placeholder,
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
        'class': 'bg-neutral-100 dark:bg-neutral-900 w-full p-2 cs-rounded p-4',
    }

def form_textarea():
    """Utility classes for text area."""
    return {
        'class': 'bg-neutral-100 dark:bg-neutral-900 w-full p-2 cs-rounded p-4',
    }
