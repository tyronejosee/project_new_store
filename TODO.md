# TODO List

- Reimplement User App
- Support
- FQs
- Deals
- devoluciones y cambios

## Dependencies

- django-import-export
- Pillow
- django-ckeditor
- django-tailwind
- psycopg2
- boto3





<div class="container mx-auto mt-6 p-6 bg-white shadow-lg rounded-lg text-left">
        {% if page.image %}
            <div><img src="{{ page.image.url }}" alt="page-image"></div>
        {% else %}
            <div><img src="{% static 'img/default-image-front.webp' %}" alt="default-image"></div>
        {% endif %}
        <p>{{ page.content | safe }}</p>
    </div>
