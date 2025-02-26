from adapter.outbound.sql_model.data_base_creator import create_session, OwnedStock
from application.port.outbound.data_updater import DataUpdater


class SqlDataUpdater(DataUpdater):
    def get_current_amount_of_action(self, user_email: str, company_name: str):
        session = create_session()
        record = session.query(OwnedStock).filter_by(customer_email=user_email, company_name=company_name).first()
        if record is None:
            record = 0

        return record.action_amount

    def update_user_data(self, user_email: str, current_amount_of_action: int, company_name: str):
        session = create_session()

        existing_record = session.query(OwnedStock).filter_by(customer_email=user_email, company_name=company_name).first()

        if existing_record:
            existing_record.action_amount = current_amount_of_action
            session.commit()

        else:
            new_stock = OwnedStock(customer_email=user_email, company_name=company_name, action_amount=current_amount_of_action)
            session.add(new_stock)
            session.commit()

        session.close()
