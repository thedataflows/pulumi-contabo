# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

import types

__config__ = pulumi.Config('contabo')


class _ExportableConfig(types.ModuleType):
    @property
    def api(self) -> Optional[str]:
        """
        The api endpoint is https://api.contabo.com.
        """
        return __config__.get('api')

    @property
    def oauth2_client_id(self) -> Optional[str]:
        """
        Your oauth2 client id can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under the
        menu item account secret.
        """
        return __config__.get('oauth2ClientId') or _utilities.get_env('CONTABO_OAUTH2_CLIENT_ID')

    @property
    def oauth2_client_secret(self) -> Optional[str]:
        """
        Your oauth2 client secret can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under
        the menu item account secret.
        """
        return __config__.get('oauth2ClientSecret') or _utilities.get_env('CONTABO_OAUTH2_CLIENT_SECRET')

    @property
    def oauth2_pass(self) -> Optional[str]:
        """
        API Password (this is a new password which you'll set or change in the [Customer Control
        Panel](https://new.contabo.com/account/security) under the menu item account secret.)
        """
        return __config__.get('oauth2Pass') or _utilities.get_env('CONTABO_OAUTH2_PASS')

    @property
    def oauth2_token_url(self) -> Optional[str]:
        """
        The oauth2 token url is https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token.
        """
        return __config__.get('oauth2TokenUrl')

    @property
    def oauth2_user(self) -> Optional[str]:
        """
        API User (your email address to login to the [Customer Control Panel](https://new.contabo.com/account/security) under
        the menu item account secret.
        """
        return __config__.get('oauth2User') or _utilities.get_env('CONTABO_OAUTH2_USER')

