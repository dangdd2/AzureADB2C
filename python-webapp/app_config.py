import os

b2c_tenant = "npsstag"
signupsignin_user_flow = "B2C_1_SignUpIn"
editprofile_user_flow = "B2C_1_ProfileEdit"
resetpassword_user_flow = "B2C_1_ProfileEdit"
authority_template = "https://npsstag.b2clogin.com/npsstag.onmicrosoft.com/{user_flow}"

CLIENT_ID = "c291dcba-d18d-420f-95f5-444ad5387f6a" # Application (client) ID of app registration

CLIENT_SECRET = "6h1Ra~AKTR6gs~Xtp1n.eB.c.07z0w9_hq" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = authority_template.format(
    tenant=b2c_tenant, user_flow=signupsignin_user_flow)
B2C_PROFILE_AUTHORITY = authority_template.format(
    tenant=b2c_tenant, user_flow=editprofile_user_flow)
B2C_RESET_PASSWORD_AUTHORITY = authority_template.format(
    tenant=b2c_tenant, user_flow=resetpassword_user_flow)

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# This is the API resource endpoint
ENDPOINT = '' # Application ID URI of app registration in Azure portal

# These are the scopes you've exposed in the web API app registration in the Azure portal
SCOPE = []  # Example with two exposed scopes: ["demo.read", "demo.write"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
