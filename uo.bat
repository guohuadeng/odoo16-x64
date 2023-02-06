rem 更新 addons_odoo，最常用的 odoo模块，如更新了企业版，先执行 .\ment.bat
title update addons_odoo

rd /s/q .\addons_odoo

xcopy d:\odoo16-x64\source\odoo\addons\base\* .\addons_odoo\base\ /E /Y

xcopy d:\odoo16-x64\source\odoo\addons\account\* .\addons_odoo\account\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\auth_oauth\* .\addons_odoo\auth_oauth\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\auth_signup\* .\addons_odoo\auth_signup\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\base_import\* .\addons_odoo\base_import\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\contacts\* .\addons_odoo\contacts\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\delivery\* .\addons_odoo\delivery\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\fleet\* .\addons_odoo\fleet\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\hr\* .\addons_odoo\hr\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\hr_expense\* .\addons_odoo\hr_expense\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\l10n_cn\* .\addons_odoo\l10n_cn\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\l10n_cn_city\* .\addons_odoo\l10n_cn_city\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\mail\* .\addons_odoo\mail\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\maintenance\* .\addons_odoo\maintenance\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\mrp\* .\addons_odoo\mrp\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\mrp_bom_cost\* .\addons_odoo\mrp_bom_cost\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\mrp_subcontracting\* .\addons_odoo\mrp_subcontracting\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\mrp_subcontracting_account\* .\addons_odoo\mrp_subcontracting_account\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\mrp_subcontracting_dropshipping\* .\addons_odoo\mrp_subcontracting_dropshipping\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\mrp_account\* .\addons_odoo\mrp_account\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\payment\* .\addons_odoo\payment\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\payment_alipay\* .\addons_odoo\payment_alipay\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\payment_transfer\* .\addons_odoo\payment_transfer\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\portal\* .\addons_odoo\portal\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\point_of_sale\* .\addons_odoo\point_of_sale\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\procurement_jit\* .\addons_odoo\procurement_jit\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\product\* .\addons_odoo\product\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\product_expiry\* .\addons_odoo\product_expiry\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\product_matrix\* .\addons_odoo\product_matrix\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\project\* .\addons_odoo\project\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\purchase\* .\addons_odoo\purchase\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\purchase_mrp\* .\addons_odoo\purchase_mrp\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\purchase_requisition\* .\addons_odoo\purchase_requisition\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\purchase_requisition_stock\* .\addons_odoo\purchase_requisition_stock\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\purchase_stock\* .\addons_odoo\purchase_stock\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\report\* .\addons_odoo\report\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale\* .\addons_odoo\sale\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_coupon\* .\addons_odoo\sale_coupon\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_expense\* .\addons_odoo\sale_expense\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_management\* .\addons_odoo\sale_management\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_mrp\* .\addons_odoo\sale_mrp\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_product_configurator\* .\addons_odoo\sale_product_configurator\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_product_matrix\* .\addons_odoo\sale_product_matrix\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_stock\* .\addons_odoo\sale_stock\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sales_team\* .\addons_odoo\sales_team\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sale_expense\* .\addons_odoo\sale_expense\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\stock\* .\addons_odoo\stock\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\stock_account\* .\addons_odoo\stock_account\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\stock_picking_batch\* .\addons_odoo\stock_picking_batch\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\sms\* .\addons_odoo\sms\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\uom\* .\addons_odoo\uom\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\web\* .\addons_odoo\web\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\website\* .\addons_odoo\website\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\website_sale\* .\addons_odoo\website_sale\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\website_sale_comparison\* .\addons_odoo\website_sale_comparison\ /E /Y
xcopy d:\odoo16-x64\source\odoo\addons\website_sale_coupon\* .\addons_odoo\website_sale_coupon\ /E /Y

rd /s/q d:\odoo16-x64\addons_odoo
xcopy .\addons_odoo\* d:\odoo16-x64\addons_odoo\ /E /Y
