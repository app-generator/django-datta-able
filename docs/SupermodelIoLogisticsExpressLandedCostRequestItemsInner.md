# SupermodelIoLogisticsExpressLandedCostRequestItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **float** | Line item number | 
**name** | **str** | Name of the item | [optional] 
**description** | **str** | Item full description | [optional] 
**manufacturer_country** | **str** | ISO Country code of the goods manufacturer | [optional] 
**part_number** | **str** | SKU number | [optional] 
**quantity** | **float** | Total quantity of the item(s) to be shipped. | 
**quantity_type** | **str** | Please provide quantitiy type. prt - part, box - box | [optional] 
**unit_price** | **float** | Product Unit price | 
**unit_price_currency_code** | **str** | Currency code of the Unit Price | 
**customs_value** | **float** | not used | [optional] 
**customs_value_currency_code** | **str** | not used | [optional] 
**commodity_code** | **str** | commodityCode is mandatory if estimatedTariffRateType (&#39;derived_rate&#39; or &#39;highest_rate&#39; or &#39;lowest_rate&#39; or &#39;center_rate&#39;) not provided in the request otherwise it is considered as Optional.&lt;BR&gt;                              &#39;highest_rate&#39; or &#39;lowest_rate&#39; or &#39;center_rate&#39;) not provided in the request otherwise it is considered as Optional.&lt;BR&gt;            Can be provided with or without dots | [optional] 
**weight** | **float** | Weight of the item | [optional] 
**weight_unit_of_measurement** | **str** | Unit of measurement | [optional] 
**category** | **str** | commodityCode category can be retrieved via referenceData API/ commodityCategory dataset.&lt;BR&gt; Category code of the Item.&lt;BR&gt;            101 - Coats &amp; Jacket&lt;BR&gt;            102 - Blazers&lt;BR&gt;            103 - Suits&lt;BR&gt;            104 - Ensembles&lt;BR&gt;            105 - Trousers&lt;BR&gt;            106 - Shirts &amp; Blouses&lt;BR&gt;            107 - Dresses&lt;BR&gt;            108 - Skirts&lt;BR&gt;            109 - Jerseys, Sweatshirts &amp; Pullovers&lt;BR&gt;            110 - Sports &amp; Swimwear&lt;BR&gt;            111 - Night &amp; Underwear&lt;BR&gt;            112 - T-Shirts&lt;BR&gt;            113 - Tights &amp; Leggings&lt;BR&gt;            114 - Socks &lt;BR&gt;            115 - Baby Clothes&lt;BR&gt;            116 - Clothing Accessories&lt;BR&gt;            201 - Sneakers&lt;BR&gt;            202 - Athletic Footwear&lt;BR&gt;            203 - Leather Footwear&lt;BR&gt;            204 - Textile &amp; Other Footwear&lt;BR&gt;            301 - Spectacle Lenses&lt;BR&gt;            302 - Sunglasses&lt;BR&gt;            303 - Eyewear Frames&lt;BR&gt;            304 - Contact Lenses&lt;BR&gt;            401 - Watches&lt;BR&gt;            402 - Jewelry&lt;BR&gt;            403 - Suitcases &amp; Briefcases&lt;BR&gt;            404 - Handbags&lt;BR&gt;            405 - Wallets &amp; Little Cases&lt;BR&gt;            406 - Bags &amp; Containers&lt;BR&gt;            501 - Beer&lt;BR&gt;            502 - Spirits&lt;BR&gt;            503 - Wine&lt;BR&gt;            504 - Cider, Perry &amp; Rice Wine&lt;BR&gt;            601 - Bottled Water&lt;BR&gt;            602 - Soft Drinks&lt;BR&gt;            603 - Juices&lt;BR&gt;            604 - Coffee&lt;BR&gt;            605 - Tea&lt;BR&gt;            606 - Cocoa&lt;BR&gt;            701 - Dairy Products &amp; Eggs&lt;BR&gt;            702 - Meat&lt;BR&gt;            703 - Fish &amp; Seafood&lt;BR&gt;            704 - Fruits &amp; Nuts&lt;BR&gt;            705 - Vegetables&lt;BR&gt;            706 - Bread &amp; Cereal Products&lt;BR&gt;            707 - Oils &amp; Fats&lt;BR&gt;            708 - Sauces &amp; Spices&lt;BR&gt;            709 - Convenience Food&lt;BR&gt;            710 - Spreads &amp; Sweeteners&lt;BR&gt;            711 - Baby Food&lt;BR&gt;            712 - Pet Food&lt;BR&gt;            801 - Cigarettes&lt;BR&gt;            802 - Smoking Tobacco&lt;BR&gt;            803 - Cigars&lt;BR&gt;            804 - E-Cigarettes&lt;BR&gt;            901 - Household Cleaners&lt;BR&gt;            902 - Dishwashing Detergents&lt;BR&gt;            903 - Polishes&lt;BR&gt;            904 - Room Scents&lt;BR&gt;            905 - Insecticides&lt;BR&gt;            1001 - Cosmetics&lt;BR&gt;            1002 - Skin Care&lt;BR&gt;            1003 - Personal Care&lt;BR&gt;            1004 - Fragrances&lt;BR&gt;            1101 - Toilet Paper&lt;BR&gt;            1102 - Paper Tissues&lt;BR&gt;            1103 - Household Paper&lt;BR&gt;            1104 - Feminine Hygiene&lt;BR&gt;            1105 - Baby Diapers&lt;BR&gt;            1106 - Incontinence&lt;BR&gt;            1202 - TV, Radio &amp; Multimedia&lt;BR&gt;            1203 - TV Peripheral Devices&lt;BR&gt;            1204 - Telephony&lt;BR&gt;            1205 - Computing&lt;BR&gt;            1206 - Drones&lt;BR&gt;            1301 - Refrigerators&lt;BR&gt;            1302 - Freezers&lt;BR&gt;            1303 - Dishwashing Machines&lt;BR&gt;            1304 - Washing Machines&lt;BR&gt;            1305 - Cookers &amp; Oven&lt;BR&gt;            1306 - Vacuum Cleaners&lt;BR&gt;            1307 - Small Kitchen Appliances&lt;BR&gt;            1308 - Hair Clippers&lt;BR&gt;            1309 - Irons&lt;BR&gt;            1310 - Toasters&lt;BR&gt;            1311 - Grills &amp; Roasters&lt;BR&gt;            1312 - Hair Dryers&lt;BR&gt;            1313 - Coffee Machines&lt;BR&gt;            1314 - Microwave Ovens&lt;BR&gt;            1315 - Electric Kettles&lt;BR&gt;            1401 - Seats &amp; Sofas&lt;BR&gt;            1402 - Beds&lt;BR&gt;            1403 - Mattresses&lt;BR&gt;            1404 - Closets, Nightstands &amp; Dressers&lt;BR&gt;            1405 - Lamps &amp; Lighting&lt;BR&gt;            1406 - Floor Covering&lt;BR&gt;            1407 - Kitchen Furniture&lt;BR&gt;            1408 - Plastic &amp; Other Furniture&lt;BR&gt;            1501 - Analgesics&lt;BR&gt;            1502 - Cold &amp; Cough Remedies&lt;BR&gt;            1503 - Digestives &amp; Intestinal Remedies&lt;BR&gt;            1504 - Skin Treatment&lt;BR&gt;            1505 - Vitamins &amp; Minerals&lt;BR&gt;            1506 - Hand Sanitizer &lt;BR&gt;            1601 - Toys &amp; Games&lt;BR&gt;            1602 - Musical Instruments&lt;BR&gt;            1603 - Sports Equipment | [optional] 
**brand** | **str** | Item&#39;s brand | [optional] 
**goods_characteristics** | [**List[SupermodelIoLogisticsExpressLandedCostRequestItemsInnerGoodsCharacteristicsInner]**](SupermodelIoLogisticsExpressLandedCostRequestItemsInnerGoodsCharacteristicsInner.md) |  | [optional] 
**additional_quantity_definitions** | [**List[SupermodelIoLogisticsExpressLandedCostRequestItemsInnerAdditionalQuantityDefinitionsInner]**](SupermodelIoLogisticsExpressLandedCostRequestItemsInnerAdditionalQuantityDefinitionsInner.md) |  | [optional] 
**estimated_tariff_rate_type** | **str** | Please enter Tariff Rate Type - default_rate,derived_rate,highest_rate,center_rate,lowest_rate | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_landed_cost_request_items_inner import SupermodelIoLogisticsExpressLandedCostRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressLandedCostRequestItemsInner from a JSON string
supermodel_io_logistics_express_landed_cost_request_items_inner_instance = SupermodelIoLogisticsExpressLandedCostRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressLandedCostRequestItemsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_landed_cost_request_items_inner_dict = supermodel_io_logistics_express_landed_cost_request_items_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressLandedCostRequestItemsInner from a dict
supermodel_io_logistics_express_landed_cost_request_items_inner_from_dict = SupermodelIoLogisticsExpressLandedCostRequestItemsInner.from_dict(supermodel_io_logistics_express_landed_cost_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


