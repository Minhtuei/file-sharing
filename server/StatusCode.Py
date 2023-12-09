class StatusCode():
    def __init__(self):
        self.LOGIN_SUCCESS_CODE = 200
        self.REGISTER_SUCCESS_CODE = 201
        self.UPLOAD_SUCCESS_CODE = 202
        self.PING_CODE = 203
        self.FETCH_SUCCESS_CODE = 204
        self.BAD_REQUEST_CODE = 400
        self.USER_NOT_FOUND_CODE = 401
        self.WRONG_PASSWORD_CODE = 402
        self.USER_ALREADY_EXISTS_CODE = 403
        self.STOP_CODE = 404
        self.FILE_NOT_FOUND_CODE = 405

    def LOGIN_SUCCESS(self):
        return str(self.LOGIN_SUCCESS_CODE)
    def REGISTER_SUCCESS(self):
        return str(self.REGISTER_SUCCESS_CODE)
    def BAD_REQUEST(self):
        return str(self.BAD_REQUEST_CODE)
    def USER_NOT_FOUND(self):
        return str(self.USER_NOT_FOUND_CODE)
    def WRONG_PASSWORD(self):
        return str(self.WRONG_PASSWORD_CODE)
    def USER_ALREADY_EXISTS(self):
        return str(self.USER_ALREADY_EXISTS_CODE)
    def UPLOAD_SUCCESS(self):
        return str(self.UPLOAD_SUCCESS_CODE)
    def FETCH_SUCCESS(self):
        return str(self.FETCH_SUCCESS_CODE)
    def PING(self):
        return str(self.PING_CODE)
    def FILE_NOT_FOUND(self):
        return str(self.FILE_NOT_FOUND_CODE)
    def STOP(self):
        return str(self.STOP_CODE)
