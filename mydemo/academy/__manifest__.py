# -*- coding: utf-8 -*-
{
    'name':"demo_website",
    'summary':"""网站建设""",
    'description':"""网站建设""",
    'author':"teddy",
    'website':"http://www.yourcompany.com",

    'category':'Uncategorized',
    'version':'0.1',


    #any module necessary for this one to work correcly
    'depends':['website'],


    #always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
    ],

    # only loaded in demonstration mode
    'demo':[
        'demo/demo.xml',
    ],


}