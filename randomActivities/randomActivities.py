from bt.btInformation import fill_biological_test_form, fill_biological_test_with_multiple_samples
from registration.personnalInformations import fill_random_personnal_infos
from utils import *
from time import sleep
import random


def add_rand_users(max, driver):
    output = []
    for i in range(0, random.randint(1, max)):
        navigate("http://localhost:8080/register.html", driver)
        u = fill_random_personnal_infos(driver)
        click_submit("button[type=submit]", driver)
        output.append(u)
    return output

def add_random_orders(max, users, driver):
    output = []
    for i in range(0, max):

        # -------------
        # LOGIN AS USER
        user = random.choice(users)
        navigate("http://localhost:8080/profile.html", driver)
        set_select_value("#fType", user['type'], driver)
        send_keys("#fUsername", user['username'], driver)
        send_keys("#fPassword", user['password'], driver)
        click_submit("button[type=submit]", driver)

        # -------------
        # FILL FORM
        navigate("http://localhost:8080/order.html", driver)
        order = fill_biological_test_form(0, driver)
        click_submit("button[type=submit]", driver)
        output.append(order)

        # -------------
        # DISCONNECT
        navigate("http://localhost:8080/profile.html", driver)
        navigate_by_text("a", "Logout", driver)
        print()

    return output

def add_random_orders_with_multiple_samples(max, users, driver):
    for i in range(0, max):

        # -------------
        # LOGIN AS USER
        user = random.choice(users)
        navigate("http://localhost:8080/profile.html", driver)
        set_select_value("#fType", user['type'], driver)
        send_keys("#fUsername", user['username'], driver)
        send_keys("#fPassword", user['password'], driver)
        click_submit("button[type=submit]", driver)

        # -------------
        # FILL FORM
        navigate("http://localhost:8080/order.html", driver)
        fill_biological_test_with_multiple_samples(user, driver)
        click_submit("button[type=submit]", driver)

        # -------------
        # DISCONNECT
        navigate("http://localhost:8080/profile.html", driver)
        navigate_by_text("a", "Logout", driver)
    print()
