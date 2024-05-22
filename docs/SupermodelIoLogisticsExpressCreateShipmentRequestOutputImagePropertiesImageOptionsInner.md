# SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Please enter the document type you want to wish set properties for | 
**template_name** | **str** | Please enter DHL Express document template name. &lt;BR&gt;                Sample Transport label templates:&lt;BR&gt;                ECOM26_84_A4_001 &lt;BR&gt;                ECOM26_84_001 - default&lt;BR&gt;                ECOM_TC_A4&lt;BR&gt;                ECOM26_A6_002&lt;BR&gt;                ECOM26_84CI_001&lt;BR&gt;                ECOM26_84CI_002 - supported single customer barcode&lt;BR&gt;                ECOM26_84CI_003 - to be used if customer barcodes are used&lt;BR&gt;                ECOM_A4_RU_002&lt;BR&gt; ECOM26_84_LBBX_001 - supported for loose BBX shipment&lt;BR&gt; ECOM26_64_LBBX_001 - supported for loose BBX shipment&lt;BR&gt;Sample WaybillDoc templates&lt;BR&gt;                ARCH_8X4_A4_002&lt;BR&gt;                ARCH_8X4 - default&lt;BR&gt;                ARCH_6X4&lt;BR&gt;                ARCH_A4_RU_002&lt;BR&gt;                &lt;BR&gt;                Sample Commercial invoice templates:&lt;BR&gt;                COMMERCIAL_INVOICE_04 - This template can print the Shipper, Recipient, and Buyer and Importer address details and is on portrait orientation, exclusive use for preparing Loose BBX shipment.&lt;BR&gt;                COMMERCIAL_INVOICE_P_10 - (default) This template can print the Shipper, Recipient and upto two more additional address details in portrait orientation. Note: If customer provided more than four address roles in the request message and this template is selected, the rendered invoice will only contain four address roles based on order of priority: Shipper, Recipient, Seller, Importer, Exporter, Buyer. &lt;BR&gt;                COMMERCIAL_INVOICE_L_10 - This template can print the Shipper,Recipient, Buyer, and Importer and Exporter address details and is on landscape orientation..&lt;BR&gt;                RET_COM_INVOICE_A4_01 - This template can print the Shipper, Recipient and Importer of record address details and is on landscape orientation. This template is for exclusive use for certain shipment where the goods are actual &#39;returns&#39;. The Shipper is the party that earlier has received the goods, but now wishes to return the goods to its originating party. The Recipient in this shipment scenario will receive the &#39;returned goods&#39;. Therefore such request of shipment with an invoice rendering may utilize the specific invoice template for &#39;Returns Invoice&#39;.&lt;BR&gt;                &lt;BR&gt;                Sample Shipment Receipt template&lt;BR&gt;                SHIP_RECPT_A4_RU_002&lt;BR&gt; SHIPRCPT_EN_001 - default &lt;BR&gt; &lt;BR&gt; Sample QR Code template template&lt;BR&gt;  QR_1_00_LL_PNG_001 - default | [optional] 
**is_requested** | **bool** | To be used for waybillDoc, invoice, shipment receipt and QRcode. If set to true then the document is provided otherwise not | [optional] 
**hide_account_number** | **bool** | To be used for waybillDoc. If set to true then account information will not be printed on the waybillDoc | [optional] 
**number_of_copies** | **float** | You can ask up to 2 waybillDoc copies to be provided | [optional] 
**invoice_type** | **str** | Please advise what type of customs documentation is required | [optional] 
**language_code** | **str** | Please enter ISO 3 letters language code for invoice or shipment receipt | [optional] 
**language_country_code** | **str** | Please enter ISO 2 letters language country code for invoice or shipment receipt | [optional] 
**language_script_code** | **str** | Please enter ISO 4 letters language script code for shipment receipt | [optional] 
**encoding_format** | **str** | Please provide the format of the QR Code output format. | [optional] 
**render_dhl_logo** | **bool** | DHL Logo to be printed in Transport Label or Waybill Document | [optional] 
**fit_labels_to_a4** | **bool** | To print respective Transport Label and Waybill document into A4 margin PDF.&lt;BR&gt;                Note: ECOM26_A6_002,ECOM26_84CI_001,ECOM26_84CI_002,ARCH_6X4,ARCH_8X4 template. &lt;BR&gt;                This option is applicable only for PDF encodingFormat selection.&lt;BR&gt;                false: Transport Label and Waybill document will use default margin settings (default behavior) &lt;BR&gt;                true: Transport Label and Waybill document will print into A4 margin PDF | [optional] 
**label_free_text** | **str** | Additional customer label free text that can be printed in certain label.Note: Applicable only to ECOM26_A6_002, ECOM_TC_A4 and ECOM26_84CI_001. | [optional] 
**label_customer_data_text** | **str** | Additional customer label text that can be printed in certain label.Note: Applicable only to ECOM26_84_A4_001, ECOM_TC_A4 and ECOM26_84CI_001 | [optional] 
**shipment_receipt_customer_data_text** | **str** | Declaration text that can be printed in certain shipment receipt template | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_output_image_properties_image_options_inner import SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner from a JSON string
supermodel_io_logistics_express_create_shipment_request_output_image_properties_image_options_inner_instance = SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_output_image_properties_image_options_inner_dict = supermodel_io_logistics_express_create_shipment_request_output_image_properties_image_options_inner_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner from a dict
supermodel_io_logistics_express_create_shipment_request_output_image_properties_image_options_inner_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner.from_dict(supermodel_io_logistics_express_create_shipment_request_output_image_properties_image_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


