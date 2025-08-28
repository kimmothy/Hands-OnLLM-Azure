terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "=4.41.0"
    }
  }
}

resource "azurerm_resource_group" "ai_foundry_rg" {
    name = "rg-chan-test-aifoundry"
    location = "koreacentral"

}

# resource "azurerm_key_vault" "ai_foundry_kv" {
#   name                = "kv-chan-test-aifoundry"
#   location            = azurerm_resource_group.ai_foundry_rg.location
#   resource_group_name = azurerm_resource_group.ai_foundry_rg.name
#   tenant_id           = data.azurerm_client_config.current.tenant_id
#   enable_rbac_authorization = true
#   public_network_access_enabled = false

#   sku_name                 = "standard"
#   purge_protection_enabled = true

# }

# resource "azurerm_storage_account" "ai_foundry_str" {
#   name                     = "strchantestaifoundry"
#   location            = azurerm_resource_group.ai_foundry_rg.location
#   resource_group_name = azurerm_resource_group.ai_foundry_rg.name
#   account_tier             = "Standard"
#   account_replication_type = "LRS"
#   public_network_access_enabled = false
# }

resource "azurerm_ai_services" "ai_foundry_service" {
  name = "ais-kc-chan-test"
  resource_group_name = azurerm_resource_group.ai_foundry_rg.name
  location = var.region
  sku_name = "S0"
  
}