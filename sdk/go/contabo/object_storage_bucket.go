// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package contabo

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Object_storage_bucket struct {
	pulumi.CustomResourceState

	// The creation date of the bucket.
	CreationDate pulumi.StringOutput `pulumi:"creationDate"`
	// The name of your bucket, consider the naming restriction
	// https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html.
	Name pulumi.StringOutput `pulumi:"name"`
	// The contabo objectStorageId on which the bucket should be created.
	ObjectStorageId pulumi.StringOutput `pulumi:"objectStorageId"`
	// Choose the access to your bucket. You can not share it at all or share it publicly.
	PublicSharing pulumi.BoolPtrOutput `pulumi:"publicSharing"`
	// If your bucket is publicly shared, you can access it with this link.
	PublicSharingLink pulumi.StringOutput `pulumi:"publicSharingLink"`
}

// NewObject_storage_bucket registers a new resource with the given unique name, arguments, and options.
func NewObject_storage_bucket(ctx *pulumi.Context,
	name string, args *Object_storage_bucketArgs, opts ...pulumi.ResourceOption) (*Object_storage_bucket, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ObjectStorageId == nil {
		return nil, errors.New("invalid value for required argument 'ObjectStorageId'")
	}
	var resource Object_storage_bucket
	err := ctx.RegisterResource("contabo:index/object_storage_bucket:object_storage_bucket", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetObject_storage_bucket gets an existing Object_storage_bucket resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetObject_storage_bucket(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *Object_storage_bucketState, opts ...pulumi.ResourceOption) (*Object_storage_bucket, error) {
	var resource Object_storage_bucket
	err := ctx.ReadResource("contabo:index/object_storage_bucket:object_storage_bucket", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Object_storage_bucket resources.
type object_storage_bucketState struct {
	// The creation date of the bucket.
	CreationDate *string `pulumi:"creationDate"`
	// The name of your bucket, consider the naming restriction
	// https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html.
	Name *string `pulumi:"name"`
	// The contabo objectStorageId on which the bucket should be created.
	ObjectStorageId *string `pulumi:"objectStorageId"`
	// Choose the access to your bucket. You can not share it at all or share it publicly.
	PublicSharing *bool `pulumi:"publicSharing"`
	// If your bucket is publicly shared, you can access it with this link.
	PublicSharingLink *string `pulumi:"publicSharingLink"`
}

type Object_storage_bucketState struct {
	// The creation date of the bucket.
	CreationDate pulumi.StringPtrInput
	// The name of your bucket, consider the naming restriction
	// https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html.
	Name pulumi.StringPtrInput
	// The contabo objectStorageId on which the bucket should be created.
	ObjectStorageId pulumi.StringPtrInput
	// Choose the access to your bucket. You can not share it at all or share it publicly.
	PublicSharing pulumi.BoolPtrInput
	// If your bucket is publicly shared, you can access it with this link.
	PublicSharingLink pulumi.StringPtrInput
}

func (Object_storage_bucketState) ElementType() reflect.Type {
	return reflect.TypeOf((*object_storage_bucketState)(nil)).Elem()
}

type object_storage_bucketArgs struct {
	// The name of your bucket, consider the naming restriction
	// https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html.
	Name *string `pulumi:"name"`
	// The contabo objectStorageId on which the bucket should be created.
	ObjectStorageId string `pulumi:"objectStorageId"`
	// Choose the access to your bucket. You can not share it at all or share it publicly.
	PublicSharing *bool `pulumi:"publicSharing"`
}

// The set of arguments for constructing a Object_storage_bucket resource.
type Object_storage_bucketArgs struct {
	// The name of your bucket, consider the naming restriction
	// https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html.
	Name pulumi.StringPtrInput
	// The contabo objectStorageId on which the bucket should be created.
	ObjectStorageId pulumi.StringInput
	// Choose the access to your bucket. You can not share it at all or share it publicly.
	PublicSharing pulumi.BoolPtrInput
}

func (Object_storage_bucketArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*object_storage_bucketArgs)(nil)).Elem()
}

type Object_storage_bucketInput interface {
	pulumi.Input

	ToObject_storage_bucketOutput() Object_storage_bucketOutput
	ToObject_storage_bucketOutputWithContext(ctx context.Context) Object_storage_bucketOutput
}

func (*Object_storage_bucket) ElementType() reflect.Type {
	return reflect.TypeOf((**Object_storage_bucket)(nil)).Elem()
}

func (i *Object_storage_bucket) ToObject_storage_bucketOutput() Object_storage_bucketOutput {
	return i.ToObject_storage_bucketOutputWithContext(context.Background())
}

func (i *Object_storage_bucket) ToObject_storage_bucketOutputWithContext(ctx context.Context) Object_storage_bucketOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Object_storage_bucketOutput)
}

// Object_storage_bucketArrayInput is an input type that accepts Object_storage_bucketArray and Object_storage_bucketArrayOutput values.
// You can construct a concrete instance of `Object_storage_bucketArrayInput` via:
//
//	Object_storage_bucketArray{ Object_storage_bucketArgs{...} }
type Object_storage_bucketArrayInput interface {
	pulumi.Input

	ToObject_storage_bucketArrayOutput() Object_storage_bucketArrayOutput
	ToObject_storage_bucketArrayOutputWithContext(context.Context) Object_storage_bucketArrayOutput
}

type Object_storage_bucketArray []Object_storage_bucketInput

