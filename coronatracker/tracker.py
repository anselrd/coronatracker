# -*- coding: utf-8 -*-
from coronatracker.applayout import get_page

if __name__ == '__main__':

    # Lay out the page
    app = get_page()

    # Put it up
    app.run_server(debug=True)
