{
    'name': 'Book Rent',
    'author': "nimdasx",
    'website': "https://sofy.web.id",
    'summary': 'Aplikasi Book Rent',
    'version': '1.0',
    'application': True,
    'category': 'Productivity',
    'license': 'Other proprietary',
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/sfx_jenis_obat.csv',
        'views/sf_book_views.xml',
        'views/sf_rent_views.xml',
        'views/sf_rent_detail_views.xml',
        'views/menus.xml',
    ],

}
