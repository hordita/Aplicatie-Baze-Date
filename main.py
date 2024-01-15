from tkinter import *
from tkinter import ttk, scrolledtext
from tkcalendar import DateEntry
import tkinter.messagebox
import cx_Oracle
from datetime import datetime

root = tkinter.Tk()
root.title('eCOMERT')

root.geometry("435x360")
photo = tkinter.PhotoImage(file='sigla.png')
root.wm_iconphoto(False, photo)

frame = tkinter.Frame(root)

frame.place(relx=0.2, rely=0.2, relheight=0.8, relwidth=0.8)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


class OracleDB:
    def __init__(self, username, password, dsn_tns):
        self.conn = cx_Oracle.connect(username, password, dsn_tns)
        self.cursor = self.conn.cursor()


    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

    def begin_transaction(self):
        self.conn.begin()

    def fetch_all(self):
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()


class ClientiManager:
    def __init__(self, db):
        self.db = db

    def insert_client(self, nume, adresa, email, telefon):
        query = "INSERT INTO clienti (id_client, nume_client, adresa, email, telefon) VALUES (clienti_id_client_seq.nextval, :1, :2, :3, :4)"
        params = (nume, adresa, email, telefon)
        self.db.execute_query(query, params)
        self.db.commit()

    def get_clients(self):
        query = "SELECT * FROM clienti"
        self.db.execute_query(query)
        return self.db.fetch_all()

    def delete_client(self, id_client):
        query = "DELETE FROM clienti WHERE id_client = :1"
        params = (id_client,)
        self.db.execute_query(query, params)
        self.db.commit()

    def update_client(self, id_client, nume, adresa, email, telefon):
        query = "UPDATE clienti SET nume_client = :1, adresa = :2, email = :3, telefon = :4 WHERE id_client = :5"
        params = (nume, adresa, email, telefon, id_client)
        self.db.execute_query(query, params)
        self.db.commit()


#def show_clients():
 #   clients = clienti_manager.get_clients()
  #  message = "\n".join([f"{client[0]}){client[1]} - {client[2]} - {client[3]} - {client[4]}" for client in clients])
   # tkinter.messagebox.showinfo("Lista de clienti", message)

def show_clients():
    clients = clienti_manager.get_clients()

    display_window = tkinter.Tk()
    display_window.title("Lista de clienți")
    scroll_text = scrolledtext.ScrolledText(display_window, width=40, height=10, wrap=tkinter.WORD)
    scroll_text.pack(expand=True, fill='both')

    message = "\n".join([f"{client[0]}) {client[1]} - {client[2]} - {client[3]} - {client[4]}" for client in clients])
    scroll_text.insert(tkinter.END, message)

    display_window.mainloop()


def insert_client():
    nume = entry_nume.get()
    adresa = entry_adresa.get()
    email = entry_email.get()
    telefon = entry_telefon.get()
    try:
        if nume and adresa and telefon:
            clienti_manager.insert_client(nume, adresa, email, telefon)
            tkinter.messagebox.showinfo("Inserare reusita", "Clientul a fost adaugat cu succes!")
        else:
            tkinter.messagebox.showerror("Eroare", "Nume, adresa si telefon sunt obligatorii!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")


def delete_client():
    id_client = entry_id_client.get()
    try:
        if id_client:
            clienti_manager.delete_client(id_client)
            tkinter.messagebox.showinfo("stergere reusita", f"Clientul cu ID-ul {id_client} a fost sters cu succes!")
            show_clients()
        else:
            tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul clientului pentru stergere!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")


def update_client():
    id_client = entry_id_client.get()
    nume = entry_nume.get()
    adresa = entry_adresa.get()
    email = entry_email.get()
    telefon = entry_telefon.get()
    if id_client and nume and adresa and telefon:
        clienti_manager.update_client(id_client, nume, adresa, email, telefon)
        tkinter.messagebox.showinfo("Actualizare reusita",
                                    f"Informatiile pentru clientul cu ID-ul {id_client} au fost actualizate cu succes!")
        show_clients()
    else:
        tkinter.messagebox.showerror("Eroare", "ID Client, Nume, Adresa si Telefon sunt obligatorii!")


def get_client_list():
    query = "SELECT id_client FROM clienti"
    db.execute_query(query)
    clients = [str(client[0]) for client in db.fetch_all()]
    return clients


