# output "sub_id" {
#     value = data.azurerm_client_config.current.subscription_id
# }

# output "rg_name" {
#     value = azurerm_resource_group.ai_foundry_rg.name
  
# }

# output "ai_foundry_name" {
#     value = azurerm_ai_services.ai_foundry_service.name
  
# }

resource "local_file" "dotenv_file" {
    content = "subs_id=${data.azurerm_client_config.current.subscription_id}\nrg_name=${azurerm_resource_group.ai_foundry_rg.name}\nai_foundry_service_name=${azurerm_ai_services.ai_foundry_service.name}"
    filename = "../python/.env"
}