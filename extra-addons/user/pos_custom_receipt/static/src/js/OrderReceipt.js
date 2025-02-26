/** @odoo-module */

import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";

import { usePos } from "@point_of_sale/app/store/pos_hook";
import { patch } from "@web/core/utils/patch";
import {onMounted} from "@odoo/owl";

patch(OrderReceipt.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
    },

    get config(){
    	return this.pos.config;
    },

  	get order() {
  		return this.pos.get_order();
	},

	get orderlines() {
  		return this.pos.get_order().get_orderlines();
	},

	get partner() {
		return this.pos.get_order().get_partner();
	},
	
	
});

