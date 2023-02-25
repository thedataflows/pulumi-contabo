// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package contabo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Private_network struct {
	pulumi.CustomResourceState

	// The totality of available IPs in the Private Network.
	AvailableIps pulumi.IntOutput `pulumi:"availableIps"`
	// The cidr range of the Private Network.
	Cidr pulumi.StringOutput `pulumi:"cidr"`
	// The creation date of the Private Network.
	CreatedDate pulumi.StringOutput `pulumi:"createdDate"`
	// The specific data center where the Private Network is located.
	DataCenter pulumi.StringOutput `pulumi:"dataCenter"`
	// The description of the Private Network. There is a limit of 255 characters per Private Network.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Add the instace Ids to the private network here. If you do not add any instance Ids an empty private network will be
	// created.
	InstanceIds pulumi.IntArrayOutput              `pulumi:"instanceIds"`
	Instances   Private_networkInstanceArrayOutput `pulumi:"instances"`
	// The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of
	// 255 characters per Private Network name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The region where the Private Network should be located. Default region is the EU.
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// The name of the region where the Private Network is located.
	RegionName pulumi.StringOutput `pulumi:"regionName"`
	// Time of the last update of the private network.
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewPrivate_network registers a new resource with the given unique name, arguments, and options.
func NewPrivate_network(ctx *pulumi.Context,
	name string, args *Private_networkArgs, opts ...pulumi.ResourceOption) (*Private_network, error) {
	if args == nil {
		args = &Private_networkArgs{}
	}

	var resource Private_network
	err := ctx.RegisterResource("contabo:index/private_network:private_network", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPrivate_network gets an existing Private_network resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrivate_network(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *Private_networkState, opts ...pulumi.ResourceOption) (*Private_network, error) {
	var resource Private_network
	err := ctx.ReadResource("contabo:index/private_network:private_network", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Private_network resources.
type private_networkState struct {
	// The totality of available IPs in the Private Network.
	AvailableIps *int `pulumi:"availableIps"`
	// The cidr range of the Private Network.
	Cidr *string `pulumi:"cidr"`
	// The creation date of the Private Network.
	CreatedDate *string `pulumi:"createdDate"`
	// The specific data center where the Private Network is located.
	DataCenter *string `pulumi:"dataCenter"`
	// The description of the Private Network. There is a limit of 255 characters per Private Network.
	Description *string `pulumi:"description"`
	// Add the instace Ids to the private network here. If you do not add any instance Ids an empty private network will be
	// created.
	InstanceIds []int                     `pulumi:"instanceIds"`
	Instances   []Private_networkInstance `pulumi:"instances"`
	// The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of
	// 255 characters per Private Network name.
	Name *string `pulumi:"name"`
	// The region where the Private Network should be located. Default region is the EU.
	Region *string `pulumi:"region"`
	// The name of the region where the Private Network is located.
	RegionName *string `pulumi:"regionName"`
	// Time of the last update of the private network.
	UpdatedAt *string `pulumi:"updatedAt"`
}

type Private_networkState struct {
	// The totality of available IPs in the Private Network.
	AvailableIps pulumi.IntPtrInput
	// The cidr range of the Private Network.
	Cidr pulumi.StringPtrInput
	// The creation date of the Private Network.
	CreatedDate pulumi.StringPtrInput
	// The specific data center where the Private Network is located.
	DataCenter pulumi.StringPtrInput
	// The description of the Private Network. There is a limit of 255 characters per Private Network.
	Description pulumi.StringPtrInput
	// Add the instace Ids to the private network here. If you do not add any instance Ids an empty private network will be
	// created.
	InstanceIds pulumi.IntArrayInput
	Instances   Private_networkInstanceArrayInput
	// The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of
	// 255 characters per Private Network name.
	Name pulumi.StringPtrInput
	// The region where the Private Network should be located. Default region is the EU.
	Region pulumi.StringPtrInput
	// The name of the region where the Private Network is located.
	RegionName pulumi.StringPtrInput
	// Time of the last update of the private network.
	UpdatedAt pulumi.StringPtrInput
}

func (Private_networkState) ElementType() reflect.Type {
	return reflect.TypeOf((*private_networkState)(nil)).Elem()
}

type private_networkArgs struct {
	// The creation date of the Private Network.
	CreatedDate *string `pulumi:"createdDate"`
	// The description of the Private Network. There is a limit of 255 characters per Private Network.
	Description *string `pulumi:"description"`
	// Add the instace Ids to the private network here. If you do not add any instance Ids an empty private network will be
	// created.
	InstanceIds []int `pulumi:"instanceIds"`
	// The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of
	// 255 characters per Private Network name.
	Name *string `pulumi:"name"`
	// The region where the Private Network should be located. Default region is the EU.
	Region *string `pulumi:"region"`
	// The name of the region where the Private Network is located.
	RegionName *string `pulumi:"regionName"`
	// Time of the last update of the private network.
	UpdatedAt *string `pulumi:"updatedAt"`
}

// The set of arguments for constructing a Private_network resource.
type Private_networkArgs struct {
	// The creation date of the Private Network.
	CreatedDate pulumi.StringPtrInput
	// The description of the Private Network. There is a limit of 255 characters per Private Network.
	Description pulumi.StringPtrInput
	// Add the instace Ids to the private network here. If you do not add any instance Ids an empty private network will be
	// created.
	InstanceIds pulumi.IntArrayInput
	// The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of
	// 255 characters per Private Network name.
	Name pulumi.StringPtrInput
	// The region where the Private Network should be located. Default region is the EU.
	Region pulumi.StringPtrInput
	// The name of the region where the Private Network is located.
	RegionName pulumi.StringPtrInput
	// Time of the last update of the private network.
	UpdatedAt pulumi.StringPtrInput
}

func (Private_networkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*private_networkArgs)(nil)).Elem()
}

type Private_networkInput interface {
	pulumi.Input

	ToPrivate_networkOutput() Private_networkOutput
	ToPrivate_networkOutputWithContext(ctx context.Context) Private_networkOutput
}

func (*Private_network) ElementType() reflect.Type {
	return reflect.TypeOf((**Private_network)(nil)).Elem()
}

func (i *Private_network) ToPrivate_networkOutput() Private_networkOutput {
	return i.ToPrivate_networkOutputWithContext(context.Background())
}

func (i *Private_network) ToPrivate_networkOutputWithContext(ctx context.Context) Private_networkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Private_networkOutput)
}