#############################
class ProduseManager:
    def __init__(self, db):
        self.db = db

    def insert_product(self, nume, descriere, pret, stoc_disponibil):
        query = "INSERT INTO produse (id_produs, nume_produs, descriere, pret, stoc_disponibil) VALUES (produse_id_produs_seq.nextval, :1, :2, :3, :4)"
        params = (nume, descriere, pret, stoc_disponibil)
        self.db.execute_query(query, params)
        self.db.commit()

    def get_products(self):
        query = "SELECT * FROM produse"
        self.db.execute_query(query)
        return self.db.fetch_all()

    def delete_product(self, id_produs):
        query = "DELETE FROM produse WHERE id_produs = :1"
        params = (id_produs,)
        self.db.execute_query(query, params)
        self.db.commit()

    def update_product(self, id_produs, nume, descriere, pret, stoc_disponibil):
        query = "UPDATE produse SET nume_produs = :1, descriere = :2, pret = :3, stoc_disponibil = :4 WHERE id_produs = :5"
        params = (nume, descriere, pret, stoc_disponibil, id_produs)
        self.db.execute_query(query, params)
        self.db.commit()


def show_products():
    products = produse_manager.get_products()
    message = "\n".join(
        [f"{product[0]}){product[1]} - {product[2]} - {product[3]}lei - {product[4]}buc." for product in products])
    tkinter.messagebox.showinfo("Lista de produse", message)


def insert_product():
    nume = entry_nume_produs.get()
    descriere = entry_descriere_produs.get()
    pret = entry_pret_produs.get()
    stoc_disponibil = entry_stoc_disponibil_produs.get()

    if nume and pret and stoc_disponibil:
        produse_manager.insert_product(nume, descriere, pret, stoc_disponibil)
        tkinter.messagebox.showinfo("Inserare reusita", "Produsul a fost adaugat cu succes!")
    else:
        tkinter.messagebox.showerror("Eroare", "Nume, pret si stoc disponibil sunt obligatorii!")


def delete_product():
    id_produs = entry_id_produs.get()
    try:
        if id_produs:
            produse_manager.delete_product(id_produs)
            tkinter.messagebox.showinfo("Stergere reusita", "Produsul a fost sters cu succes!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")


def update_product():
    id_produs = entry_id_produs.get()
    nume = entry_nume_produs.get()
    descriere = entry_descriere_produs.get()
    pret = entry_pret_produs.get()
    stoc_disponibil = entry_stoc_disponibil_produs.get()

    if id_produs and nume and pret and stoc_disponibil:
        produse_manager.update_product(id_produs, nume, descriere, pret, stoc_disponibil)
        tkinter.messagebox.showinfo("Actualizare reusita", "Datele produsului au fost actualizate cu succes!")


###############################
class IstoricPretManager:
    def __init__(self, db):
        self.db = db

    def insert_price_history(self, id_produs, pret_vechi, pret_nou, data_schimbare):
        query = "INSERT INTO istoric_pret (id_pret, id_produs, pret_vechi, pret_nou, data_schimbare) VALUES (istoric_pret_id_pret_seq.nextval, :1, :2, :3, :4)"
        params = (id_produs, pret_vechi, pret_nou, data_schimbare)
        self.db.execute_query(query, params)
        self.db.commit()

    def get_price_history(self, id_produs):
        query = "SELECT * FROM istoric_pret WHERE id_produs = :1"
        params = (id_produs,)
        self.db.execute_query(query, params)
        return self.db.fetch_all()

    def delete_price_history(self, id_istoric_pret):
        query = "DELETE FROM istoric_pret WHERE id_pret = :1"
        params = (id_istoric_pret,)
        self.db.execute_query(query, params)
        self.db.commit()

    def update_price_history(self, id_istoric_pret, id_produs, pret_vechi, pret_nou, data_schimbare):
        query = "UPDATE istoric_pret SET id_produs = :1, pret_vechi = :2, pret_nou = :3, data_schimbare = :4 WHERE id_pret = :5"
        params = (id_produs, pret_vechi, pret_nou, data_schimbare, id_istoric_pret)
        self.db.execute_query(query, params)
        self.db.commit()


