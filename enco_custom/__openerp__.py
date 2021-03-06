# -*- coding: utf-8 -*-
# © 2016 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Enco - Custom",
    "version": "8.0.1.0.0",
    "author": "AvanzOSC",
    "license": "AGPL-3",
    "category": "Custom module",
    "website": "http://www.avanzosc.es",
    "contributors": [
        "Ana Juaristi <ajuaristio@gmail.com>",
        "Esther Martín <esthermartin@avanzosc.es>",
    ],
    "depends": [
        "account",
        "sale",
        "sale_stock",
        ],
    "data": [
        "report/report_layout.xml",
        "report/report_paperformat.xml",
        "report/report_generalledger.xml",
        "views/sale_order_view.xml",
        ],
    "installable": True
}