func (Object_storage_bucketArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Object_storage_bucket)(nil)).Elem()
}

func (i Object_storage_bucketArray) ToObject_storage_bucketArrayOutput() Object_storage_bucketArrayOutput {
	return i.ToObject_storage_bucketArrayOutputWithContext(context.Background())
}

func (i Object_storage_bucketArray) ToObject_storage_bucketArrayOutputWithContext(ctx context.Context) Object_storage_bucketArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Object_storage_bucketArrayOutput)
}

// Object_storage_bucketMapInput is an input type that accepts Object_storage_bucketMap and Object_storage_bucketMapOutput values.
// You can construct a concrete instance of `Object_storage_bucketMapInput` via:
//
//	Object_storage_bucketMap{ "key": Object_storage_bucketArgs{...} }
type Object_storage_bucketMapInput interface {
	pulumi.Input

	ToObject_storage_bucketMapOutput() Object_storage_bucketMapOutput
	ToObject_storage_bucketMapOutputWithContext(context.Context) Object_storage_bucketMapOutput
}

type Object_storage_bucketMap map[string]Object_storage_bucketInput

func (Object_storage_bucketMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Object_storage_bucket)(nil)).Elem()
}

func (i Object_storage_bucketMap) ToObject_storage_bucketMapOutput() Object_storage_bucketMapOutput {
	return i.ToObject_storage_bucketMapOutputWithContext(context.Background())
}

func (i Object_storage_bucketMap) ToObject_storage_bucketMapOutputWithContext(ctx context.Context) Object_storage_bucketMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Object_storage_bucketMapOutput)
}

type Object_storage_bucketOutput struct{ *pulumi.OutputState }

func (Object_storage_bucketOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Object_storage_bucket)(nil)).Elem()
}

func (o Object_storage_bucketOutput) ToObject_storage_bucketOutput() Object_storage_bucketOutput {
	return o
}

func (o Object_storage_bucketOutput) ToObject_storage_bucketOutputWithContext(ctx context.Context) Object_storage_bucketOutput {
	return o
}

// The creation date of the bucket.
func (o Object_storage_bucketOutput) CreationDate() pulumi.StringOutput {
	return o.ApplyT(func(v *Object_storage_bucket) pulumi.StringOutput { return v.CreationDate }).(pulumi.StringOutput)
}

// The name of your bucket, consider the naming restriction
// https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html.
func (o Object_storage_bucketOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Object_storage_bucket) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The contabo objectStorageId on which the bucket should be created.
func (o Object_storage_bucketOutput) ObjectStorageId() pulumi.StringOutput {
	return o.ApplyT(func(v *Object_storage_bucket) pulumi.StringOutput { return v.ObjectStorageId }).(pulumi.StringOutput)
}

// Choose the access to your bucket. You can not share it at all or share it publicly.
func (o Object_storage_bucketOutput) PublicSharing() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Object_storage_bucket) pulumi.BoolPtrOutput { return v.PublicSharing }).(pulumi.BoolPtrOutput)
}

// If your bucket is publicly shared, you can access it with this link.
func (o Object_storage_bucketOutput) PublicSharingLink() pulumi.StringOutput {
	return o.ApplyT(func(v *Object_storage_bucket) pulumi.StringOutput { return v.PublicSharingLink }).(pulumi.StringOutput)
}

type Object_storage_bucketArrayOutput struct{ *pulumi.OutputState }

func (Object_storage_bucketArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Object_storage_bucket)(nil)).Elem()
}

func (o Object_storage_bucketArrayOutput) ToObject_storage_bucketArrayOutput() Object_storage_bucketArrayOutput {
	return o
}

func (o Object_storage_bucketArrayOutput) ToObject_storage_bucketArrayOutputWithContext(ctx context.Context) Object_storage_bucketArrayOutput {
	return o
}

func (o Object_storage_bucketArrayOutput) Index(i pulumi.IntInput) Object_storage_bucketOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Object_storage_bucket {
		return vs[0].([]*Object_storage_bucket)[vs[1].(int)]
	}).(Object_storage_bucketOutput)
}

type Object_storage_bucketMapOutput struct{ *pulumi.OutputState }

func (Object_storage_bucketMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Object_storage_bucket)(nil)).Elem()
}

func (o Object_storage_bucketMapOutput) ToObject_storage_bucketMapOutput() Object_storage_bucketMapOutput {
	return o
}

func (o Object_storage_bucketMapOutput) ToObject_storage_bucketMapOutputWithContext(ctx context.Context) Object_storage_bucketMapOutput {
	return o
}

func (o Object_storage_bucketMapOutput) MapIndex(k pulumi.StringInput) Object_storage_bucketOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Object_storage_bucket {
		return vs[0].(map[string]*Object_storage_bucket)[vs[1].(string)]
	}).(Object_storage_bucketOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*Object_storage_bucketInput)(nil)).Elem(), &Object_storage_bucket{})
	pulumi.RegisterInputType(reflect.TypeOf((*Object_storage_bucketArrayInput)(nil)).Elem(), Object_storage_bucketArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*Object_storage_bucketMapInput)(nil)).Elem(), Object_storage_bucketMap{})
	pulumi.RegisterOutputType(Object_storage_bucketOutput{})
	pulumi.RegisterOutputType(Object_storage_bucketArrayOutput{})
	pulumi.RegisterOutputType(Object_storage_bucketMapOutput{})
}