def show_price_history():
    id_produs = entry_id_produs.get()
    if id_produs:
        price_history = istoric_pret_manager.get_price_history(id_produs)
        if price_history:
            message = "\n".join(
                [f"{price[0]})p.V->{price[1]} p.N->{price[2]} - {price[3]} ID.Produs {price[4]}" for price in
                 price_history])
            tkinter.messagebox.showinfo("Istoric de preturi",
                                        f"Istoric de preturi pentru produsul cu ID-ul {id_produs}:\n{message}")
        else:
            tkinter.messagebox.showinfo("Istoric de preturi",
                                        f"Niciun istoric de preturi gasit pentru produsul cu ID-ul {id_produs}")
    else:
        tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul produsului pentru afisarea istoricului de preturi!")


def insert_price_history():
    id_produs = entry_id_produs_istoric.get()
    pret_vechi = entry_pret_vechi.get()
    pret_nou = entry_pret_nou.get()
    data_schimbare = entry_data_schimbare.get_date()
    data_schimbare = datetime.strftime(data_schimbare, '%d-%b-%Y')
    try:
        if id_produs and pret_vechi and pret_nou and data_schimbare:
            istoric_pret_manager.insert_price_history(id_produs, pret_vechi, pret_nou, data_schimbare)
            tkinter.messagebox.showinfo("Inserare reusita", "Istoricul de pret a fost adaugat cu succes!")
        else:
            tkinter.messagebox.showerror("Eroare", "ID Produs, Pret Vechi, Pret Nou si Data Schimbarii sunt obligatorii!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")

def delete_price_history():
    id_istoric_pret = entry_id_istoric_pret.get()
    try:
        if id_istoric_pret:
            istoric_pret_manager.delete_price_history(id_istoric_pret)
            tkinter.messagebox.showinfo("Stergere reusita", "Istoricul de pret a fost sters cu succes!")
        else:
            tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul istoricului de pret pentru stergere!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")


def update_price_history():
    id_istoric_pret = entry_id_istoric_pret.get()
    id_produs = entry_id_produs_istoric.get()
    pret_vechi = entry_pret_vechi.get()
    pret_nou = entry_pret_nou.get()
    data_schimbare = entry_data_schimbare.get_date()
    data_schimbare = datetime.strftime(data_schimbare, '%d-%b-%Y')

    if id_istoric_pret and id_produs and pret_vechi and pret_nou and data_schimbare:
        istoric_pret_manager.update_price_history(id_istoric_pret, id_produs, pret_vechi, pret_nou, data_schimbare)
        tkinter.messagebox.showinfo("Actualizare reusita", "Istoricul de pret a fost actualizat cu succes!")
    else:
        tkinter.messagebox.showerror("Eroare", "Completati toate câmpurile pentru actualizare!")


def get_product_list():
    query = "SELECT id_produs FROM produse"
    db.execute_query(query)
    products = [str(product[0]) for product in db.fetch_all()]
    return products


###################################
class RecenziiManager:
    def __init__(self, db):
        self.db = db

    def insert_review(self, id_produs, id_client, comentariu):
        query = "INSERT INTO recenzii (id_recenzie, id_produs, id_client, comentariu) VALUES (recenzii_id_recenzie_seq.nextval, :1, :2, :3)"
        params = (id_produs, id_client, comentariu)
        self.db.execute_query(query, params)
        self.db.commit()

    def get_reviews(self, id_produs):
        query = "SELECT * FROM recenzii WHERE id_produs = :1"
        params = (id_produs,)
        self.db.execute_query(query, params)
        return self.db.fetch_all()

    def update_review(self, id_recenzie, comentariu):
        query = "UPDATE recenzii SET comentariu = :1 WHERE id_recenzie = :2"
        params = (comentariu, id_recenzie)
        self.db.execute_query(query, params)
        self.db.commit()

    def delete_review(self, id_recenzie):
        query = "DELETE FROM recenzii WHERE id_recenzie = :1"
        params = (id_recenzie,)
        self.db.execute_query(query, params)
        self.db.commit()


def show_reviews():
    id_produs = entry_id_produs_recenzie.get()
    if id_produs:
        reviews = recenzii_manager.get_reviews(id_produs)
        if reviews:
            message = "\n".join(
                [f"{review[0]}){review[1]}| ID.Clie->{review[2]} ID.Prod->{review[3]}" for review in reviews])
            tkinter.messagebox.showinfo("Lista de recenzii",
                                        f"Recenzii pentru produsul cu ID-ul {id_produs}:\n{message}")
        else:
            tkinter.messagebox.showinfo("Lista de recenzii",
                                        f"Nicio recenzie gasita pentru produsul cu ID-ul {id_produs}")
    else:
        tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul produsului pentru afisarea recenziilor!")


