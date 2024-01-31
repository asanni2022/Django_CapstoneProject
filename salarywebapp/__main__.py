import pulumi
from pulumi_azure_native import web, resources

# Create an Azure Resource Group
resource_group = resources.ResourceGroup('capstoneprojects')

# Define an App Service Plan
app_service_plan = web.AppServicePlan(
    'salaryappserviceplan',
    resource_group_name=resource_group.name,
    kind='Linux',
    reserved=True,  # For Linux, must be true
    sku={'name': 'B1', 'tier': 'Basic'}
)

# Define the Web App
app = web.WebApp(
    'salaryappwebapp',
    resource_group_name=resource_group.name,
    server_farm_id=app_service_plan.id,
    site_config=web.SiteConfigArgs(
        app_settings=[
            web.NameValuePairArgs(name='WEBSITES_PORT', value='8000'),
            # Define other environment variables here
        ],
        linux_fx_version=f'DOCKER|asanni2022/salary_app:v1.0'  # My Docker image
    ),
    https_only=True
)

pulumi.export('endpoint', app.default_host_name)
