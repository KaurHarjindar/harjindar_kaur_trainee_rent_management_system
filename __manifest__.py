{
    'name' : 'Tenants Management system',
    'version' : '1.1',
    'summary' : 'manage the tenants',
    'author': "Harjindar",
    'depends': ['web_dashboard'],
    'data' : [
        'security/ir.model.access.csv',

        # 'wizard/inquiry_view.xml',
       	
       	'views/owner.xml',
    ],
    'demo' : [
      'demo/demo.xml',
    ],
       
}