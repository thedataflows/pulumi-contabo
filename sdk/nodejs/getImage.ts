// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getImage(args: GetImageArgs, opts?: pulumi.InvokeOptions): Promise<GetImageResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("contabo:index/getImage:getImage", {
        "description": args.description,
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getImage.
 */
export interface GetImageArgs {
    description?: string;
    id: string;
}

/**
 * A collection of values returned by getImage.
 */
export interface GetImageResult {
    readonly creationDate: string;
    readonly description: string;
    readonly errorMessage: string;
    readonly format: string;
    readonly id: string;
    readonly lastUpdated: string;
    readonly name: string;
    readonly osType: string;
    readonly standardImage: boolean;
    readonly status: string;
    readonly uploadedSizeMb: number;
    readonly version: string;
}
export function getImageOutput(args: GetImageOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetImageResult> {
    return pulumi.output(args).apply((a: any) => getImage(a, opts))
}

/**
 * A collection of arguments for invoking getImage.
 */
export interface GetImageOutputArgs {
    description?: pulumi.Input<string>;
    id: pulumi.Input<string>;
}
