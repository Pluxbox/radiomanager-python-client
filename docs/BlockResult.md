# BlockResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the current Block. | 
**broadcast_id** | **int** | Currently assigned Broadcast connected to the current Block, identified by the Broadcast ID. | 
**start** | **datetime** | Start of the Block (formatted as a DateTime object), saved with an TimeZone. | 
**stop** | **datetime** | End of the Block (formatted as a DateTime object), saved with an TimeZone. | 
**created_at** | **datetime** | Time of the creation of the Block (formatted as a DateTime object), saved with an TimeZone. | 
**updated_at** | **datetime** | Time of the last update of the Block (formatted as a DateTime object), saved with an TimeZone. | 
**deleted_at** | **datetime** | Moment when the Block got deleted (formatted as a DateTime object), saved with an TimeZone. | 
**external_station_id** | **int** |  | [optional] 
**items** | [**BlockRelationsItems**](BlockRelationsItems.md) |  | [optional] 
**broadcast** | [**BlockRelationsBroadcast**](BlockRelationsBroadcast.md) |  | [optional] 
**program** | [**BlockRelationsProgram**](BlockRelationsProgram.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


