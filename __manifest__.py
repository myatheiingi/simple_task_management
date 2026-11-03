{
    'name': 'Simple Task Management',
    'version': '19.0.1.0.0',
    'summary': 'Simple Employee Task Management',
    'category': 'Productivity',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
    ],
    'application': True,
    'installable': True,
}