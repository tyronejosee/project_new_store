"""Global Utils."""


def placeholder_attrs(placeholder):
    """Returns an HTML attribute dictionary to avoid code repetition."""
    return {
        'class': 'bg-neutral-100 p-4 text-neutral-800 rounded-xl block w-full dark:bg-neutral-900 dark:text-neutral-200 dark:focus:ring-sky-500 dark:focus:border-sky-500',
        'placeholder': placeholder,
    }
