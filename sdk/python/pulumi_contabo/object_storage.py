# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['Object_storageArgs', 'Object_storage']

@pulumi.input_type
class Object_storageArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 total_purchased_space_tb: pulumi.Input[float],
                 auto_scalings: Optional[pulumi.Input[Sequence[pulumi.Input['Object_storageAutoScalingArgs']]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Object_storage resource.
        :param pulumi.Input[str] region: Region where the Object Storage should be located. Default region is the EU. Following regions are available:
               `EU`,`US-central`, `SIN`.
        :param pulumi.Input[float] total_purchased_space_tb: Amount of purchased / requested object storage in terabyte.
        :param pulumi.Input[str] display_name: Display name for object storage.
        """
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "total_purchased_space_tb", total_purchased_space_tb)
        if auto_scalings is not None:
            pulumi.set(__self__, "auto_scalings", auto_scalings)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        Region where the Object Storage should be located. Default region is the EU. Following regions are available:
        `EU`,`US-central`, `SIN`.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="totalPurchasedSpaceTb")
    def total_purchased_space_tb(self) -> pulumi.Input[float]:
        """
        Amount of purchased / requested object storage in terabyte.
        """
        return pulumi.get(self, "total_purchased_space_tb")

    @total_purchased_space_tb.setter
    def total_purchased_space_tb(self, value: pulumi.Input[float]):
        pulumi.set(self, "total_purchased_space_tb", value)

    @property
    @pulumi.getter(name="autoScalings")
    def auto_scalings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['Object_storageAutoScalingArgs']]]]:
        return pulumi.get(self, "auto_scalings")

    @auto_scalings.setter
    def auto_scalings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['Object_storageAutoScalingArgs']]]]):
        pulumi.set(self, "auto_scalings", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name for object storage.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


@pulumi.input_type
class _Object_storageState:
    def __init__(__self__, *,
                 auto_scalings: Optional[pulumi.Input[Sequence[pulumi.Input['Object_storageAutoScalingArgs']]]] = None,
                 cancel_date: Optional[pulumi.Input[str]] = None,
                 created_date: Optional[pulumi.Input[str]] = None,
                 customer_id: Optional[pulumi.Input[str]] = None,
                 data_center: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 s3_tenant_id: Optional[pulumi.Input[str]] = None,
                 s3_url: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 total_purchased_space_tb: Optional[pulumi.Input[float]] = None):
        """
        Input properties used for looking up and filtering Object_storage resources.
        :param pulumi.Input[str] cancel_date: The date on which the Object Storage will be cancelled and therefore no longer available.
        :param pulumi.Input[str] created_date: The creation date of the Object Storage.
        :param pulumi.Input[str] customer_id: Your customer number.
        :param pulumi.Input[str] data_center: Data center the object storage is located in.
        :param pulumi.Input[str] display_name: Display name for object storage.
        :param pulumi.Input[str] region: Region where the Object Storage should be located. Default region is the EU. Following regions are available:
               `EU`,`US-central`, `SIN`.
        :param pulumi.Input[str] s3_tenant_id: Your S3 tenant Id. Only required for public sharing.
        :param pulumi.Input[str] s3_url: S3 URL to connect to your S3 compatible Object Storage.
        :param pulumi.Input[str] status: The object storage status. It can be set to `PROVISIONING`,`READY`,`UPGRADING`,`CANCELLED`,`ERROR` or `DISABLED`.
        :param pulumi.Input[str] tenant_id: Your customer tenant Id.
        :param pulumi.Input[float] total_purchased_space_tb: Amount of purchased / requested object storage in terabyte.
        """
        if auto_scalings is not None:
            pulumi.set(__self__, "auto_scalings", auto_scalings)
        if cancel_date is not None:
            pulumi.set(__self__, "cancel_date", cancel_date)
        if created_date is not None:
            pulumi.set(__self__, "created_date", created_date)
        if customer_id is not None:
            pulumi.set(__self__, "customer_id", customer_id)
        if data_center is not None:
            pulumi.set(__self__, "data_center", data_center)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if s3_tenant_id is not None:
            pulumi.set(__self__, "s3_tenant_id", s3_tenant_id)
        if s3_url is not None:
            pulumi.set(__self__, "s3_url", s3_url)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if total_purchased_space_tb is not None:
            pulumi.set(__self__, "total_purchased_space_tb", total_purchased_space_tb)

    @property
    @pulumi.getter(name="autoScalings")
    def auto_scalings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['Object_storageAutoScalingArgs']]]]:
        return pulumi.get(self, "auto_scalings")

    @auto_scalings.setter
    def auto_scalings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['Object_storageAutoScalingArgs']]]]):
        pulumi.set(self, "auto_scalings", value)

    @property
    @pulumi.getter(name="cancelDate")
    def cancel_date(self) -> Optional[pulumi.Input[str]]:
        """
        The date on which the Object Storage will be cancelled and therefore no longer available.
        """
        return pulumi.get(self, "cancel_date")

    @cancel_date.setter
    def cancel_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cancel_date", value)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[str]]:
        """
        The creation date of the Object Storage.
        """
        return pulumi.get(self, "created_date")

    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_date", value)

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[pulumi.Input[str]]:
        """
        Your customer number.
        """
        return pulumi.get(self, "customer_id")

    @customer_id.setter
    def customer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_id", value)

    @property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> Optional[pulumi.Input[str]]:
        """
        Data center the object storage is located in.
        """
        return pulumi.get(self, "data_center")

    @data_center.setter
    def data_center(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_center", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name for object storage.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region where the Object Storage should be located. Default region is the EU. Following regions are available:
        `EU`,`US-central`, `SIN`.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="s3TenantId")
    def s3_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Your S3 tenant Id. Only required for public sharing.
        """
        return pulumi.get(self, "s3_tenant_id")

    @s3_tenant_id.setter
    def s3_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_tenant_id", value)

    @property
    @pulumi.getter(name="s3Url")
    def s3_url(self) -> Optional[pulumi.Input[str]]:
        """
        S3 URL to connect to your S3 compatible Object Storage.
        """
        return pulumi.get(self, "s3_url")

    @s3_url.setter
    def s3_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_url", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The object storage status. It can be set to `PROVISIONING`,`READY`,`UPGRADING`,`CANCELLED`,`ERROR` or `DISABLED`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Your customer tenant Id.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="totalPurchasedSpaceTb")
    def total_purchased_space_tb(self) -> Optional[pulumi.Input[float]]:
        """
        Amount of purchased / requested object storage in terabyte.
        """
        return pulumi.get(self, "total_purchased_space_tb")

    @total_purchased_space_tb.setter
    def total_purchased_space_tb(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "total_purchased_space_tb", value)


class Object_storage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scalings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Object_storageAutoScalingArgs']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 total_purchased_space_tb: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        Create a Object_storage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Display name for object storage.
        :param pulumi.Input[str] region: Region where the Object Storage should be located. Default region is the EU. Following regions are available:
               `EU`,`US-central`, `SIN`.
        :param pulumi.Input[float] total_purchased_space_tb: Amount of purchased / requested object storage in terabyte.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Object_storageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Object_storage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param Object_storageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Object_storageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_scalings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Object_storageAutoScalingArgs']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 total_purchased_space_tb: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = Object_storageArgs.__new__(Object_storageArgs)

            __props__.__dict__["auto_scalings"] = auto_scalings
            __props__.__dict__["display_name"] = display_name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            if total_purchased_space_tb is None and not opts.urn:
                raise TypeError("Missing required property 'total_purchased_space_tb'")
            __props__.__dict__["total_purchased_space_tb"] = total_purchased_space_tb
            __props__.__dict__["cancel_date"] = None
            __props__.__dict__["created_date"] = None
            __props__.__dict__["customer_id"] = None
            __props__.__dict__["data_center"] = None
            __props__.__dict__["s3_tenant_id"] = None
            __props__.__dict__["s3_url"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["tenant_id"] = None
        super(Object_storage, __self__).__init__(
            'contabo:index/object_storage:object_storage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_scalings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Object_storageAutoScalingArgs']]]]] = None,
            cancel_date: Optional[pulumi.Input[str]] = None,
            created_date: Optional[pulumi.Input[str]] = None,
            customer_id: Optional[pulumi.Input[str]] = None,
            data_center: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            s3_tenant_id: Optional[pulumi.Input[str]] = None,
            s3_url: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            total_purchased_space_tb: Optional[pulumi.Input[float]] = None) -> 'Object_storage':
        """
        Get an existing Object_storage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cancel_date: The date on which the Object Storage will be cancelled and therefore no longer available.
        :param pulumi.Input[str] created_date: The creation date of the Object Storage.
        :param pulumi.Input[str] customer_id: Your customer number.
        :param pulumi.Input[str] data_center: Data center the object storage is located in.
        :param pulumi.Input[str] display_name: Display name for object storage.
        :param pulumi.Input[str] region: Region where the Object Storage should be located. Default region is the EU. Following regions are available:
               `EU`,`US-central`, `SIN`.
        :param pulumi.Input[str] s3_tenant_id: Your S3 tenant Id. Only required for public sharing.
        :param pulumi.Input[str] s3_url: S3 URL to connect to your S3 compatible Object Storage.
        :param pulumi.Input[str] status: The object storage status. It can be set to `PROVISIONING`,`READY`,`UPGRADING`,`CANCELLED`,`ERROR` or `DISABLED`.
        :param pulumi.Input[str] tenant_id: Your customer tenant Id.
        :param pulumi.Input[float] total_purchased_space_tb: Amount of purchased / requested object storage in terabyte.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _Object_storageState.__new__(_Object_storageState)

        __props__.__dict__["auto_scalings"] = auto_scalings
        __props__.__dict__["cancel_date"] = cancel_date
        __props__.__dict__["created_date"] = created_date
        __props__.__dict__["customer_id"] = customer_id
        __props__.__dict__["data_center"] = data_center
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["region"] = region
        __props__.__dict__["s3_tenant_id"] = s3_tenant_id
        __props__.__dict__["s3_url"] = s3_url
        __props__.__dict__["status"] = status
        __props__.__dict__["tenant_id"] = tenant_id
        __props__.__dict__["total_purchased_space_tb"] = total_purchased_space_tb
        return Object_storage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoScalings")
    def auto_scalings(self) -> pulumi.Output[Optional[Sequence['outputs.Object_storageAutoScaling']]]:
        return pulumi.get(self, "auto_scalings")

    @property
    @pulumi.getter(name="cancelDate")
    def cancel_date(self) -> pulumi.Output[str]:
        """
        The date on which the Object Storage will be cancelled and therefore no longer available.
        """
        return pulumi.get(self, "cancel_date")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        The creation date of the Object Storage.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> pulumi.Output[str]:
        """
        Your customer number.
        """
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> pulumi.Output[str]:
        """
        Data center the object storage is located in.
        """
        return pulumi.get(self, "data_center")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Display name for object storage.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where the Object Storage should be located. Default region is the EU. Following regions are available:
        `EU`,`US-central`, `SIN`.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="s3TenantId")
    def s3_tenant_id(self) -> pulumi.Output[str]:
        """
        Your S3 tenant Id. Only required for public sharing.
        """
        return pulumi.get(self, "s3_tenant_id")

    @property
    @pulumi.getter(name="s3Url")
    def s3_url(self) -> pulumi.Output[str]:
        """
        S3 URL to connect to your S3 compatible Object Storage.
        """
        return pulumi.get(self, "s3_url")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The object storage status. It can be set to `PROVISIONING`,`READY`,`UPGRADING`,`CANCELLED`,`ERROR` or `DISABLED`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Your customer tenant Id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="totalPurchasedSpaceTb")
    def total_purchased_space_tb(self) -> pulumi.Output[float]:
        """
        Amount of purchased / requested object storage in terabyte.
        """
        return pulumi.get(self, "total_purchased_space_tb")
