from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route


class WebsiteSaleInherit(WebsiteSale):

    @route(['/shop/address'], type='http', auth="public", website=True, sitemap=False)
    def address(self, **post):

        # Check if the current website is "Edgeborough School eStore"
        website = request.website
        if website.name and website.name == "Edgeborough School eStore":
            res = super(WebsiteSaleInherit, self).address(**post)

            if post.get('x_student_name'):
                order = request.website.sale_get_order()
                if order:
                    partner = order.partner_id
                    partner.sudo().write(
                        {'x_student_name': post['x_student_name']})

            return res
        else:
            # If website name is not "Edgeborough School eStore", call the original method
            return super(WebsiteSaleInherit, self).address(**post)
