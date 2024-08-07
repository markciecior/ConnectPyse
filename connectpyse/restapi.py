# -*- encoding: utf-8 -*-
#
# THE RESTAPI GENERIC CLIENT CONSUMER
# Author: Sergio Berlotto <sergio.berlotto@gmail.com>
#

# Project died, so updates made by me: Joshua M Smith <saether@gmail.com>


import requests as req
import json


class EndpointError(AttributeError):

    def __init__(self, endpoint):

        message = "Call Error: endpoint '{}' not allowed.".format(
            endpoint
        )
        super(EndpointError, self).__init__(message)


class ApiError(Exception):

    def __init__(self, method, route, status_code, server_message):

        message = """{method} {route} Return code: {status_code}\n
Server message:{server_message}""".format(**locals())
        super(ApiError, self).__init__(message)


class Client(object):

    def __init__(self, root_path):
        self.root_path = root_path
        self.known_endpoints = []

    def __getattribute__(self, attr):

        try:
            return super(Client, self).__getattribute__(attr)
        except AttributeError:
            return Endpoint(
                self.root_path,
                attr,
                ensure_ascii=self.ensure_ascii
            )


class Endpoint(object):

    def __init__(self, root_path, endpoint, ensure_ascii):
        self.endpoint = endpoint
        self.root_path = root_path
        self.ensure_ascii = ensure_ascii

    def _url(self, path, *args):
        url = "{}/{}/".format(self.root_path, path)
        if args:
            url += "/".join([str(a) for a in args])
        return url

    def _headers(self, others={}, setContentType=True):
        """Return the default headers and others as necessary"""
        headers = {}
        if setContentType:
            headers = {
                'Content-Type': 'application/json'
            }

        for p in others.keys():
            headers[p] = others[p]
        return headers

    def _params(self, others={}):
        params = {}
        for p in others.keys():
            params[p] = others[p]
        return params

    def _formatreturn(self, resp):
        try:
            r = resp.json()
        except ValueError:
            #When the return is not a JSON
            r = resp.text
        return r

    def post(self, user_data, the_id=None, user_params={}, user_headers={}, files=None):

        if the_id:
            url = self._url(self.endpoint, the_id)
        else:
            url = self._url(self.endpoint)

        if user_data:
            strjsondata = json.dumps(user_data, ensure_ascii=self.ensure_ascii)
            resp = req.post(
                url,
                data=strjsondata,
                headers=self._headers(user_headers),
                params=self._params(user_params),
                stream=False
            )
        else:
            resp = req.post(
                url,
                files=files,
                headers=self._headers(user_headers, setContentType=False),
                params=self._params(user_params),
                stream=False
            )

        if resp.status_code != 201:
            raise ApiError(
                "POST",
                self.endpoint,
                resp.status_code,
                resp.text)
        else:
            return self._formatreturn(resp)

    def put(self, the_id, user_data, user_params={}, user_headers={}):

        strjsondata = json.dumps(user_data, ensure_ascii=self.ensure_ascii)

        resp = req.put(
            self._url(self.endpoint, the_id),
            data=strjsondata,
            headers=self._headers(user_headers),
            params=self._params(user_params)
        )

        if resp.status_code != 200:
            raise ApiError(
                "PUT",
                self.endpoint,
                resp.status_code,
                resp.text)
        else:
            return self._formatreturn(resp)

    def patch(self, the_id, user_data, user_params={}, user_headers={}):

        strjsondata = json.dumps(user_data, ensure_ascii=self.ensure_ascii)

        resp = req.patch(
            self._url(self.endpoint, the_id),
            data=strjsondata,
            headers=self._headers(user_headers),
            params=self._params(user_params)
        )

        if resp.status_code != 200:
            raise ApiError(
                "PATCH",
                self.endpoint,
                resp.status_code,
                resp.text)
        else:
            return self._formatreturn(resp)

    def get(self, the_id=None, level=None, user_params={}, user_headers={}):

        if the_id:
            url = self._url(self.endpoint, the_id)
        else:
            url = self._url(self.endpoint)

        resp = req.get(
            url,
            headers=self._headers(user_headers),
            params=self._params(user_params)
        )

        if resp.status_code != 200:
            raise ApiError(
                "GET",
                self.endpoint,
                resp.status_code,
                resp.text)
        else:
            return self._formatreturn(resp)

    def delete(self, the_id=None, level=None, user_params={}, user_headers={}):

        if the_id:
            url = self._url(self.endpoint, the_id)
        else:
            url = self._url(self.endpoint)

        resp = req.delete(
            url,
            headers=self._headers(user_headers),
            params=self._params(user_params)
        )

        if resp.status_code != 204:
            raise ApiError(
                "DELETE",
                self.endpoint,
                resp.status_code,
                resp.text)
        else:
            return self._formatreturn(resp)
