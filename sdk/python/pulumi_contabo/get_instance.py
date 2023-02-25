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
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    """
    A collection of values returned by getInstance.
    """
    def __init__(__self__, add_ons=None, additional_ips_v4s=None, cancel_date=None, cpu_cores=None, created_date=None, disk_mb=None, display_name=None, error_message=None, id=None, image_id=None, ip_configs=None, last_updated=None, license=None, mac_address=None, name=None, os_type=None, period=None, product_id=None, product_type=None, ram_mb=None, region=None, ssh_keys=None, status=None, user_data=None, v_host_id=None):
        if add_ons and not isinstance(add_ons, list):
            raise TypeError("Expected argument 'add_ons' to be a list")
        pulumi.set(__self__, "add_ons", add_ons)
        if additional_ips_v4s and not isinstance(additional_ips_v4s, list):
            raise TypeError("Expected argument 'additional_ips_v4s' to be a list")
        pulumi.set(__self__, "additional_ips_v4s", additional_ips_v4s)
        if cancel_date and not isinstance(cancel_date, str):
            raise TypeError("Expected argument 'cancel_date' to be a str")
        pulumi.set(__self__, "cancel_date", cancel_date)
        if cpu_cores and not isinstance(cpu_cores, int):
            raise TypeError("Expected argument 'cpu_cores' to be a int")
        pulumi.set(__self__, "cpu_cores", cpu_cores)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if disk_mb and not isinstance(disk_mb, int):
            raise TypeError("Expected argument 'disk_mb' to be a int")
        pulumi.set(__self__, "disk_mb", disk_mb)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if ip_configs and not isinstance(ip_configs, list):
            raise TypeError("Expected argument 'ip_configs' to be a list")
        pulumi.set(__self__, "ip_configs", ip_configs)
        if last_updated and not isinstance(last_updated, str):
            raise TypeError("Expected argument 'last_updated' to be a str")
        pulumi.set(__self__, "last_updated", last_updated)
        if license and not isinstance(license, str):
            raise TypeError("Expected argument 'license' to be a str")
        pulumi.set(__self__, "license", license)
        if mac_address and not isinstance(mac_address, str):
            raise TypeError("Expected argument 'mac_address' to be a str")
        pulumi.set(__self__, "mac_address", mac_address)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if period and not isinstance(period, int):
            raise TypeError("Expected argument 'period' to be a int")
        pulumi.set(__self__, "period", period)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)
        if product_type and not isinstance(product_type, str):
            raise TypeError("Expected argument 'product_type' to be a str")
        pulumi.set(__self__, "product_type", product_type)
        if ram_mb and not isinstance(ram_mb, int):
            raise TypeError("Expected argument 'ram_mb' to be a int")
        pulumi.set(__self__, "ram_mb", ram_mb)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if ssh_keys and not isinstance(ssh_keys, list):
            raise TypeError("Expected argument 'ssh_keys' to be a list")
        pulumi.set(__self__, "ssh_keys", ssh_keys)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if user_data and not isinstance(user_data, str):
            raise TypeError("Expected argument 'user_data' to be a str")
        pulumi.set(__self__, "user_data", user_data)
        if v_host_id and not isinstance(v_host_id, int):
            raise TypeError("Expected argument 'v_host_id' to be a int")
        pulumi.set(__self__, "v_host_id", v_host_id)

    @property
    @pulumi.getter(name="addOns")
    def add_ons(self) -> Sequence['outputs.GetInstanceAddOnResult']:
        return pulumi.get(self, "add_ons")

    @property
    @pulumi.getter(name="additionalIpsV4s")
    def additional_ips_v4s(self) -> Sequence['outputs.GetInstanceAdditionalIpsV4Result']:
        return pulumi.get(self, "additional_ips_v4s")

    @property
    @pulumi.getter(name="cancelDate")
    def cancel_date(self) -> str:
        return pulumi.get(self, "cancel_date")

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> int:
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="diskMb")
    def disk_mb(self) -> int:
        return pulumi.get(self, "disk_mb")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="ipConfigs")
    def ip_configs(self) -> Sequence['outputs.GetInstanceIpConfigResult']:
        return pulumi.get(self, "ip_configs")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> str:
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter
    def license(self) -> str:
        return pulumi.get(self, "license")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> str:
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def period(self) -> int:
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="productType")
    def product_type(self) -> str:
        return pulumi.get(self, "product_type")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> int:
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="sshKeys")
    def ssh_keys(self) -> Sequence[int]:
        return pulumi.get(self, "ssh_keys")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> str:
        return pulumi.get(self, "user_data")

    @property
    @pulumi.getter(name="vHostId")
    def v_host_id(self) -> int:
        return pulumi.get(self, "v_host_id")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            add_ons=self.add_ons,
            additional_ips_v4s=self.additional_ips_v4s,
            cancel_date=self.cancel_date,
            cpu_cores=self.cpu_cores,
            created_date=self.created_date,
            disk_mb=self.disk_mb,
            display_name=self.display_name,
            error_message=self.error_message,
            id=self.id,
            image_id=self.image_id,
            ip_configs=self.ip_configs,
            last_updated=self.last_updated,
            license=self.license,
            mac_address=self.mac_address,
            name=self.name,
            os_type=self.os_type,
            period=self.period,
            product_id=self.product_id,
            product_type=self.product_type,
            ram_mb=self.ram_mb,
            region=self.region,
            ssh_keys=self.ssh_keys,
            status=self.status,
            user_data=self.user_data,
            v_host_id=self.v_host_id)


