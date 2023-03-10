// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { GetImageArgs, GetImageResult, GetImageOutputArgs } from "./getImage";
export const getImage: typeof import("./getImage").getImage = null as any;
export const getImageOutput: typeof import("./getImage").getImageOutput = null as any;
utilities.lazyLoad(exports, ["getImage","getImageOutput"], () => require("./getImage"));

export { GetInstanceArgs, GetInstanceResult, GetInstanceOutputArgs } from "./getInstance";
export const getInstance: typeof import("./getInstance").getInstance = null as any;
export const getInstanceOutput: typeof import("./getInstance").getInstanceOutput = null as any;
utilities.lazyLoad(exports, ["getInstance","getInstanceOutput"], () => require("./getInstance"));

export { GetInstanceSnapshotArgs, GetInstanceSnapshotResult, GetInstanceSnapshotOutputArgs } from "./getInstanceSnapshot";
export const getInstanceSnapshot: typeof import("./getInstanceSnapshot").getInstanceSnapshot = null as any;
export const getInstanceSnapshotOutput: typeof import("./getInstanceSnapshot").getInstanceSnapshotOutput = null as any;
utilities.lazyLoad(exports, ["getInstanceSnapshot","getInstanceSnapshotOutput"], () => require("./getInstanceSnapshot"));

export { GetObjectStorageArgs, GetObjectStorageResult, GetObjectStorageOutputArgs } from "./getObjectStorage";
export const getObjectStorage: typeof import("./getObjectStorage").getObjectStorage = null as any;
export const getObjectStorageOutput: typeof import("./getObjectStorage").getObjectStorageOutput = null as any;
utilities.lazyLoad(exports, ["getObjectStorage","getObjectStorageOutput"], () => require("./getObjectStorage"));

export { GetObjectStorageBucketArgs, GetObjectStorageBucketResult, GetObjectStorageBucketOutputArgs } from "./getObjectStorageBucket";
export const getObjectStorageBucket: typeof import("./getObjectStorageBucket").getObjectStorageBucket = null as any;
export const getObjectStorageBucketOutput: typeof import("./getObjectStorageBucket").getObjectStorageBucketOutput = null as any;
utilities.lazyLoad(exports, ["getObjectStorageBucket","getObjectStorageBucketOutput"], () => require("./getObjectStorageBucket"));

export { GetPrivateNetworkArgs, GetPrivateNetworkResult, GetPrivateNetworkOutputArgs } from "./getPrivateNetwork";
export const getPrivateNetwork: typeof import("./getPrivateNetwork").getPrivateNetwork = null as any;
export const getPrivateNetworkOutput: typeof import("./getPrivateNetwork").getPrivateNetworkOutput = null as any;
utilities.lazyLoad(exports, ["getPrivateNetwork","getPrivateNetworkOutput"], () => require("./getPrivateNetwork"));

export { GetSecretArgs, GetSecretResult, GetSecretOutputArgs } from "./getSecret";
export const getSecret: typeof import("./getSecret").getSecret = null as any;
export const getSecretOutput: typeof import("./getSecret").getSecretOutput = null as any;
utilities.lazyLoad(exports, ["getSecret","getSecretOutput"], () => require("./getSecret"));

export { ImageArgs, ImageState } from "./image";
export type Image = import("./image").Image;
export const Image: typeof import("./image").Image = null as any;
utilities.lazyLoad(exports, ["Image"], () => require("./image"));

export { InstanceArgs, InstanceState } from "./instance";
export type Instance = import("./instance").Instance;
export const Instance: typeof import("./instance").Instance = null as any;
utilities.lazyLoad(exports, ["Instance"], () => require("./instance"));

export { Instance_snapshotArgs, Instance_snapshotState } from "./instance_snapshot";
export type Instance_snapshot = import("./instance_snapshot").Instance_snapshot;
export const Instance_snapshot: typeof import("./instance_snapshot").Instance_snapshot = null as any;
utilities.lazyLoad(exports, ["Instance_snapshot"], () => require("./instance_snapshot"));

export { Object_storageArgs, Object_storageState } from "./object_storage";
export type Object_storage = import("./object_storage").Object_storage;
export const Object_storage: typeof import("./object_storage").Object_storage = null as any;
utilities.lazyLoad(exports, ["Object_storage"], () => require("./object_storage"));

export { Object_storage_bucketArgs, Object_storage_bucketState } from "./object_storage_bucket";
export type Object_storage_bucket = import("./object_storage_bucket").Object_storage_bucket;
export const Object_storage_bucket: typeof import("./object_storage_bucket").Object_storage_bucket = null as any;
utilities.lazyLoad(exports, ["Object_storage_bucket"], () => require("./object_storage_bucket"));

export { Private_networkArgs, Private_networkState } from "./private_network";
export type Private_network = import("./private_network").Private_network;
export const Private_network: typeof import("./private_network").Private_network = null as any;
utilities.lazyLoad(exports, ["Private_network"], () => require("./private_network"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { SecretArgs, SecretState } from "./secret";
export type Secret = import("./secret").Secret;
export const Secret: typeof import("./secret").Secret = null as any;
utilities.lazyLoad(exports, ["Secret"], () => require("./secret"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "contabo:index/image:image":
                return new Image(name, <any>undefined, { urn })
            case "contabo:index/instance:instance":
                return new Instance(name, <any>undefined, { urn })
            case "contabo:index/instance_snapshot:instance_snapshot":
                return new Instance_snapshot(name, <any>undefined, { urn })
            case "contabo:index/object_storage:object_storage":
                return new Object_storage(name, <any>undefined, { urn })
            case "contabo:index/object_storage_bucket:object_storage_bucket":
                return new Object_storage_bucket(name, <any>undefined, { urn })
            case "contabo:index/private_network:private_network":
                return new Private_network(name, <any>undefined, { urn })
            case "contabo:index/secret:secret":
                return new Secret(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("contabo", "index/image", _module)
pulumi.runtime.registerResourceModule("contabo", "index/instance", _module)
pulumi.runtime.registerResourceModule("contabo", "index/instance_snapshot", _module)
pulumi.runtime.registerResourceModule("contabo", "index/object_storage", _module)
pulumi.runtime.registerResourceModule("contabo", "index/object_storage_bucket", _module)
pulumi.runtime.registerResourceModule("contabo", "index/private_network", _module)
pulumi.runtime.registerResourceModule("contabo", "index/secret", _module)
pulumi.runtime.registerResourcePackage("contabo", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:contabo") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
