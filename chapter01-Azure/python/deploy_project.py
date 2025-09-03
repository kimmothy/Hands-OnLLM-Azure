from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
from dotenv import load_dotenv


subscription_id = load_dotenv("subs_id")
resource_group_name = load_dotenv("rg_name")
foundry_resource_name = load_dotenv("ai_foundry_service_name")
foundry_project_name = 'myprj'
location = 'koreacentral'

client = CognitiveServicesManagementClient(
    credential=DefaultAzureCredential(), 
    subscription_id=subscription_id,
    api_version="2025-04-01-preview"
)

# Create resource
# resource = client.accounts.begin_create(
#     resource_group_name=resource_group_name,
#     account_name=foundry_resource_name,
#     account={
#         "location": location,
#         "kind": "AIServices",
#         "sku": {"name": "S0",},
#         "identity": {"type": "SystemAssigned"},
#         "properties": {
#             "allowProjectManagement": True,
#             "customSubDomainName": foundry_resource_name
#         }
#     }
# )

# Wait for the resource creation to complete
# resource_result = resource.result()

# Create default project
project = client.projects.begin_create(
    resource_group_name=resource_group_name,
    account_name=foundry_resource_name,
    project_name=foundry_project_name,
    project={
        "location": location,
        "identity": {
            "type": "SystemAssigned"
        },
        "properties": {}
    }
)