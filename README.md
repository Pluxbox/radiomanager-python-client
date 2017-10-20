# Pluxbox RadioManager Client
RadioManager

- API version: 2.0
For more information, please visit [https://pluxbox.com](https://pluxbox.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

To install the python package, run the following command:

```sh
pip install Pluxbox-RadioManager-Python-SDK
```
Then import the package:
```python
import radiomanager_sdk 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import radiomanager_sdk
from radiomanager_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
radiomanager_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# radiomanager_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'
# create an instance of the API class
api_instance = radiomanager_sdk.BlockApi()
id = 789 # int | ID of Block **(Required)**
external_station_id = 789 # int | Query on a different (content providing) station *(Optional)* (optional)

try:
    # Get block by id
    api_response = api_instance.get_block_by_id(id, external_station_id=external_station_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->get_block_by_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://staging.radiomanager.io/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BlockApi* | [**get_block_by_id**](docs/BlockApi.md#get_block_by_id) | **GET** /blocks/{id} | Get block by id
*BlockApi* | [**get_current_block**](docs/BlockApi.md#get_current_block) | **GET** /blocks/current | Get current Block
*BlockApi* | [**get_next_block**](docs/BlockApi.md#get_next_block) | **GET** /blocks/next | Get next Block
*BlockApi* | [**list_blocks**](docs/BlockApi.md#list_blocks) | **GET** /blocks | Get a list of all blocks currently in your station.
*BroadcastApi* | [**create_broadcast**](docs/BroadcastApi.md#create_broadcast) | **POST** /broadcasts | Create broadcast.
*BroadcastApi* | [**delete_broadcast_by_id**](docs/BroadcastApi.md#delete_broadcast_by_id) | **DELETE** /broadcasts/{id} | Delete broadcast by id
*BroadcastApi* | [**get_broadcast_by_id**](docs/BroadcastApi.md#get_broadcast_by_id) | **GET** /broadcasts/{id} | Get broadcast by id
*BroadcastApi* | [**get_current_broadcast**](docs/BroadcastApi.md#get_current_broadcast) | **GET** /broadcasts/current | Get current Broadcast
*BroadcastApi* | [**get_daily_epg**](docs/BroadcastApi.md#get_daily_epg) | **GET** /broadcasts/epg/daily | Get daily EPG
*BroadcastApi* | [**get_epg_by_date**](docs/BroadcastApi.md#get_epg_by_date) | **GET** /broadcasts/epg | Get EPG by date
*BroadcastApi* | [**get_next_broadcast**](docs/BroadcastApi.md#get_next_broadcast) | **GET** /broadcasts/next | Get next Broadcast
*BroadcastApi* | [**get_weekly_epg**](docs/BroadcastApi.md#get_weekly_epg) | **GET** /broadcasts/epg/weekly | Get weekly EPG
*BroadcastApi* | [**list_broadcasts**](docs/BroadcastApi.md#list_broadcasts) | **GET** /broadcasts | Get all broadcasts.
*BroadcastApi* | [**print_broadcast_by_id**](docs/BroadcastApi.md#print_broadcast_by_id) | **GET** /broadcasts/print/{id} | Print Broadcast by id
*BroadcastApi* | [**update_broadcast_by_id**](docs/BroadcastApi.md#update_broadcast_by_id) | **PATCH** /broadcasts/{id} | Update broadcast by id
*CampaignApi* | [**create_campaign**](docs/CampaignApi.md#create_campaign) | **POST** /campaigns | Create campaign.
*CampaignApi* | [**delete_campaign_by_id**](docs/CampaignApi.md#delete_campaign_by_id) | **DELETE** /campaigns/{id} | Delete campaign by id
*CampaignApi* | [**get_campaign_by_id**](docs/CampaignApi.md#get_campaign_by_id) | **GET** /campaigns/{id} | Get campaign by id
*CampaignApi* | [**list_campaigns**](docs/CampaignApi.md#list_campaigns) | **GET** /campaigns | Get all campaigns.
*CampaignApi* | [**update_campaign_by_id**](docs/CampaignApi.md#update_campaign_by_id) | **PATCH** /campaigns/{id} | Update campaign by id
*ContactApi* | [**create_contact**](docs/ContactApi.md#create_contact) | **POST** /contacts | Create contact.
*ContactApi* | [**delete_contact_by_id**](docs/ContactApi.md#delete_contact_by_id) | **DELETE** /contacts/{id} | Delete contact by id
*ContactApi* | [**get_contact_by_id**](docs/ContactApi.md#get_contact_by_id) | **GET** /contacts/{id} | Get contact by id
*ContactApi* | [**list_contacts**](docs/ContactApi.md#list_contacts) | **GET** /contacts | Get all contacts.
*ContactApi* | [**update_contact_by_id**](docs/ContactApi.md#update_contact_by_id) | **PATCH** /contacts/{id} | Update contact by id
*GenreApi* | [**get_genre_by_id**](docs/GenreApi.md#get_genre_by_id) | **GET** /genres/{id} | Get genre by id
*GenreApi* | [**list_genres**](docs/GenreApi.md#list_genres) | **GET** /genres | List all genres.
*ItemApi* | [**create_item**](docs/ItemApi.md#create_item) | **POST** /items | Create an new item.
*ItemApi* | [**current_item_post_structure**](docs/ItemApi.md#current_item_post_structure) | **POST** /items/current/structure | Post a current playing item, keep structure
*ItemApi* | [**current_item_post_timing**](docs/ItemApi.md#current_item_post_timing) | **POST** /items/current/timing | Post a current playing item
*ItemApi* | [**delete_item_by_id**](docs/ItemApi.md#delete_item_by_id) | **DELETE** /items/{id} | Delete item by ID.
*ItemApi* | [**get_item_by_id**](docs/ItemApi.md#get_item_by_id) | **GET** /items/{id} | Get extended item details by ID.
*ItemApi* | [**list_items**](docs/ItemApi.md#list_items) | **GET** /items | Get a list of all the items currently in your station.
*ItemApi* | [**playlist_post_structure**](docs/ItemApi.md#playlist_post_structure) | **POST** /items/playlist/structure | Post a playlist, keep current structure
*ItemApi* | [**playlist_post_timing**](docs/ItemApi.md#playlist_post_timing) | **POST** /items/playlist/timing | Post a playlist
*ItemApi* | [**update_item_by_id**](docs/ItemApi.md#update_item_by_id) | **PATCH** /items/{id} | Update extended item details by ID.
*ModelTypeApi* | [**get_model_type_by_id**](docs/ModelTypeApi.md#get_model_type_by_id) | **GET** /model_types/{id} | Get modelType by id
*ModelTypeApi* | [**list_model_types**](docs/ModelTypeApi.md#list_model_types) | **GET** /model_types | Get all modelTypes.
*PresenterApi* | [**create_presenter**](docs/PresenterApi.md#create_presenter) | **POST** /presenters | Create presenter.
*PresenterApi* | [**delete_presenter_by_id**](docs/PresenterApi.md#delete_presenter_by_id) | **DELETE** /presenters/{id} | Delete presenter by id
*PresenterApi* | [**get_presenter_by_id**](docs/PresenterApi.md#get_presenter_by_id) | **GET** /presenters/{id} | Get presenter by id
*PresenterApi* | [**list_presenters**](docs/PresenterApi.md#list_presenters) | **GET** /presenters | Get all presenters.
*PresenterApi* | [**update_presenter_by_id**](docs/PresenterApi.md#update_presenter_by_id) | **PATCH** /presenters/{id} | Update presenter by id
*ProgramApi* | [**create_program**](docs/ProgramApi.md#create_program) | **POST** /programs | Create program.
*ProgramApi* | [**delete_program_by_id**](docs/ProgramApi.md#delete_program_by_id) | **DELETE** /programs/{id} | Delete program by id
*ProgramApi* | [**get_program_by_id**](docs/ProgramApi.md#get_program_by_id) | **GET** /programs/{id} | Get program by id
*ProgramApi* | [**list_programs**](docs/ProgramApi.md#list_programs) | **GET** /programs | Get all programs.
*ProgramApi* | [**update_program_by_id**](docs/ProgramApi.md#update_program_by_id) | **PATCH** /programs/{id} | Update program by id
*StationApi* | [**get_station**](docs/StationApi.md#get_station) | **GET** /station | Get own station only
*StoryApi* | [**create_story**](docs/StoryApi.md#create_story) | **POST** /stories | Create story.
*StoryApi* | [**delete_story_by_id**](docs/StoryApi.md#delete_story_by_id) | **DELETE** /stories/{id} | Delete story by id
*StoryApi* | [**get_story_by_id**](docs/StoryApi.md#get_story_by_id) | **GET** /stories/{id} | Get story by id
*StoryApi* | [**list_stories**](docs/StoryApi.md#list_stories) | **GET** /stories | Get all stories.
*StoryApi* | [**update_story_by_id**](docs/StoryApi.md#update_story_by_id) | **PATCH** /stories/{id} | Update story by id
*StringApi* | [**get_strings_by_name**](docs/StringApi.md#get_strings_by_name) | **GET** /strings/{name} | Get Strings (formatted)
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /tags | Create tag.
*TagApi* | [**delete_tag_by_id**](docs/TagApi.md#delete_tag_by_id) | **DELETE** /tags/{id} | Delete tag by id
*TagApi* | [**get_tag_by_id**](docs/TagApi.md#get_tag_by_id) | **GET** /tags/{id} | Get tags by id
*TagApi* | [**list_tags**](docs/TagApi.md#list_tags) | **GET** /tags | Get a list of all the tags currently in your station.
*TagApi* | [**update_tag_by_id**](docs/TagApi.md#update_tag_by_id) | **PATCH** /tags/{id} | Update tag by id
*UserApi* | [**delete_user_by_id**](docs/UserApi.md#delete_user_by_id) | **DELETE** /users/{id} | Remove user from station by Id
*UserApi* | [**get_user_by_id**](docs/UserApi.md#get_user_by_id) | **GET** /users/{id} | Get user by id
*UserApi* | [**invite_user_by_mail**](docs/UserApi.md#invite_user_by_mail) | **POST** /users/invite | Invite user by mail
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /users | Get all users.
*VisualSlideApi* | [**get_visual_slide**](docs/VisualSlideApi.md#get_visual_slide) | **GET** /visual | Get Visual Slide Image as Base64


## Documentation For Models

 - [Block](docs/Block.md)
 - [BlockRelations](docs/BlockRelations.md)
 - [BlockRelationsBroadcast](docs/BlockRelationsBroadcast.md)
 - [BlockRelationsBroadcastParams](docs/BlockRelationsBroadcastParams.md)
 - [BlockRelationsItems](docs/BlockRelationsItems.md)
 - [BlockRelationsItemsParams](docs/BlockRelationsItemsParams.md)
 - [BlockRelationsProgram](docs/BlockRelationsProgram.md)
 - [BlockResults](docs/BlockResults.md)
 - [Broadcast](docs/Broadcast.md)
 - [BroadcastEPGDay](docs/BroadcastEPGDay.md)
 - [BroadcastEPGRelations](docs/BroadcastEPGRelations.md)
 - [BroadcastFieldValues](docs/BroadcastFieldValues.md)
 - [BroadcastInputOnly](docs/BroadcastInputOnly.md)
 - [BroadcastOutputOnly](docs/BroadcastOutputOnly.md)
 - [BroadcastRelations](docs/BroadcastRelations.md)
 - [BroadcastRelationsBlocks](docs/BroadcastRelationsBlocks.md)
 - [BroadcastRelationsItems](docs/BroadcastRelationsItems.md)
 - [BroadcastRelationsItemsParams](docs/BroadcastRelationsItemsParams.md)
 - [BroadcastRelationsModelType](docs/BroadcastRelationsModelType.md)
 - [BroadcastRelationsPresenters](docs/BroadcastRelationsPresenters.md)
 - [BroadcastRelationsTags](docs/BroadcastRelationsTags.md)
 - [BroadcastResults](docs/BroadcastResults.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignOutputOnly](docs/CampaignOutputOnly.md)
 - [CampaignRelations](docs/CampaignRelations.md)
 - [CampaignRelationsItems](docs/CampaignRelationsItems.md)
 - [CampaignRelationsItemsParams](docs/CampaignRelationsItemsParams.md)
 - [CampaignResults](docs/CampaignResults.md)
 - [Contact](docs/Contact.md)
 - [ContactFieldValues](docs/ContactFieldValues.md)
 - [ContactOutputOnly](docs/ContactOutputOnly.md)
 - [ContactRelations](docs/ContactRelations.md)
 - [ContactRelationsItems](docs/ContactRelationsItems.md)
 - [ContactRelationsTags](docs/ContactRelationsTags.md)
 - [ContactRelationsTagsParams](docs/ContactRelationsTagsParams.md)
 - [ContactResults](docs/ContactResults.md)
 - [Data](docs/Data.md)
 - [Data1](docs/Data1.md)
 - [EPGResults](docs/EPGResults.md)
 - [Forbidden](docs/Forbidden.md)
 - [Genre](docs/Genre.md)
 - [GenreOutputOnly](docs/GenreOutputOnly.md)
 - [GenreRelations](docs/GenreRelations.md)
 - [GenreRelationsBroadcasts](docs/GenreRelationsBroadcasts.md)
 - [GenreRelationsBroadcastsParams](docs/GenreRelationsBroadcastsParams.md)
 - [GenreRelationsPrograms](docs/GenreRelationsPrograms.md)
 - [GenreResults](docs/GenreResults.md)
 - [ImportItem](docs/ImportItem.md)
 - [ImportItemFieldValues](docs/ImportItemFieldValues.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [InviteUserData](docs/InviteUserData.md)
 - [InviteUserSuccess](docs/InviteUserSuccess.md)
 - [Item](docs/Item.md)
 - [ItemInputOnly](docs/ItemInputOnly.md)
 - [ItemOutputOnly](docs/ItemOutputOnly.md)
 - [ItemRelations](docs/ItemRelations.md)
 - [ItemRelationsBlock](docs/ItemRelationsBlock.md)
 - [ItemRelationsCampaign](docs/ItemRelationsCampaign.md)
 - [ItemRelationsContacts](docs/ItemRelationsContacts.md)
 - [ItemRelationsContactsParams](docs/ItemRelationsContactsParams.md)
 - [ItemRelationsProgram](docs/ItemRelationsProgram.md)
 - [ItemRelationsTags](docs/ItemRelationsTags.md)
 - [ItemResults](docs/ItemResults.md)
 - [ModelType](docs/ModelType.md)
 - [ModelTypeOptions](docs/ModelTypeOptions.md)
 - [ModelTypeOutputOnly](docs/ModelTypeOutputOnly.md)
 - [ModelTypeRelations](docs/ModelTypeRelations.md)
 - [ModelTypeRelationsBroadcasts](docs/ModelTypeRelationsBroadcasts.md)
 - [ModelTypeRelationsCampaigns](docs/ModelTypeRelationsCampaigns.md)
 - [ModelTypeRelationsCampaignsParams](docs/ModelTypeRelationsCampaignsParams.md)
 - [ModelTypeRelationsContacts](docs/ModelTypeRelationsContacts.md)
 - [ModelTypeRelationsItems](docs/ModelTypeRelationsItems.md)
 - [ModelTypeRelationsPresenters](docs/ModelTypeRelationsPresenters.md)
 - [ModelTypeRelationsPrograms](docs/ModelTypeRelationsPrograms.md)
 - [ModelTypeResults](docs/ModelTypeResults.md)
 - [NotFound](docs/NotFound.md)
 - [PostSuccess](docs/PostSuccess.md)
 - [Presenter](docs/Presenter.md)
 - [PresenterOutputOnly](docs/PresenterOutputOnly.md)
 - [PresenterRelations](docs/PresenterRelations.md)
 - [PresenterRelationsBroadcasts](docs/PresenterRelationsBroadcasts.md)
 - [PresenterRelationsPrograms](docs/PresenterRelationsPrograms.md)
 - [PresenterRelationsProgramsParams](docs/PresenterRelationsProgramsParams.md)
 - [PresenterResults](docs/PresenterResults.md)
 - [Program](docs/Program.md)
 - [ProgramFieldValues](docs/ProgramFieldValues.md)
 - [ProgramInputOnly](docs/ProgramInputOnly.md)
 - [ProgramOutputOnly](docs/ProgramOutputOnly.md)
 - [ProgramRelations](docs/ProgramRelations.md)
 - [ProgramRelationsBlocks](docs/ProgramRelationsBlocks.md)
 - [ProgramRelationsBroadcasts](docs/ProgramRelationsBroadcasts.md)
 - [ProgramRelationsItems](docs/ProgramRelationsItems.md)
 - [ProgramRelationsItemsParams](docs/ProgramRelationsItemsParams.md)
 - [ProgramRelationsPresenters](docs/ProgramRelationsPresenters.md)
 - [ProgramRelationsTags](docs/ProgramRelationsTags.md)
 - [ProgramResults](docs/ProgramResults.md)
 - [ReadOnly](docs/ReadOnly.md)
 - [RelationsPlaceholder](docs/RelationsPlaceholder.md)
 - [StationResult](docs/StationResult.md)
 - [StationResultStation](docs/StationResultStation.md)
 - [Story](docs/Story.md)
 - [StoryInputOnly](docs/StoryInputOnly.md)
 - [StoryOutputOnly](docs/StoryOutputOnly.md)
 - [StoryRelations](docs/StoryRelations.md)
 - [StoryRelationsItems](docs/StoryRelationsItems.md)
 - [StoryRelationsTags](docs/StoryRelationsTags.md)
 - [StoryRelationsTagsParams](docs/StoryRelationsTagsParams.md)
 - [StoryResults](docs/StoryResults.md)
 - [Success](docs/Success.md)
 - [Tag](docs/Tag.md)
 - [TagOutputOnly](docs/TagOutputOnly.md)
 - [TagRelations](docs/TagRelations.md)
 - [TagRelationsBroadcasts](docs/TagRelationsBroadcasts.md)
 - [TagRelationsBroadcastsParams](docs/TagRelationsBroadcastsParams.md)
 - [TagRelationsContacts](docs/TagRelationsContacts.md)
 - [TagRelationsItems](docs/TagRelationsItems.md)
 - [TagRelationsPrograms](docs/TagRelationsPrograms.md)
 - [TagResults](docs/TagResults.md)
 - [TextString](docs/TextString.md)
 - [TooManyRequests](docs/TooManyRequests.md)
 - [UnprocessableEntity](docs/UnprocessableEntity.md)
 - [UserResult](docs/UserResult.md)
 - [UserResultSettings](docs/UserResultSettings.md)
 - [UserResults](docs/UserResults.md)
 - [VisualResult](docs/VisualResult.md)
 - [BlockResult](docs/BlockResult.md)
 - [BroadcastDataInput](docs/BroadcastDataInput.md)
 - [BroadcastEPGResult](docs/BroadcastEPGResult.md)
 - [BroadcastResult](docs/BroadcastResult.md)
 - [CampaignDataInput](docs/CampaignDataInput.md)
 - [CampaignResult](docs/CampaignResult.md)
 - [ContactDataInput](docs/ContactDataInput.md)
 - [ContactResult](docs/ContactResult.md)
 - [GenreResult](docs/GenreResult.md)
 - [ItemDataInput](docs/ItemDataInput.md)
 - [ItemResult](docs/ItemResult.md)
 - [ModelTypeResult](docs/ModelTypeResult.md)
 - [PresenterDataInput](docs/PresenterDataInput.md)
 - [PresenterEPGResult](docs/PresenterEPGResult.md)
 - [PresenterResult](docs/PresenterResult.md)
 - [ProgramDataInput](docs/ProgramDataInput.md)
 - [ProgramResult](docs/ProgramResult.md)
 - [StoryDataInput](docs/StoryDataInput.md)
 - [StoryResult](docs/StoryResult.md)
 - [TagDataInput](docs/TagDataInput.md)
 - [TagResult](docs/TagResult.md)


## Documentation For Authorization


## API Key

- **Type**: API key
- **API key parameter name**: api-key
- **Location**: HTTP header


## Author

support@pluxbox.com

