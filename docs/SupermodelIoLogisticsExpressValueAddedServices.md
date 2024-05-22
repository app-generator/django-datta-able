# SupermodelIoLogisticsExpressValueAddedServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_code** | **str** | Please enter DHL Express value added service code. For detailed list of all available service codes for your prospect shipment please invoke GET /products or GET /rates | 
**value** | **float** | Please enter monetary value of service (e.g. Insured Value) | [optional] 
**currency** | **str** | Please enter currency code (e.g. Insured Value currency code) | [optional] 
**method** | **str** | Payment method code (e.g. Cash) | [optional] 
**dangerous_goods** | [**List[SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner]**](SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner.md) | The DangerousGoods section indicates if there is dangerous good content within the shipment. &lt;BR&gt; The ContentID node contains the Content ID for Dangerous Good classification. &lt;BR&gt; It is required to provide the dangerous good Content ID for every dangerous good special service provided, and vice versa. &lt;BR&gt; For the complete list of dangerous goods Content IDs and dangerous goods special services combinations, refer to Reference Data Guide section 5. valueAddedServicesDefinition\\\\dangerousGoods. &lt;BR&gt; Note: Please contact your DHL Express IT representative if additional assistance is required.&lt;BR&gt;&lt;BR&gt; For dangerous goods shipment with Dry Ice example: UN1845 (Content ID: 901), additional node must be populated &#39;dryIceTotalNetWeight.&#39;&lt;BR&gt; For dangerous goods shipment with &#39;Excepted Quantities&#39;, additional node must be populated &#39;unCodes&#39;. Few scenarios guideline to prepare a Dangerous Goods shipment for:&lt;BR&gt;&lt;BR&gt; A) Dry Ice: &lt;BR&gt; 1.&#39;serviceCode&#39; element must contain value of &#39;HC&#39;&lt;BR&gt; 2.&#39;contentID&#39; element consists of &#39;901&#39;&lt;BR&gt; 3.&#39;dryIceTotalNetWeight&#39; element consists of the total net weight of the dry ice in &#39;unitofMeasurement&#39; &lt;BR&gt;&lt;BR&gt; B) Lithium Battery: &lt;BR&gt; 1.&#39;serviceType&#39; element must contain value of &#39;HD&#39;, &#39;HM&#39;, &#39;HV&#39; or &#39;HW&#39;&lt;BR&gt; 2.&#39;contentID&#39; element consists of &#39;966&#39;, &#39;969&#39;, &#39;967&#39;, &#39;970&#39; respectively&lt;BR&gt;&lt;BR&gt; C) Excepted Quantities:&lt;BR&gt; 1.&#39;serviceCode&#39; element must contain value of &#39;HH&#39;&lt;BR&gt; 2.&#39;contentID&#39; element consists of &#39;E01&lt;BR&gt; 3.&#39;unCodes&#39; element consists of the UN code associate with it.&lt;BR&gt; | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_value_added_services import SupermodelIoLogisticsExpressValueAddedServices

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressValueAddedServices from a JSON string
supermodel_io_logistics_express_value_added_services_instance = SupermodelIoLogisticsExpressValueAddedServices.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressValueAddedServices.to_json())

# convert the object into a dict
supermodel_io_logistics_express_value_added_services_dict = supermodel_io_logistics_express_value_added_services_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressValueAddedServices from a dict
supermodel_io_logistics_express_value_added_services_from_dict = SupermodelIoLogisticsExpressValueAddedServices.from_dict(supermodel_io_logistics_express_value_added_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


