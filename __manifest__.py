{
    'name': 'Library Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',


        'views/book_views.xml',
        'views/borrower_views.xml',
        'views/loan_views.xml'
    ],
    'installable': True,
    'application': True
}
