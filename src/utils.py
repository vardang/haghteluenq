
def wait_until_page_loaded(wait):
    def page_has_loaded(dr):
        page_state = dr.execute_script(
            'return document.readyState;'
        )
        return page_state == 'complete'

    wait.until(page_has_loaded)


def wait_until_jquery_active(wait):
    def page_has_loaded(dr):
        page_state = dr.execute_script('return jQuery.active;')
        return page_state == 0

    wait.until(page_has_loaded)
