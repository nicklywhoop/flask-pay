"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app, api
from application.ressources import bill, client, currency, invoice, ledger, payout, rate, session, settlement, subscription, token

api.add_resource(bill.BillHandler, '/bills', '/bills/<string:bill_id>', '/bills/<string:bill_id>/deliveries')
api.add_resource(bill.BillDeliveryHandler, '/bills/<string:bill_id>/deliveries')
api.add_resource(client.ClientHandler, '/clients', '/clients/<string:key_id>')
api.add_resource(currency.CurrencyHandler, '/currencies')
api.add_resource(invoice.InvoiceHandler, '/invoices', '/invoices/<string:invoice_id>')
api.add_resource(invoice.InvoiceEventHandler, '/invoices/<string:invoice_id>/events')
api.add_resource(invoice.InvoiceRefundHandler,'/invoices/<string:invoice_id>/refunds', '/invoices/<string:invoice_id>/refunds/<string:request_id>')
api.add_resource(invoice.InvoiceNotificationHandler, '/invoices/<string:invoice_id>/notifications')
api.add_resource(ledger.LedgerHandler, '/ledgers/<string:currency>', '/ledgers')
api.add_resource(payout.PayoutHandler, '/payouts', '/payouts/<string:payout_id>')
api.add_resource(rate.RateHandler, '/rates', '/rates/<string:base_currency>', '/rates/<string:base_currency>/<string:currency>')
api.add_resource(session.SessionHandler, '/sessions')
api.add_resource(settlement.SettlementHandler, '/settlements', '/settlements/<string:settlement_id>')
api.add_resource(settlement.SettlementReconciliationHandler, '/settlements/<string:settlement_id>/reconciliationReport')
api.add_resource(subscription.SubscriptionHandler, '/subscriptions', '/subscriptions/<string:subscription_id>')
api.add_resource(token.TokenHandler, '/tokens')

from flask import jsonify
# Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({}), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return jsonify({}), 500