// Private_networkArrayInput is an input type that accepts Private_networkArray and Private_networkArrayOutput values.
// You can construct a concrete instance of `Private_networkArrayInput` via:
//
//	Private_networkArray{ Private_networkArgs{...} }
type Private_networkArrayInput interface {
	pulumi.Input

	ToPrivate_networkArrayOutput() Private_networkArrayOutput
	ToPrivate_networkArrayOutputWithContext(context.Context) Private_networkArrayOutput
}

type Private_networkArray []Private_networkInput

func (Private_networkArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Private_network)(nil)).Elem()
}

func (i Private_networkArray) ToPrivate_networkArrayOutput() Private_networkArrayOutput {
	return i.ToPrivate_networkArrayOutputWithContext(context.Background())
}

func (i Private_networkArray) ToPrivate_networkArrayOutputWithContext(ctx context.Context) Private_networkArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Private_networkArrayOutput)
}

// Private_networkMapInput is an input type that accepts Private_networkMap and Private_networkMapOutput values.
// You can construct a concrete instance of `Private_networkMapInput` via:
//
//	Private_networkMap{ "key": Private_networkArgs{...} }
type Private_networkMapInput interface {
	pulumi.Input

	ToPrivate_networkMapOutput() Private_networkMapOutput
	ToPrivate_networkMapOutputWithContext(context.Context) Private_networkMapOutput
}

type Private_networkMap map[string]Private_networkInput

func (Private_networkMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Private_network)(nil)).Elem()
}

func (i Private_networkMap) ToPrivate_networkMapOutput() Private_networkMapOutput {
	return i.ToPrivate_networkMapOutputWithContext(context.Background())
}

func (i Private_networkMap) ToPrivate_networkMapOutputWithContext(ctx context.Context) Private_networkMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Private_networkMapOutput)
}

