from flask import request


def controller():
    return request.form['foodItem']