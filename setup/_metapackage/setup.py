import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-calendar",
    description="Meta package for oca-calendar Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-calendar_event_link_base>=16.0dev,<16.1dev',
        'odoo-addon-calendar_event_type_color>=16.0dev,<16.1dev',
        'odoo-addon-calendar_monthly_multi>=16.0dev,<16.1dev',
        'odoo-addon-resource_booking>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
