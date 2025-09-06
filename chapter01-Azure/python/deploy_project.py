from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
from dotenv import load_dotenv

subscription_id = load_dotenv("subs_id")
resource_group_name = load_dotenv("rg_name")
foundry_resource_name = load_dotenv("ai_foundry_service_name")
foundry_project_name = 'myprj'
location = 'koreacentral'

#########################################################################
# Default Azure Credential 함수를 사용하면 실행 환경에 따라 가능한 인증방법을 사용하여 인증하게 됩니다.
# terraform을 실행할 때 az login 명령을 실행했기 때문에 일반적으론 CLI 인증을 사용하게 됩니다.
# 이 코드에선 인증 과정을 가시적으로 경험하기 위해 Interactive Brouser Credential을 사용합니다.
#########################################################################
client = CognitiveServicesManagementClient(
    # credential=DefaultAzureCredential(), 
    credential=InteractiveBrowserCredential(), 
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