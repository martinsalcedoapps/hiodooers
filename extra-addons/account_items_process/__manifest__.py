{
    'name'        : 'MSP Account Items Process',
    'version'     : '0.1',
    'summary'     : "MSP Account Items Process",
    'description' : "Estructura Básica para Wizard",
    'author'      : "Martin Salcedo Pacheco",
    'website'     : 'https://www.msalcedo.com/',
    'depends'     : [
        'base',
        'account',
    ],
    'category'    : 'Customizations',
    'sequence'    : 10,
    'demo'        : [

    ],
    'data'        : [
        # 'entries/module_actions_act_window.xml',
        # 'entries/module_menu.xml',

        'security/ir_model_access.xml',

        'views/account_move.xml',

        'wizard/account_items_process.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install': False,
    'assets'      : {},
    'license'     : 'LGPL-3',
}
