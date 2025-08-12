param containerName string
param imageName string
param registryLoginServer string
param registryUsername string
@secure()
param registryPassword string
param location string = resourceGroup().location
param cpu double = 1
param memory double = 1.5
param port int = 8080
param appEnv string = 'dev'
param appVersion string = '1.0.0'

resource containerGroup 'Microsoft.ContainerInstance/containerGroups@2023-05-01' = {
  name: containerName
  location: location
  properties: {
    osType: 'Linux'
    containers: [
      {
        name: containerName
        properties: {
          image: imageName
          ports: [ { port: port, protocol: 'TCP' } ]
          resources: { requests: { cpu: cpu, memoryInGB: memory } }
          environmentVariables: [
            { name: 'APP_ENV', value: appEnv },
            { name: 'APP_VERSION', value: appVersion },
            { name: 'PORT', value: string(port) }
          ]
        }
      }
    ]
    imageRegistryCredentials: [
      { server: registryLoginServer, username: registryUsername, password: registryPassword }
    ]
    ipAddress: {
      type: 'Public'
      ports: [ { port: port, protocol: 'TCP' } ]
      dnsNameLabel: '${containerName}-${uniqueString(resourceGroup().id)}'
    }
  }
}
output url string = 'http://' + containerGroup.properties.ipAddress.fqdn + ':' + string(port)
