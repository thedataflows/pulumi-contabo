# Contabo Resource Provider

The Contabo Resource Provider lets you manage [contabo](https://contabo.com/en) resources. It is based on <https://github.com/contabo/terraform-provider-contabo>.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumi/contabo
```

or `yarn`:

```bash
yarn add @pulumi/contabo
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_contabo
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/thedataflows/pulumi-contabo/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.contabo
```

## Configuration

The following configuration points are available for the `contabo` provider:

- `contabo:oauth2_client_id` (environment: `CONTABO_OAUTH2_CLIENT_ID`)
- `contabo:oauth2_client_secret` (environment: `CONTABO_OAUTH2_CLIENT_SECRET`)
- `contabo:oauth2_user` (environment: `CONTABO_OAUTH2_USER`)
- `contabo:oauth2_pass` (environment: `CONTABO_OAUTH2_PASS`)

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/contabo/api-docs/).
