{
    "name": "POS Custom Reciept",
    "version": "17.0.3.2.1",
    'sequence': 1,
    "description": """
        POS Custom Reciept
    """,
    "summary": """POS Custom Reciept""",
    "category": "Point Of Sale",
    'price': 0,
    'currency': 'USD',
    'license': 'OPL-1',
    'sequence': 1,
    "depends": ["point_of_sale"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_custom_receipt/static/src/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
