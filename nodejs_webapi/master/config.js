// Update these four variables with values from your B2C tenant in the Azure portal
const clientID = "c291dcba-d18d-420f-95f5-444ad5387f6a"; // Application (client) ID of your API's application registration
const b2cDomainHost = "npsstag.b2clogin.com";
const tenantId = "593d6ba9-6270-486f-8264-f6c354a8ea5f"; // Alternatively, you can use your Directory (tenant) ID (a GUID)
const policyName = "B2C_1_SignUpIn";

const config = {
    identityMetadata: "https://" + b2cDomainHost + "/" + tenantId + "/" + policyName + "/v2.0/.well-known/openid-configuration/",
    clientID: clientID,
    policyName: policyName,
    isB2C: true,
    validateIssuer: false,
    loggingLevel: 'info',
    loggingNoPII: false,
    passReqToCallback: false
}

module.exports = config;