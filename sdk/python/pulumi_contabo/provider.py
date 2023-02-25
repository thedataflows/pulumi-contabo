# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 api: Optional[pulumi.Input[str]] = None,
                 oauth2_client_id: Optional[pulumi.Input[str]] = None,
                 oauth2_client_secret: Optional[pulumi.Input[str]] = None,
                 oauth2_pass: Optional[pulumi.Input[str]] = None,
                 oauth2_token_url: Optional[pulumi.Input[str]] = None,
                 oauth2_user: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] api: The api endpoint is https://api.contabo.com.
        :param pulumi.Input[str] oauth2_client_id: Your oauth2 client id can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under the
               menu item account secret.
        :param pulumi.Input[str] oauth2_client_secret: Your oauth2 client secret can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under
               the menu item account secret.
        :param pulumi.Input[str] oauth2_pass: API Password (this is a new password which you'll set or change in the [Customer Control
               Panel](https://new.contabo.com/account/security) under the menu item account secret.)
        :param pulumi.Input[str] oauth2_token_url: The oauth2 token url is https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token.
        :param pulumi.Input[str] oauth2_user: API User (your email address to login to the [Customer Control Panel](https://new.contabo.com/account/security) under
               the menu item account secret.
        """
        if api is not None:
            pulumi.set(__self__, "api", api)
        if oauth2_client_id is None:
            oauth2_client_id = _utilities.get_env('CONTABO_OAUTH2_CLIENT_ID')
        if oauth2_client_id is not None:
            pulumi.set(__self__, "oauth2_client_id", oauth2_client_id)
        if oauth2_client_secret is None:
            oauth2_client_secret = _utilities.get_env('CONTABO_OAUTH2_CLIENT_SECRET')
        if oauth2_client_secret is not None:
            pulumi.set(__self__, "oauth2_client_secret", oauth2_client_secret)
        if oauth2_pass is None:
            oauth2_pass = _utilities.get_env('CONTABO_OAUTH2_PASS')
        if oauth2_pass is not None:
            pulumi.set(__self__, "oauth2_pass", oauth2_pass)
        if oauth2_token_url is not None:
            pulumi.set(__self__, "oauth2_token_url", oauth2_token_url)
        if oauth2_user is None:
            oauth2_user = _utilities.get_env('CONTABO_OAUTH2_USER')
        if oauth2_user is not None:
            pulumi.set(__self__, "oauth2_user", oauth2_user)

    @property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input[str]]:
        """
        The api endpoint is https://api.contabo.com.
        """
        return pulumi.get(self, "api")

    @api.setter
    def api(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api", value)

    @property
    @pulumi.getter(name="oauth2ClientId")
    def oauth2_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        Your oauth2 client id can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under the
        menu item account secret.
        """
        return pulumi.get(self, "oauth2_client_id")

    @oauth2_client_id.setter
    def oauth2_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth2_client_id", value)

    @property
    @pulumi.getter(name="oauth2ClientSecret")
    def oauth2_client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        Your oauth2 client secret can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under
        the menu item account secret.
        """
        return pulumi.get(self, "oauth2_client_secret")

    @oauth2_client_secret.setter
    def oauth2_client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth2_client_secret", value)

    @property
    @pulumi.getter(name="oauth2Pass")
    def oauth2_pass(self) -> Optional[pulumi.Input[str]]:
        """
        API Password (this is a new password which you'll set or change in the [Customer Control
        Panel](https://new.contabo.com/account/security) under the menu item account secret.)
        """
        return pulumi.get(self, "oauth2_pass")

    @oauth2_pass.setter
    def oauth2_pass(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth2_pass", value)

    @property
    @pulumi.getter(name="oauth2TokenUrl")
    def oauth2_token_url(self) -> Optional[pulumi.Input[str]]:
        """
        The oauth2 token url is https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token.
        """
        return pulumi.get(self, "oauth2_token_url")

    @oauth2_token_url.setter
    def oauth2_token_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth2_token_url", value)

    @property
    @pulumi.getter(name="oauth2User")
    def oauth2_user(self) -> Optional[pulumi.Input[str]]:
        """
        API User (your email address to login to the [Customer Control Panel](https://new.contabo.com/account/security) under
        the menu item account secret.
        """
        return pulumi.get(self, "oauth2_user")

    @oauth2_user.setter
    def oauth2_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth2_user", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api: Optional[pulumi.Input[str]] = None,
                 oauth2_client_id: Optional[pulumi.Input[str]] = None,
                 oauth2_client_secret: Optional[pulumi.Input[str]] = None,
                 oauth2_pass: Optional[pulumi.Input[str]] = None,
                 oauth2_token_url: Optional[pulumi.Input[str]] = None,
                 oauth2_user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the contabo package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api: The api endpoint is https://api.contabo.com.
        :param pulumi.Input[str] oauth2_client_id: Your oauth2 client id can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under the
               menu item account secret.
        :param pulumi.Input[str] oauth2_client_secret: Your oauth2 client secret can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under
               the menu item account secret.
        :param pulumi.Input[str] oauth2_pass: API Password (this is a new password which you'll set or change in the [Customer Control
               Panel](https://new.contabo.com/account/security) under the menu item account secret.)
        :param pulumi.Input[str] oauth2_token_url: The oauth2 token url is https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token.
        :param pulumi.Input[str] oauth2_user: API User (your email address to login to the [Customer Control Panel](https://new.contabo.com/account/security) under
               the menu item account secret.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the contabo package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api: Optional[pulumi.Input[str]] = None,
                 oauth2_client_id: Optional[pulumi.Input[str]] = None,
                 oauth2_client_secret: Optional[pulumi.Input[str]] = None,
                 oauth2_pass: Optional[pulumi.Input[str]] = None,
                 oauth2_token_url: Optional[pulumi.Input[str]] = None,
                 oauth2_user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["api"] = api
            if oauth2_client_id is None:
                oauth2_client_id = _utilities.get_env('CONTABO_OAUTH2_CLIENT_ID')
            __props__.__dict__["oauth2_client_id"] = oauth2_client_id
            if oauth2_client_secret is None:
                oauth2_client_secret = _utilities.get_env('CONTABO_OAUTH2_CLIENT_SECRET')
            __props__.__dict__["oauth2_client_secret"] = oauth2_client_secret
            if oauth2_pass is None:
                oauth2_pass = _utilities.get_env('CONTABO_OAUTH2_PASS')
            __props__.__dict__["oauth2_pass"] = oauth2_pass
            __props__.__dict__["oauth2_token_url"] = oauth2_token_url
            if oauth2_user is None:
                oauth2_user = _utilities.get_env('CONTABO_OAUTH2_USER')
            __props__.__dict__["oauth2_user"] = oauth2_user
        super(Provider, __self__).__init__(
            'contabo',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def api(self) -> pulumi.Output[Optional[str]]:
        """
        The api endpoint is https://api.contabo.com.
        """
        return pulumi.get(self, "api")

    @property
    @pulumi.getter(name="oauth2ClientId")
    def oauth2_client_id(self) -> pulumi.Output[Optional[str]]:
        """
        Your oauth2 client id can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under the
        menu item account secret.
        """
        return pulumi.get(self, "oauth2_client_id")

    @property
    @pulumi.getter(name="oauth2ClientSecret")
    def oauth2_client_secret(self) -> pulumi.Output[Optional[str]]:
        """
        Your oauth2 client secret can be found in the [Customer Control Panel](https://new.contabo.com/account/security) under
        the menu item account secret.
        """
        return pulumi.get(self, "oauth2_client_secret")

    @property
    @pulumi.getter(name="oauth2Pass")
    def oauth2_pass(self) -> pulumi.Output[Optional[str]]:
        """
        API Password (this is a new password which you'll set or change in the [Customer Control
        Panel](https://new.contabo.com/account/security) under the menu item account secret.)
        """
        return pulumi.get(self, "oauth2_pass")

    @property
    @pulumi.getter(name="oauth2TokenUrl")
    def oauth2_token_url(self) -> pulumi.Output[Optional[str]]:
        """
        The oauth2 token url is https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token.
        """
        return pulumi.get(self, "oauth2_token_url")

    @property
    @pulumi.getter(name="oauth2User")
    def oauth2_user(self) -> pulumi.Output[Optional[str]]:
        """
        API User (your email address to login to the [Customer Control Panel](https://new.contabo.com/account/security) under
        the menu item account secret.
        """
        return pulumi.get(self, "oauth2_user")

