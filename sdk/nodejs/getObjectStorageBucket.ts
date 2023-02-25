// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getObjectStorageBucket(args: GetObjectStorageBucketArgs, opts?: pulumi.InvokeOptions): Promise<GetObjectStorageBucketResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("contabo:index/getObjectStorageBucket:getObjectStorageBucket", {
        "name": args.name,
        "objectStorageId": args.objectStorageId,
        "publicSharing": args.publicSharing,
    }, opts);
}

/**
 * A collection of arguments for invoking getObjectStorageBucket.
 */
export interface GetObjectStorageBucketArgs {
    name: string;
    objectStorageId: string;
    publicSharing?: boolean;
}

/**
 * A collection of values returned by getObjectStorageBucket.
 */
export interface GetObjectStorageBucketResult {
    readonly creationDate: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    readonly objectStorageId: string;
    readonly publicSharing?: boolean;
    readonly publicSharingLink: string;
}
export function getObjectStorageBucketOutput(args: GetObjectStorageBucketOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetObjectStorageBucketResult> {
    return pulumi.output(args).apply((a: any) => getObjectStorageBucket(a, opts))
}

/**
 * A collection of arguments for invoking getObjectStorageBucket.
 */
export interface GetObjectStorageBucketOutputArgs {
    name: pulumi.Input<string>;
    objectStorageId: pulumi.Input<string>;
    publicSharing?: pulumi.Input<boolean>;
}
