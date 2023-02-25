// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

// The api endpoint is https://api.contabo.com.
func GetApi(ctx *pulumi.Context) string {
	return config.Get(ctx, "contabo:api")
}

// Your oauth2 client id can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under the
// menu item account secret.
func GetOauth2ClientId(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "contabo:oauth2ClientId")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "CONTABO_OAUTH2_CLIENT_ID").(string)
}

// Your oauth2 client secret can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under
// the menu item account secret.
func GetOauth2ClientSecret(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "contabo:oauth2ClientSecret")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "CONTABO_OAUTH2_CLIENT_SECRET").(string)
}

// API Password (this is a new password which you'll set or change in the [Customer Control
// Panel](https://new.contabo.com/account/security) under the menu item account secret.)
func GetOauth2Pass(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "contabo:oauth2Pass")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "CONTABO_OAUTH2_PASS").(string)
}

// The oauth2 token url is https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token.
func GetOauth2TokenUrl(ctx *pulumi.Context) string {
	return config.Get(ctx, "contabo:oauth2TokenUrl")
}

// API User (your email address to login to the [Customer Control Panel](https://new.contabo.com/account/security) under
// the menu item account secret.
func GetOauth2User(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "contabo:oauth2User")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "CONTABO_OAUTH2_USER").(string)
}