def insert_review():
    id_produs = entry_id_produs_recenzie.get()
    id_client = entry_id_client_recenzie.get()
    comentariu = entry_comentariu_recenzie.get()
    try:
        if id_produs and id_client and comentariu:
            recenzii_manager.insert_review(id_produs, id_client, comentariu)
            tkinter.messagebox.showinfo("Inserare reusita", "Recenzia a fost adaugata cu succes!")
        else:
            tkinter.messagebox.showerror("Eroare", "ID Produs, Nota si Comentariu sunt obligatorii!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")


def update_review():
    id_recenzie = entry_id_recenzie.get()
    comentariu_nou = entry_comentariu_recenzie.get()

    if id_recenzie and comentariu_nou:
        recenzii_manager.update_review(id_recenzie, comentariu_nou)
        tkinter.messagebox.showinfo("Actualizare reusita", "Recenzia a fost actualizata cu succes!")
    else:
        tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul recenziei si noul comentariu!")


def delete_review():
    id_recenzie = entry_id_recenzie.get()
    if id_recenzie:
        recenzii_manager.delete_review(id_recenzie)
        tkinter.messagebox.showinfo("stergere reusita", "Recenzia a fost stearsa cu succes!")
    else:
        tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul recenziei pentru stergere!")


#############################
class ComenziManager:
    def __init__(self, db):
        self.db = db

    def insert_order(self, id_client, data, pret):
        query = "INSERT INTO comenzi (id_comanda, id_client, data_comanda, total_plata) VALUES (comenzi_id_comanda_seq.nextval, :1, :2, :3)"
        params = (id_client, data, pret)
        self.db.execute_query(query, params)
        self.db.commit()

    def get_orders(self, id_client):
        query = "SELECT * FROM comenzi WHERE id_client = :1"
        params = (id_client,)
        self.db.execute_query(query, params)
        return self.db.fetch_all()

    def update_order(self, id_comanda, new_data, new_pret):
        query = "UPDATE comenzi SET data_comanda = :1, total_plata = :2 WHERE id_comanda = :3"
        params = (new_data, new_pret, id_comanda)
        self.db.execute_query(query, params)
        self.db.commit()

    def delete_order(self, id_comanda):
        query = "DELETE FROM comenzi WHERE id_comanda = :1"
        params = (id_comanda,)
        self.db.execute_query(query, params)
        self.db.commit()


def show_orders():
    id_client = entry_id_client_comanda.get()
    if id_client:
        orders = comenzi_manager.get_orders(id_client)
        if orders:
            message = "\n".join([f"{order[0]})Data->{order[1]} - {order[2]}lei ID_CLIE.{order[3]}" for order in orders])
            tkinter.messagebox.showinfo("Lista de comenzi", f"Comenzi pentru clientul cu ID-ul {id_client}:\n{message}")
        else:
            tkinter.messagebox.showinfo("Lista de comenzi",
                                        f"Nicio comanda gasita pentru clientul cu ID-ul {id_client}")
    else:
        tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul clientului pentru afisarea comenzilor!")


def insert_order():
    id_client = entry_id_client_comanda.get()
    data = entry_data_comanda.get_date()
    data = datetime.strftime(data, '%d-%b-%Y')
    pret = entry_pret_comanda.get()
    try:
        if id_client and data and pret:
            comenzi_manager.insert_order(id_client, data, pret)
            tkinter.messagebox.showinfo("Inserare reusita", "Comanda a fost adaugata cu succes!")
        else:
            tkinter.messagebox.showerror("Eroare", "ID Client, ID Produs si Cantitate sunt obligatorii!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")


def update_order():
    id_comanda = entry_id_comanda.get()
    new_data = entry_data_comanda.get_date()
    new_data = datetime.strftime(new_data, '%d-%b-%Y')
    new_pret = entry_pret_comanda.get()

    if id_comanda and new_data and new_pret:
        comenzi_manager.update_order(id_comanda, new_data, new_pret)
        tkinter.messagebox.showinfo("Actualizare reusita", "Comanda a fost actualizata cu succes!")
    else:
        tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul comenzii, noua data si noul total de plata!")


