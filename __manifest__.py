# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'odoo_patch',
    'version' : '1.1',
    'summary': """
    可以配置edit create delete等参数实现动态（根据每条记录）的显示删除，新建、编辑按钮
        edit='{"domain": "state!=\"draft\""}'""",
    'sequence': 15,
    'category': 'tools',
    'depends': ['base'],
    'data': ["xml/odoo_patch.xml"],
    'installable': True,
    'application': True,
    'auto_install': False,
}