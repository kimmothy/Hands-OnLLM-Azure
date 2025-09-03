terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "=4.41.0"
    }
    http = {

    }
  }
}

provider "azurerm" {
  features {

  }
  subscription_id = var.sub_id
  
}

resource "azurerm_resource_group" "ai_foundry_rg" {
    name = "rg-chan-test-aifoundry"
    location = "koreacentral"
    

}


resource "azurerm_ai_services" "ai_foundry_service" {
  name = "ais-${var.region_code}-${var.prj_code}-${var.env_code}"
  resource_group_name = azurerm_resource_group.ai_foundry_rg.name
  location = var.region
  sku_name = "S0"
  public_network_access = "Enabled"
  custom_subdomain_name = "ais-${var.region_code}-${var.prj_code}-${var.env_code}"

  network_acls {
    default_action = "Deny"
    ip_rules = [data.http.ip.response_body]
    
  }
  
  identity {
    type = "SystemAssigned"
  }
  
}