def delete_order():
    id_comanda = entry_id_comanda.get()
    try:
        if id_comanda:
            comenzi_manager.delete_order(id_comanda)
            tkinter.messagebox.showinfo("Stergere reusita", "Comanda a fost stearsa cu succes!")
        else:
            tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul comenzii pentru stergere!")
    except Exception as e:
        tkinter.messagebox.showwarning("Atentie", f"NU RESPECTA CONSTRANGERILE: {str(e)}")


def get_order_list():
    query = "SELECT id_comanda FROM comenzi"
    db.execute_query(query)
    orders = [str(order[0]) for order in db.fetch_all()]
    return orders


###########################################

class DetaliiComandaManager:
    def __init__(self, db):
        self.db = db

    def insert_order_detail(self, id_comanda, id_produs, cantitate):

        self.db.begin_transaction()

        try:
            query_stoc = "SELECT stoc_disponibil FROM produse WHERE id_produs = :1"
            params_stoc = (id_produs,)
            self.db.execute_query(query_stoc, params_stoc)
            stoc_disponibil = self.db.fetch_all()[0][0]

            if int(stoc_disponibil) < int(cantitate):
                tkinter.messagebox.showerror("Tranzactie esuata", "Nu exista suficiente produse In stoc!")
                return

            query_insert = "INSERT INTO detalii_comanda (comenzi_id_comanda, produse_id_produs, cantitate) VALUES (:1, :2, :3)"
            params_insert = (id_comanda, id_produs, cantitate)
            self.db.execute_query(query_insert, params_insert)

            query_update_stoc = "UPDATE produse SET stoc_disponibil = stoc_disponibil - :1 WHERE id_produs = :2"
            params_update_stoc = (cantitate, id_produs)
            self.db.execute_query(query_update_stoc, params_update_stoc)
            self.db.commit()
            tkinter.messagebox.showinfo("Succes", "Produsul a fost adaugat cu succes!")

        except Exception as e:
            self.db.rollback()
            tkinter.messagebox.showerror("Tranzactie esuata", f"A aparut o eroare neprevazuta:{str(e)}")

    def get_order_details(self, id_comanda):
        query = "SELECT * FROM detalii_comanda WHERE comenzi_id_comanda = :1"
        params = (id_comanda,)
        self.db.execute_query(query, params)
        return self.db.fetch_all()

    def delete_order_detail(self, id_comanda, id_produs):

        self.db.begin_transaction()
        try:

            query_existence = "SELECT * FROM detalii_comanda WHERE comenzi_id_comanda = :1 AND produse_id_produs = :2"
            params_existence = (id_comanda, id_produs)
            self.db.execute_query(query_existence, params_existence)
            existing_detail = self.db.fetch_all()

            if not existing_detail:
                tkinter.messagebox.showerror("Eroare", "In aceasta comanda nu exista produsul selectat!")
                return

            query_get_quantity = "SELECT cantitate FROM detalii_comanda WHERE comenzi_id_comanda = :1 AND produse_id_produs = :2"
            params_get_quantity = (id_comanda, id_produs)
            self.db.execute_query(query_get_quantity, params_get_quantity)
            quantity_to_return = self.db.fetch_all()[0][0]

            query_delete = "DELETE FROM detalii_comanda WHERE comenzi_id_comanda = :1 AND produse_id_produs = :2"
            params_delete = (id_comanda, id_produs)
            self.db.execute_query(query_delete, params_delete)

            query_update_stock = "UPDATE produse SET stoc_disponibil = stoc_disponibil + :1 WHERE id_produs = :2"
            params_update_stock = (quantity_to_return, id_produs)
            self.db.execute_query(query_update_stock, params_update_stock)
            self.db.commit()
            tkinter.messagebox.showinfo("Succes", "Produsul selectat a fost sters cu succes, iar stocul a fost "
                                                  "actualizat!")
        except Exception as e:
            self.db.rollback()
            tkinter.messagebox.showerror("Eroare", f"Eroare la stergerea produsului: {str(e)}")


