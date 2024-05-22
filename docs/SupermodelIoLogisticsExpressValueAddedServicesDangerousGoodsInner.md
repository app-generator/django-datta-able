# SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | **str** | Please enter valid DHL Express Dangerous good content id (please contact your DHL Express IT representative for the relevant content ID code if you are shipping Dan | 
**dry_ice_total_net_weight** | **float** | Please enter dry ice total net weight when shipping dry ice | [optional] 
**custom_description** | **str** | The customDescription node contains the customized Dangerous Goods statement to declare contents accurately. The customDescription node value will be displayed in the Transport Label and Waybill Document, replacing the default IATA Dangerous Goods statement constructed based on contentId node.&lt;BR&gt;            Multiple customDescription nodes from multiple dangerousGoods nodes will be concatenated using comma separator with combined maximum limit of 200 characters.&lt;BR&gt;            &lt;BR&gt;            It is recommended to use customDescription for entire shipment for each dangerousGoods to fully utilize customDescription printout in Transport Label and Waybill Document.&lt;BR&gt;            &lt;BR&gt;            Note: For &#39;customDescription&#39; usage, ensure all &#39;dangerousGoods&#39; segments are including the &#39;customDescription&#39; field value. Any of the dangerousGoods does not provide with customDescription field value will be ignored from printing in Transport Label and Waybill Document.   | [optional] 
**un_codes** | **List[str]** | Please enter UN code(s) | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_value_added_services_dangerous_goods_inner import SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner from a JSON string
supermodel_io_logistics_express_value_added_services_dangerous_goods_inner_instance = SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_value_added_services_dangerous_goods_inner_dict = supermodel_io_logistics_express_value_added_services_dangerous_goods_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner from a dict
supermodel_io_logistics_express_value_added_services_dangerous_goods_inner_from_dict = SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner.from_dict(supermodel_io_logistics_express_value_added_services_dangerous_goods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


