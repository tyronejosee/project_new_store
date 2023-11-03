"""Global Utils."""


def placeholder_attrs(placeholder):
    """Returns an HTML attribute dictionary to avoid code repetition."""
    return {
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-3xl focus:ring-sky-500 focus:border-sky-500 block w-full p-2.5 dark:bg-neutral-800 dark:border-neutral-700 dark:placeholder-gray-400 dark:text-white dark:focus:ring-sky-500 dark:focus:border-sky-500',
        'placeholder': placeholder,
    }
