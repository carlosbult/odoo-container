/** @odoo-module */

import { Order, Orderline, Payment } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(Order.prototype, {

	export_for_printing() {
        const json = super.export_for_printing(...arguments);
        if (json) {
        	let headerdata = json.headerData;
        	headerdata['config'] = this.pos.config || '';
        	headerdata['pos'] = this.pos || '';
            headerdata['order'] = this || '';
            headerdata['partner'] = this.get_partner() || false;
            headerdata['date'] = json.date ;

        	json.headerData = headerdata;
        }
        return json;
    },

    value_in_other_currency(val){
        let self = this;
        let rate_company = this.pos.config.rate_company;
        let show_currency_rate = this.pos.config.show_currency_rate;
        let price = val;
        let price_other_currency  = price * show_currency_rate || 0;
        return price_other_currency;
    },
   
});