def get_instance(add_ons: Optional[Sequence[pulumi.InputType['GetInstanceAddOnArgs']]] = None,
                 cancel_date: Optional[str] = None,
                 display_name: Optional[str] = None,
                 id: Optional[str] = None,
                 image_id: Optional[str] = None,
                 license: Optional[str] = None,
                 product_id: Optional[str] = None,
                 region: Optional[str] = None,
                 ssh_keys: Optional[Sequence[int]] = None,
                 user_data: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['addOns'] = add_ons
    __args__['cancelDate'] = cancel_date
    __args__['displayName'] = display_name
    __args__['id'] = id
    __args__['imageId'] = image_id
    __args__['license'] = license
    __args__['productId'] = product_id
    __args__['region'] = region
    __args__['sshKeys'] = ssh_keys
    __args__['userData'] = user_data
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('contabo:index/getInstance:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        add_ons=__ret__.add_ons,
        additional_ips_v4s=__ret__.additional_ips_v4s,
        cancel_date=__ret__.cancel_date,
        cpu_cores=__ret__.cpu_cores,
        created_date=__ret__.created_date,
        disk_mb=__ret__.disk_mb,
        display_name=__ret__.display_name,
        error_message=__ret__.error_message,
        id=__ret__.id,
        image_id=__ret__.image_id,
        ip_configs=__ret__.ip_configs,
        last_updated=__ret__.last_updated,
        license=__ret__.license,
        mac_address=__ret__.mac_address,
        name=__ret__.name,
        os_type=__ret__.os_type,
        period=__ret__.period,
        product_id=__ret__.product_id,
        product_type=__ret__.product_type,
        ram_mb=__ret__.ram_mb,
        region=__ret__.region,
        ssh_keys=__ret__.ssh_keys,
        status=__ret__.status,
        user_data=__ret__.user_data,
        v_host_id=__ret__.v_host_id)


@_utilities.lift_output_func(get_instance)
def get_instance_output(add_ons: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInstanceAddOnArgs']]]]] = None,
                        cancel_date: Optional[pulumi.Input[Optional[str]]] = None,
                        display_name: Optional[pulumi.Input[Optional[str]]] = None,
                        id: Optional[pulumi.Input[str]] = None,
                        image_id: Optional[pulumi.Input[Optional[str]]] = None,
                        license: Optional[pulumi.Input[Optional[str]]] = None,
                        product_id: Optional[pulumi.Input[Optional[str]]] = None,
                        region: Optional[pulumi.Input[Optional[str]]] = None,
                        ssh_keys: Optional[pulumi.Input[Optional[Sequence[int]]]] = None,
                        user_data: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