type Private_networkOutput struct{ *pulumi.OutputState }

func (Private_networkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Private_network)(nil)).Elem()
}

func (o Private_networkOutput) ToPrivate_networkOutput() Private_networkOutput {
	return o
}

func (o Private_networkOutput) ToPrivate_networkOutputWithContext(ctx context.Context) Private_networkOutput {
	return o
}

// The totality of available IPs in the Private Network.
func (o Private_networkOutput) AvailableIps() pulumi.IntOutput {
	return o.ApplyT(func(v *Private_network) pulumi.IntOutput { return v.AvailableIps }).(pulumi.IntOutput)
}

// The cidr range of the Private Network.
func (o Private_networkOutput) Cidr() pulumi.StringOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringOutput { return v.Cidr }).(pulumi.StringOutput)
}

// The creation date of the Private Network.
func (o Private_networkOutput) CreatedDate() pulumi.StringOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringOutput { return v.CreatedDate }).(pulumi.StringOutput)
}

// The specific data center where the Private Network is located.
func (o Private_networkOutput) DataCenter() pulumi.StringOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringOutput { return v.DataCenter }).(pulumi.StringOutput)
}

// The description of the Private Network. There is a limit of 255 characters per Private Network.
func (o Private_networkOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Add the instace Ids to the private network here. If you do not add any instance Ids an empty private network will be
// created.
func (o Private_networkOutput) InstanceIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Private_network) pulumi.IntArrayOutput { return v.InstanceIds }).(pulumi.IntArrayOutput)
}

func (o Private_networkOutput) Instances() Private_networkInstanceArrayOutput {
	return o.ApplyT(func(v *Private_network) Private_networkInstanceArrayOutput { return v.Instances }).(Private_networkInstanceArrayOutput)
}

// The name of the Private Network. It may contain letters, numbers, colons, dashes, and underscores. There is a limit of
// 255 characters per Private Network name.
func (o Private_networkOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The region where the Private Network should be located. Default region is the EU.
func (o Private_networkOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringPtrOutput { return v.Region }).(pulumi.StringPtrOutput)
}

// The name of the region where the Private Network is located.
func (o Private_networkOutput) RegionName() pulumi.StringOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringOutput { return v.RegionName }).(pulumi.StringOutput)
}

// Time of the last update of the private network.
func (o Private_networkOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *Private_network) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

type Private_networkArrayOutput struct{ *pulumi.OutputState }

func (Private_networkArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Private_network)(nil)).Elem()
}

func (o Private_networkArrayOutput) ToPrivate_networkArrayOutput() Private_networkArrayOutput {
	return o
}

func (o Private_networkArrayOutput) ToPrivate_networkArrayOutputWithContext(ctx context.Context) Private_networkArrayOutput {
	return o
}

func (o Private_networkArrayOutput) Index(i pulumi.IntInput) Private_networkOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Private_network {
		return vs[0].([]*Private_network)[vs[1].(int)]
	}).(Private_networkOutput)
}

type Private_networkMapOutput struct{ *pulumi.OutputState }

func (Private_networkMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Private_network)(nil)).Elem()
}

func (o Private_networkMapOutput) ToPrivate_networkMapOutput() Private_networkMapOutput {
	return o
}

func (o Private_networkMapOutput) ToPrivate_networkMapOutputWithContext(ctx context.Context) Private_networkMapOutput {
	return o
}

func (o Private_networkMapOutput) MapIndex(k pulumi.StringInput) Private_networkOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Private_network {
		return vs[0].(map[string]*Private_network)[vs[1].(string)]
	}).(Private_networkOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*Private_networkInput)(nil)).Elem(), &Private_network{})
	pulumi.RegisterInputType(reflect.TypeOf((*Private_networkArrayInput)(nil)).Elem(), Private_networkArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*Private_networkMapInput)(nil)).Elem(), Private_networkMap{})
	pulumi.RegisterOutputType(Private_networkOutput{})
	pulumi.RegisterOutputType(Private_networkArrayOutput{})
	pulumi.RegisterOutputType(Private_networkMapOutput{})
}