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

__all__ = [
    'GetObjectStorageResult',
    'AwaitableGetObjectStorageResult',
    'get_object_storage',
    'get_object_storage_output',
]

@pulumi.output_type
class GetObjectStorageResult:
    """
    A collection of values returned by getObjectStorage.
    """
    def __init__(__self__, auto_scalings=None, cancel_date=None, created_date=None, customer_id=None, data_center=None, display_name=None, id=None, region=None, s3_tenant_id=None, s3_url=None, status=None, tenant_id=None, total_purchased_space_tb=None):
        if auto_scalings and not isinstance(auto_scalings, list):
            raise TypeError("Expected argument 'auto_scalings' to be a list")
        pulumi.set(__self__, "auto_scalings", auto_scalings)
        if cancel_date and not isinstance(cancel_date, str):
            raise TypeError("Expected argument 'cancel_date' to be a str")
        pulumi.set(__self__, "cancel_date", cancel_date)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if customer_id and not isinstance(customer_id, str):
            raise TypeError("Expected argument 'customer_id' to be a str")
        pulumi.set(__self__, "customer_id", customer_id)
        if data_center and not isinstance(data_center, str):
            raise TypeError("Expected argument 'data_center' to be a str")
        pulumi.set(__self__, "data_center", data_center)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if s3_tenant_id and not isinstance(s3_tenant_id, str):
            raise TypeError("Expected argument 's3_tenant_id' to be a str")
        pulumi.set(__self__, "s3_tenant_id", s3_tenant_id)
        if s3_url and not isinstance(s3_url, str):
            raise TypeError("Expected argument 's3_url' to be a str")
        pulumi.set(__self__, "s3_url", s3_url)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if total_purchased_space_tb and not isinstance(total_purchased_space_tb, float):
            raise TypeError("Expected argument 'total_purchased_space_tb' to be a float")
        pulumi.set(__self__, "total_purchased_space_tb", total_purchased_space_tb)

    @property
    @pulumi.getter(name="autoScalings")
    def auto_scalings(self) -> Sequence['outputs.GetObjectStorageAutoScalingResult']:
        return pulumi.get(self, "auto_scalings")

    @property
    @pulumi.getter(name="cancelDate")
    def cancel_date(self) -> str:
        return pulumi.get(self, "cancel_date")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> str:
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> str:
        return pulumi.get(self, "data_center")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="s3TenantId")
    def s3_tenant_id(self) -> str:
        return pulumi.get(self, "s3_tenant_id")

    @property
    @pulumi.getter(name="s3Url")
    def s3_url(self) -> str:
        return pulumi.get(self, "s3_url")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="totalPurchasedSpaceTb")
    def total_purchased_space_tb(self) -> float:
        return pulumi.get(self, "total_purchased_space_tb")


class AwaitableGetObjectStorageResult(GetObjectStorageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectStorageResult(
            auto_scalings=self.auto_scalings,
            cancel_date=self.cancel_date,
            created_date=self.created_date,
            customer_id=self.customer_id,
            data_center=self.data_center,
            display_name=self.display_name,
            id=self.id,
            region=self.region,
            s3_tenant_id=self.s3_tenant_id,
            s3_url=self.s3_url,
            status=self.status,
            tenant_id=self.tenant_id,
            total_purchased_space_tb=self.total_purchased_space_tb)


def get_object_storage(auto_scalings: Optional[Sequence[pulumi.InputType['GetObjectStorageAutoScalingArgs']]] = None,
                       id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectStorageResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['autoScalings'] = auto_scalings
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('contabo:index/getObjectStorage:getObjectStorage', __args__, opts=opts, typ=GetObjectStorageResult).value

    return AwaitableGetObjectStorageResult(
        auto_scalings=__ret__.auto_scalings,
        cancel_date=__ret__.cancel_date,
        created_date=__ret__.created_date,
        customer_id=__ret__.customer_id,
        data_center=__ret__.data_center,
        display_name=__ret__.display_name,
        id=__ret__.id,
        region=__ret__.region,
        s3_tenant_id=__ret__.s3_tenant_id,
        s3_url=__ret__.s3_url,
        status=__ret__.status,
        tenant_id=__ret__.tenant_id,
        total_purchased_space_tb=__ret__.total_purchased_space_tb)


@_utilities.lift_output_func(get_object_storage)
def get_object_storage_output(auto_scalings: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetObjectStorageAutoScalingArgs']]]]] = None,
                              id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetObjectStorageResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
