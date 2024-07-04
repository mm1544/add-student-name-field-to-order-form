{
    'name': 'Add student name field to order form',
    'version': '1.0',
    'category': 'Generic Modules/Others',
    'summary': 'For Edgeborough website, on "/shop/address" URL take x_student_name field and copy to created contact\'s x_student_name field.',
    'sequence': '1',
    'author': 'Martynas Minskis',
    'depends': ['sale'],
    'demo': [],
    'data': [

        #        Sequence: security, data, wizards, views
        # 'security/ir.model.access.csv',
        # 'wizard/sale_order_wizard.xml',
        # 'views/sale_order_view.xml',
    ],
    'demo': [],
    'qweb': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}
