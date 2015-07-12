# -*- coding: utf-8 -*-

import getpass
from line import LineClient

def GetLineAuthToken(username, password):
    return LineClient(username, password).authToken;

username = raw_input("Username: ");
password = getpass.getpass();

print;

authToken = GetLineAuthToken(username, password);

print;

divider = ("-" * len(authToken));

print("authToken:");
print(divider);
print authToken;
print(divider);
