from magnit_web import database as db
from magnit_web.magnitshop import MagnitShop

if __name__ == '__main__':
    shop = MagnitShop()
    session = db.start_session

    products_temp = []
    for i in shop.get_promo_urls():

        print(i)

        products_temp.append(i)
        if len(products_temp) == 5:

            print(products_temp)

            # database.Promo.create_all(session, url=[lambda x: x, products_temp])
            session.add_all([db.Promo(url=i) for i in products_temp])
            session.commit()
            products_temp = []
