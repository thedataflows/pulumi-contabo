# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SecretArgs', 'Secret']

@pulumi.input_type
class SecretArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 value: pulumi.Input[str],
                 created_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Secret resource.
        :param pulumi.Input[str] type: The type of the secret. It will be available only when retrieving secrets, following types are allowed: `ssh`,
               `password`.
        :param pulumi.Input[str] value: The value of the secret. It will be available only when retrieving a single secret.
        :param pulumi.Input[str] created_at: The creation date of the secret.
        :param pulumi.Input[str] name: Name of the secret.
        :param pulumi.Input[str] updated_at: Last updated time of the secret.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the secret. It will be available only when retrieving secrets, following types are allowed: `ssh`,
        `password`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the secret. It will be available only when retrieving a single secret.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The creation date of the secret.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the secret.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Last updated time of the secret.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


@pulumi.input_type
class _SecretState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Secret resources.
        :param pulumi.Input[str] created_at: The creation date of the secret.
        :param pulumi.Input[str] name: Name of the secret.
        :param pulumi.Input[str] type: The type of the secret. It will be available only when retrieving secrets, following types are allowed: `ssh`,
               `password`.
        :param pulumi.Input[str] updated_at: Last updated time of the secret.
        :param pulumi.Input[str] value: The value of the secret. It will be available only when retrieving a single secret.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The creation date of the secret.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the secret.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the secret. It will be available only when retrieving secrets, following types are allowed: `ssh`,
        `password`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Last updated time of the secret.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the secret. It will be available only when retrieving a single secret.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class Secret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Secret resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The creation date of the secret.
        :param pulumi.Input[str] name: Name of the secret.
        :param pulumi.Input[str] type: The type of the secret. It will be available only when retrieving secrets, following types are allowed: `ssh`,
               `password`.
        :param pulumi.Input[str] updated_at: Last updated time of the secret.
        :param pulumi.Input[str] value: The value of the secret. It will be available only when retrieving a single secret.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Secret resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecretArgs.__new__(SecretArgs)

            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["updated_at"] = updated_at
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
        super(Secret, __self__).__init__(
            'contabo:index/secret:secret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'Secret':
        """
        Get an existing Secret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The creation date of the secret.
        :param pulumi.Input[str] name: Name of the secret.
        :param pulumi.Input[str] type: The type of the secret. It will be available only when retrieving secrets, following types are allowed: `ssh`,
               `password`.
        :param pulumi.Input[str] updated_at: Last updated time of the secret.
        :param pulumi.Input[str] value: The value of the secret. It will be available only when retrieving a single secret.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretState.__new__(_SecretState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["value"] = value
        return Secret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The creation date of the secret.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the secret.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the secret. It will be available only when retrieving secrets, following types are allowed: `ssh`,
        `password`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Last updated time of the secret.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the secret. It will be available only when retrieving a single secret.
        """
        return pulumi.get(self, "value")

