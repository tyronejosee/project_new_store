"""Global Utils."""

def form_text_input(placeholder):
    """Utility classes for text input."""
    return {
        'class': 'bg-neutral-100 p-4 text-neutral-800 rounded-xl block w-full dark:bg-neutral-900 dark:text-neutral-200 dark:focus:ring-sky-500 dark:focus:border-sky-500',
        'placeholder': placeholder,
    }


def form_number_input(placeholder):
    """Utility classes for number input."""
    return {
        'class': 'bg-neutral-100 p-4 text-neutral-800 rounded-xl block w-full dark:bg-neutral-900 dark:text-neutral-200 dark:focus:ring-sky-500 dark:focus:border-sky-500',
        'placeholder': placeholder,
    }


def form_select():
    """Utility classes for select."""
    return {
        'class': 'bg-neutral-100 dark:bg-neutral-900 w-full p-2 rounded-xl p-4',
    }


def form_textarea():
    """Utility classes for text area."""
    return {
        'class': 'bg-neutral-100 dark:bg-neutral-900 w-full p-2 rounded-xl p-4',
    }
