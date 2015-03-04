Employee additional fields [hr_employee_additional_fields]
===========


This module adds additional fields to an employee form

at present these are 
- employee Nr.
- Hukou   ### this influences which kind of social insurance is applicable to an employee in P.R. China ###  
- Join company date 
- Shebao Nr.   ### the social Security in China ###


Installation
============

To install this module, you need to:

 * git clone https://github.com/vrms/odoo_hr_additional_fields.git
 * make it available to odoo by adding its location to the addons_path in 
   /etc/odoo-server.conf

Configuration
=============

To configure this module, you need to:

 * no configuration required

Usage
=====


Known issues / Roadmap
======================

* make the additional fields search and sortable

Credits
=======

Contributors
------------

Laura Jarvenpaa <laura@kapsi.fi>
Gunnar Wagner <vrms@netcologne.de>

Maintainer
----------

This module is maintained by Gunnar Wagner <vrms@netcologne.de>

To contribute to this module, please visit https://github.com/vrms.
