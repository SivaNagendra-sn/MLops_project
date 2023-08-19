import sys

def error_messgae_details(error, error_detail:sys):

    _,_, exe_tb = error_detail.exc_info()
    filename= exe_tb.tb_frame.f_code.co_filename
    error_mesage = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(filename, exe_tb.tb_line, str(error))
    return error_mesage


class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_messgae_details(error_message, error_detail)

    def __str__(self):
        return self.error_message
    