def show_order_details():
    id_comanda = entry_id_comanda_detalii.get()
    if id_comanda:
        order_details = detalii_comanda_manager.get_order_details(id_comanda)
        if order_details:
            message = "\n".join(
                [f"id_produs->{detail[0]} id_comanda->{detail[1]} cantitate->{detail[2]}" for detail in order_details])
            print(message)
            tkinter.messagebox.showinfo("Detalii comanda", f"Detalii pentru comanda cu ID-ul {id_comanda}:\n{message}")
        else:
            tkinter.messagebox.showinfo("Detalii comanda",
                                        f"Nicio detaliu de comanda gasit pentru comanda cu ID-ul {id_comanda}")
    else:
        tkinter.messagebox.showerror("Eroare", "Introduceti ID-ul comenzii pentru afisarea detaliilor de comanda!")


def delete_order_detail():
    id_comanda = entry_id_comanda_detalii.get()
    id_produs = entry_id_produs_detalii.get()

    if id_comanda and id_produs:
        detalii_comanda_manager.delete_order_detail(id_comanda, id_produs)
    else:
        tkinter.messagebox.showerror("Eroare", "ID Comanda si ID Produs sunt obligatorii!")


def insert_order_detail():
    id_comanda = entry_id_comanda_detalii.get()
    id_produs = entry_id_produs_detalii.get()
    cantitate = entry_cantitate_detalii.get()

    if id_comanda and id_produs and cantitate:
        detalii_comanda_manager.insert_order_detail(id_comanda, id_produs, cantitate)
    else:
        tkinter.messagebox.showerror("Eroare", "ID Comanda, ID Produs si Cantitate sunt obligatorii!")


