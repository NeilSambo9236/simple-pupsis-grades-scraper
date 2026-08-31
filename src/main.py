from playwright.sync_api import sync_playwright

from scraper import (
    open_browser, 
    input_login_credentials, 
    click_login, 
    click_grades_section,  
    extract_grades_table
)

from transform import to_table


def print_data(df) :
    columns = ["Subject Code", 
               "Description", 
               "Faculty Name", 
               "Sect Code", 
               "Final Grade", 
               "Grade Status"
    ]

    print(f"Necessary records: \n\n{df[columns]}")


def main() :
    with sync_playwright() as pw :
        browser, page = open_browser(pw)

        input_login_credentials(page)
        click_login(page)
        click_grades_section(page)

        page.wait_for_timeout(1000)

        headers, grades_in_list = extract_grades_table(page)

        df = to_table(headers, grades_in_list)
        print_data(df)

        browser.close()


if __name__ == "__main__" : 
    main()