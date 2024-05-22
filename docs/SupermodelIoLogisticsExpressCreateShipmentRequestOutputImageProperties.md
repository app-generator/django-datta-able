# SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties

Here you can modify label, waybillDoc, invoice and shipment receipt properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer_dpi** | **float** | Printer DPI Resolution for X-axis and Y-axis (in DPI) for transport label and waybill document output | [optional] 
**customer_barcodes** | [**List[SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesCustomerBarcodesInner]**](SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesCustomerBarcodesInner.md) | Customer barcodes to be printed on supported transport label templates | [optional] 
**customer_logos** | [**List[SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesCustomerLogosInner]**](SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesCustomerLogosInner.md) | Customer Logo Image to be printed on transport label | [optional] 
**encoding_format** | **str** | Please provide the format of the output documents. Note that invoice and shipment receipt will always come back as PDF | [optional] [default to 'pdf']
**image_options** | [**List[SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner]**](SupermodelIoLogisticsExpressCreateShipmentRequestOutputImagePropertiesImageOptionsInner.md) | Here the image options are defined for label, waybillDoc, invoice, QRcode and shipment receipt | [optional] 
**split_transport_and_waybill_doc_labels** | **bool** | When set to true it will generate a single PDF or thermal output file for the Transport Label, a single PDF or thermal output file for the Waybill document and a single PDF file consisting of Commercial Invoice and Shipment Receipt. The default value is false, a single PDF or thermal output image file consists of Transport Label and single PDF or thermal output image file for Waybill Document will be returned in create shipment response. | [optional] 
**all_documents_in_one_image** | **bool** | When set to true it will generate a single PDF or thermal output image file consists of Transport Label, Waybill Document, Shipment Receipt and Commercial Invoice.&lt;BR&gt;          The default value is false, where a single PDF or thermal output image file consists of Transport Label + Waybill Document and single PDF or thermal output image file for Shipment Receipt and Customs Invoice will be returned. | [optional] 
**split_documents_by_pages** | **bool** | When set to true it will generate a single PDF or thermal output image file for each page for the Transport Label and single PDF or thermal output image file for Waybill Document will be returned in the create shipment response. The default value is false, a single PDF or thermal output image file for each page for Transport Label and single PDF or thermal output image file for Waybill Document will be returned in create shipment response. | [optional] 
**split_invoice_and_receipt** | **bool** | When set to true it will generate a single PDF or thermal output image file consisting of Transport Label + Waybill Document, a single file consist of Commercial Invoice and a single file consist of Shipment Receipt. The default value is false, a single PDF or thermal output image file consists of Transport Label + Waybill Document and single PDF or thermal output image file for Shipment Receipt and Customs Invoice will be returned in create shipment response. | [optional] 
**receipt_and_labels_in_one_image** | **bool** | When set to true it will generate a single PDF file consisting of Transport Label, Waybill Document and Shipment Receipt. The default value is false, a single PDF or thermal output image file consists of Transport Label + Waybill Document and single PDF file for Shipment Receipt will be returned in create shipment response.  Applicable only when #/outputImageProperties/imageOptions/0/typeCode is &#39;receipt&#39; and #/outputImageProperties/encodingFormat is PDF. | [optional] 

## Example

```python
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_output_image_properties import SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties

# TODO update the JSON string below
json = "{}"
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties from a JSON string
supermodel_io_logistics_express_create_shipment_request_output_image_properties_instance = SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties.from_json(json)
# print the JSON string representation of the object
print(SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties.to_json())

# convert the object into a dict
supermodel_io_logistics_express_create_shipment_request_output_image_properties_dict = supermodel_io_logistics_express_create_shipment_request_output_image_properties_instance.to_dict()
# create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties from a dict
supermodel_io_logistics_express_create_shipment_request_output_image_properties_from_dict = SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties.from_dict(supermodel_io_logistics_express_create_shipment_request_output_image_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