###################################################
if __name__ == "__main__":

    username = "bd009"
    password = "Hordila1234"
    dsn_tns = cx_Oracle.makedsn('bd-dc.cs.tuiasi.ro', '1539', service_name='orcl')
    db = OracleDB(username, password, dsn_tns)

    clienti_manager = ClientiManager(db)
    produse_manager = ProduseManager(db)
    istoric_pret_manager = IstoricPretManager(db)
    recenzii_manager = RecenziiManager(db)
    comenzi_manager = ComenziManager(db)
    detalii_comanda_manager = DetaliiComandaManager(db)


    def page1():
        global entry_nume, entry_adresa, entry_email, entry_telefon, entry_id_client
        clear_frame(frame)
        Label(frame, text="Nume:").grid(row=0, column=0)
        entry_nume = Entry(frame)
        entry_nume.grid(row=0, column=1)

        Label(frame, text="Adresa:").grid(row=1, column=0)
        entry_adresa = Entry(frame)
        entry_adresa.grid(row=1, column=1)

        Label(frame, text="Email:").grid(row=2, column=0)
        entry_email = Entry(frame)
        entry_email.grid(row=2, column=1)

        Label(frame, text="Telefon:").grid(row=3, column=0)
        entry_telefon = Entry(frame)
        entry_telefon.grid(row=3, column=1)

        btn_insert = Button(frame, text="Adaugare client", command=insert_client)
        btn_insert.grid(row=4, column=0, columnspan=2)

        btn_show_clients = Button(frame, text="Afisare clienti", command=show_clients)
        btn_show_clients.grid(row=5, column=0, columnspan=2)

        Label(frame, text="ID Client:").grid(row=6, column=0)
        entry_id_client = Entry(frame)
        entry_id_client.grid(row=6, column=1)

        btn_delete_client = Button(frame, text="Stergere client", command=delete_client)
        btn_delete_client.grid(row=7, column=0, columnspan=2)

        btn_update_client = Button(frame, text="Actualizare client", command=update_client)
        btn_update_client.grid(row=8, column=0, columnspan=2)


    def page2():
        global entry_nume_produs, entry_descriere_produs, entry_pret_produs, entry_stoc_disponibil_produs, entry_id_produs
        clear_frame(frame)
        Label(frame, text="Nume Produs:").grid(row=0, column=0)
        entry_nume_produs = Entry(frame)
        entry_nume_produs.grid(row=0, column=1)

        Label(frame, text="Descriere:").grid(row=1, column=0)
        entry_descriere_produs = Entry(frame)
        entry_descriere_produs.grid(row=1, column=1)

        Label(frame, text="Pret:").grid(row=2, column=0)
        entry_pret_produs = Entry(frame)
        entry_pret_produs.grid(row=2, column=1)

        Label(frame, text="Stoc Disponibil:").grid(row=3, column=0)
        entry_stoc_disponibil_produs = Entry(frame)
        entry_stoc_disponibil_produs.grid(row=3, column=1)

        btn_insert_produs = Button(frame, text="Adaugare produs", command=insert_product)
        btn_insert_produs.grid(row=4, column=0, columnspan=2)

        btn_show_products = Button(frame, text="Afisare produse", command=show_products)
        btn_show_products.grid(row=5, column=0, columnspan=2)

        Label(frame, text="ID Produs:").grid(row=6, column=0)
        entry_id_produs = Entry(frame)
        entry_id_produs.grid(row=6, column=1)

        btn_delete_produs = Button(frame, text="Stergere produs", command=delete_product)
        btn_delete_produs.grid(row=7, column=0, columnspan=2)

        btn_update_produs = Button(frame, text="Actualizare produs", command=update_product)
        btn_update_produs.grid(row=8, column=0, columnspan=2)


    def page3():
        global entry_id_produs, entry_id_produs_istoric, entry_pret_vechi, entry_pret_nou, entry_id_istoric_pret, entry_data_schimbare
        clear_frame(frame)

        products = get_product_list()

        Label(frame, text="ID Produs:").grid(row=0, column=0)
        entry_id_produs = ttk.Combobox(frame, values=products)
        entry_id_produs.grid(row=0, column=1)

        btn_show_price_history = Button(frame, text="Afisare Istoric", command=show_price_history)
        btn_show_price_history.grid(row=1, column=0, columnspan=2)

        Label(frame, text="ID Produs:").grid(row=2, column=0)
        entry_id_produs_istoric = ttk.Combobox(frame, values=products)
        entry_id_produs_istoric.grid(row=2, column=1)

        Label(frame, text="Pret Vechi:").grid(row=3, column=0)
        entry_pret_vechi = Entry(frame)
        entry_pret_vechi.grid(row=3, column=1)

        Label(frame, text="Pret Nou:").grid(row=4, column=0)
        entry_pret_nou = Entry(frame)
        entry_pret_nou.grid(row=4, column=1)

        Label(frame, text="Data Schimbare:").grid(row=5, column=0)
        #entry_data_schimbare = Entry(frame)
        entry_data_schimbare = DateEntry(frame, width=12, background='darkblue', foreground='white', date_pattern='dd-MM-yyyy',borderwidth=2)
        entry_data_schimbare.grid(row=5, column=1)

        btn_insert_price_history = Button(frame, text="Adaugare Istoric", command=insert_price_history)
        btn_insert_price_history.grid(row=6, column=0, columnspan=2)

        Label(frame, text="ID Istoric Pret:").grid(row=7, column=0)
        entry_id_istoric_pret = Entry(frame)
        entry_id_istoric_pret.grid(row=7, column=1)

        btn_update_price_history = Button(frame, text="Actualizare Istoric", command=update_price_history)
        btn_update_price_history.grid(row=8, column=0, columnspan=2)

        btn_delete_price_history = Button(frame, text="Stergere Istoric", command=delete_price_history)
        btn_delete_price_history.grid(row=9, column=0, columnspan=2)


    def page4():
        clear_frame(frame)
        global entry_id_produs_recenzie, recenzii_manager, entry_id_client_recenzie, entry_id_recenzie, entry_comentariu_recenzie

        products = get_product_list()

        Label(frame, text="ID Produs:").grid(row=6, column=0)
        entry_id_produs_recenzie = ttk.Combobox(frame, values=products)
        entry_id_produs_recenzie.grid(row=6, column=1)

        clients = get_client_list()

        Label(frame, text="ID Client:").grid(row=7, column=0)
        entry_id_client_recenzie = ttk.Combobox(frame, values=clients)
        entry_id_client_recenzie.grid(row=7, column=1)

        Label(frame, text="Comentariu:").grid(row=8, column=0)
        entry_comentariu_recenzie = Entry(frame)
        entry_comentariu_recenzie.grid(row=8, column=1)

        btn_insert_recenzie = Button(frame, text="Adaugare recenzie", command=insert_review)
        btn_insert_recenzie.grid(row=9, column=0, columnspan=2)

        btn_show_reviews = Button(frame, text="Afisare recenzii", command=show_reviews)
        btn_show_reviews.grid(row=10, column=0, columnspan=2)

        Label(frame, text="ID Recenzie:").grid(row=11, column=0)
        entry_id_recenzie = Entry(frame)
        entry_id_recenzie.grid(row=11, column=1)

        btn_update_review = Button(frame, text="Actualizare recenzie", command=update_review)
        btn_update_review.grid(row=12, column=0, columnspan=2)

        btn_delete_review = Button(frame, text="Stergere recenzie", command=delete_review)
        btn_delete_review.grid(row=13, column=0, columnspan=2)


    def page5():
        clear_frame(frame)
        global entry_id_client_comanda, entry_data_comanda, entry_pret_comanda, entry_id_comanda

        clients = get_client_list()

        Label(frame, text="ID Client:").grid(row=0, column=0)
        entry_id_client_comanda = ttk.Combobox(frame, values=clients)
        entry_id_client_comanda.grid(row=0, column=1)

        Label(frame, text="DataComanda:").grid(row=1, column=0)
        entry_data_comanda = DateEntry(frame, width=12, background='darkblue', foreground='white', date_pattern='dd-MM-yyyy',borderwidth=2)
        entry_data_comanda.grid(row=1, column=1)

        Label(frame, text="Pret:").grid(row=2, column=0)
        entry_pret_comanda = Entry(frame)
        entry_pret_comanda.grid(row=2, column=1)

        btn_insert_order = Button(frame, text="Adaugare comanda", command=insert_order)
        btn_insert_order.grid(row=3, column=0, columnspan=2)

        btn_show_orders = Button(frame, text="Afisare comenzi", command=show_orders)
        btn_show_orders.grid(row=4, column=0, columnspan=2)

        orders = get_order_list()

        Label(frame, text="ID Comanda:").grid(row=5, column=0)
        entry_id_comanda = ttk.Combobox(frame, values=orders)
        entry_id_comanda.grid(row=5, column=1)

        btn_update_order = Button(frame, text="Actualizare comanda", command=update_order)
        btn_update_order.grid(row=6, column=0, columnspan=2)

        btn_delete_order = Button(frame, text="stergere comanda", command=delete_order)
        btn_delete_order.grid(row=7, column=0, columnspan=2)


    def page6():
        clear_frame(frame)
        global entry_id_comanda_detalii, entry_id_produs_detalii, entry_cantitate_detalii

        orders = get_order_list()

        Label(frame, text="ID Comanda:").grid(row=0, column=0)
        entry_id_comanda_detalii = ttk.Combobox(frame, values=orders)
        entry_id_comanda_detalii.grid(row=0, column=1)

        products = get_product_list()

        Label(frame, text="ID Produs:").grid(row=1, column=0)
        entry_id_produs_detalii = ttk.Combobox(frame, values=products)
        entry_id_produs_detalii.grid(row=1, column=1)

        Label(frame, text="Cantitate:").grid(row=2, column=0)
        entry_cantitate_detalii = Entry(frame)
        entry_cantitate_detalii.grid(row=2, column=1)

        btn_insert_order_detail = Button(frame, text="Adaugare produse la comanda", command=insert_order_detail)
        btn_insert_order_detail.grid(row=3, column=0, columnspan=2)

        btn_show_order_details = Button(frame, text="Afisare detalii comanda", command=show_order_details)
        btn_show_order_details.grid(row=4, column=0, columnspan=2)

        btn_delete_order_detail = Button(frame, text="Sterge", command=delete_order_detail)
        btn_delete_order_detail.grid(row=5, column=0, columnspan=2)


    bt = tkinter.Button(root, text='CLIENTI', command=page1)
    bt.grid(column=0, row=0)

    bt1 = tkinter.Button(root, text='PRODUSE', command=page2)
    bt1.grid(row=0, column=1)

    bt2 = tkinter.Button(root, text='ISTORIC PRET', command=page3)
    bt2.grid(row=0, column=2)

    bt3 = tkinter.Button(root, text='RECENZI', command=page4)
    bt3.grid(row=0, column=3)

    bt4 = tkinter.Button(root, text='COMENZI', command=page5)
    bt4.grid(row=0, column=4)

    bt5 = tkinter.Button(root, text='DETALII COMANDA', command=page6)
    bt5.grid(row=0, column=5)

    root.mainloop()

    db.close()
