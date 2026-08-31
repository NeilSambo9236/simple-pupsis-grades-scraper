from config import (
    STUDENT_NUMBER, 
    PASSWORD, 
    BIRTH_MONTH, 
    BIRTH_DAY, 
    BIRTH_YEAR
)


def open_browser(pw) :
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://sis1.pup.edu.ph/student/")

    return browser, page


def input_login_credentials(page) :
    page.locator('input[type="text"]').fill(STUDENT_NUMBER)
    page.locator('input[type="password"]').fill(PASSWORD)

    page.locator('select[name="SelectMonth"]').select_option(label=BIRTH_MONTH)
    page.locator('select[name="SelectDay"]').select_option(label=BIRTH_DAY)
    page.locator('select[name="SelectYear"]').select_option(label=BIRTH_YEAR)


def click_login(page) :
    page.locator('input[type="submit"]').click()


def click_grades_section(page) :
    page.locator('a[href="https://sis1.pup.edu.ph/student/grades"]').click()


def extract_grades_table(page) :
    grades_in_list = []
    number = 0

    while True :
        # Locator for the grades tables
        table = page.locator(f'table[id="DataTables_Table_{number}"]')

        # If there are no tables left, end the table scraping
        if table.count() == 0 :
            break

        # Locator for rows of grades tables
        rows = table.locator('tr[role="row"]')

        # Loops through all the rows of the grades table
        for row in rows.all() :
            # Locates and collects the headers and rows of the grades table
            row = (row.locator('th[data-asw-org-font-size="16"], td[data-asw-org-font-size="16"]').all_text_contents())

            # Puts "no data" as a value if there is no data in a cell
            row = (["No data" if value in ("", " ") else value for value in row])

            grades_in_list.append(row)     

        number += 1

    # Gets the column headers
    headers = grades_in_list[0]
    # Removes the column headers from the data
    grades_in_list = [value for value in grades_in_list[1:] if value != headers]    

    return headers, grades_in_list