from odoo import http
from odoo.http import request


class Tenants(http.Controller):
    #tenants detail view
    @http.route('/tenants', auth='public', website=True,csrf=False)
    def tenants_details(self , **kw):
       tenants_details = request.env['training.tenants'].search([])
       return  request.render('rms.tenant_webview', {'tenantsDetail':tenants_details})

    #create and edit tenants
    @http.route(['/tenants/edit/','/tenants/editform/<model("training.tenants"):s>'],auth='public',website=True,csrf=False)
    def tenantform(self, s=None):
        tenantsform=None
        if s:
            tenantsform = http.request.env['training.tenants'].browse([s.id])
        return http.request.render('rms.tenant_form',{'tenantsform' : tenantsform})

    @http.route(['/tenants/submit/','/tenants/submit/<int:s>'],type='http',auth="public",website=True,csrf=False, method='post')
    def tenantsedit(self,s,**kw):
        print("hello",s)
        if kw:
            if s:
                request.env['training.tenants'].browse([s]).write({
                    'name':kw.get('name'),
                    'dob':kw.get('dob'),
                    'gender':kw.get('gender'),
                    'phone':kw.get('phone'),
                    'email':kw.get('email'),
                    'Religion':kw.get('Religion'),
                    'Marital_status':kw.get('Marital_status'),
                    'Home_address':kw.get('Home_address'),
                    'Occupation':kw.get('Occupation'),
                    'Father_name':kw.get('Father_name'),
                    'Fphone':kw.get('Fphone'),

                    })
            else:
                request.env["training.tenants"].create({
                        'name':kw.get('name'),
                        'dob':kw.get('dob'),
                        'gender':kw.get('gender'),
                        'phone':kw.get('phone'),
                        'email':kw.get('email'),
                        'Religion':kw.get('Religion'),
                        'Marital_status':kw.get('Marital_status'),
                        'Home_address':kw.get('Home_address'),
                        'Occupation':kw.get('Occupation'),
                        'Father_name':kw.get('Father_name'),
                        'Fphone':kw.get('Fphone'),
                    })

            return request.redirect("/tenants")
        

    #delete record
    @http.route(['/delete/<model("training.tenants"):s>'], type='http', auth="public", website=True)
    def delete(self, s=None):
        print(s)
        s.unlink()
        print("record deleted")
        return request.redirect('/tenants')


    #owner detail view
    @http.route('/owner',auth="public",website=True)
    def owner_details(self, **kw):
        owner_details = request.env['training.owner'].sudo().search([])
        return request.render('rms.owner_webview',{'ownerdetails':owner_details})


    @http.route(['/form/edit/', '/form/editform/<model("training.owner"):editid>'],auth='public',website=True,csrf=False)
    def createform(self, editid=None):
        owner=None
        #print(editid)
        if editid:
            owner = http.request.env['training.owner'].browse([editid.id])
            #print(owner)
        return http.request.render('rms.owner_form',{'owner' : owner})

    #edit record owner
    @http.route(['/form/submit/','/form/submit/<int:editid>'],type='http',auth="public",website=True,csrf=False, method='post')
    def edit(self,editid=None,**post):
        print("hello",editid)
        if post:
            if editid:
                request.env['training.owner'].browse([editid]).write({
                    'name': post.get('name'),
                    'lastname': post.get('lastname'),
                    'number': post.get('number'),
                    'email': post.get('email'),
                    'address': post.get('address'),
                    'city': post.get('city'),
                    'state': post.get('state')
                    })
            else:
                request.env['training.owner'].create({
                    'name': post.get('name'),
                    'lastname': post.get('lastname'),
                    'number': post.get('number'),
                    'email': post.get('email'),
                    'address': post.get('address'),
                    'city': post.get('city'),
                    'state': post.get('state')
                    })
        return http.request.redirect('/owner')

    @http.route(['/form/delete/<model("training.owner"):s>'],type="http",auth="public",website=True,csrf=False)
    def deleteForm(self,s=None):
        if s:
            s.unlink()
        return http.request.redirect('/owner')