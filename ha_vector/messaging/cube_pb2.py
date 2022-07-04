# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cube.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import messages_pb2 as messages__pb2
import response_status_pb2 as response__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncube.proto\x12\x1e\x41nki.Vector.external_interface\x1a\x0emessages.proto\x1a\x15response_status.proto\"\x14\n\x12\x43onnectCubeRequest\"\x8d\x01\n\x13\x43onnectCubeResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x11\n\tobject_id\x18\x03 \x01(\r\x12\x12\n\nfactory_id\x18\x04 \x01(\t\"\x17\n\x15\x43ubesAvailableRequest\"m\n\x16\x43ubesAvailableResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\x12\x13\n\x0b\x66\x61\x63tory_ids\x18\x02 \x03(\t\"\x17\n\x15\x44isconnectCubeRequest\"X\n\x16\x44isconnectCubeResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\"\x18\n\x16\x46lashCubeLightsRequest\"Y\n\x17\x46lashCubeLightsResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\"\x1c\n\x1a\x46orgetPreferredCubeRequest\"]\n\x1b\x46orgetPreferredCubeResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\"-\n\x17SetPreferredCubeRequest\x12\x12\n\nfactory_id\x18\x01 \x01(\t\"Z\n\x18SetPreferredCubeResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\"\xb0\x03\n\x14SetCubeLightsRequest\x12\x11\n\tobject_id\x18\x01 \x01(\r\x12\x10\n\x08on_color\x18\x02 \x03(\r\x12\x11\n\toff_color\x18\x03 \x03(\r\x12\x14\n\x0con_period_ms\x18\x04 \x03(\r\x12\x15\n\roff_period_ms\x18\x05 \x03(\r\x12\x1f\n\x17transition_on_period_ms\x18\x06 \x03(\r\x12 \n\x18transition_off_period_ms\x18\x07 \x03(\r\x12\x0e\n\x06offset\x18\x08 \x03(\x05\x12\x15\n\rrelative_to_x\x18\t \x01(\x02\x12\x15\n\rrelative_to_y\x18\n \x01(\x02\x12\x0e\n\x06rotate\x18\x0b \x01(\x08\x12\\\n\rmake_relative\x18\x0c \x01(\x0e\x32\x45.Anki.Vector.external_interface.SetCubeLightsRequest.MakeRelativeMode\"D\n\x10MakeRelativeMode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\r\n\tBY_CORNER\x10\x02\x12\x0b\n\x07\x42Y_SIDE\x10\x03\"W\n\x15SetCubeLightsResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\"%\n\x0fObjectAvailable\x12\x12\n\nfactory_id\x18\x01 \x01(\t\"\x92\x01\n\x15ObjectConnectionState\x12\x11\n\tobject_id\x18\x01 \x01(\r\x12\x12\n\nfactory_id\x18\x02 \x01(\t\x12?\n\x0bobject_type\x18\x03 \x01(\x0e\x32*.Anki.Vector.external_interface.ObjectType\x12\x11\n\tconnected\x18\x04 \x01(\x08\"3\n\x0bObjectMoved\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x11\n\tobject_id\x18\x02 \x01(\r\";\n\x13ObjectStoppedMoving\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x11\n\tobject_id\x18\x02 \x01(\r\"t\n\x13ObjectUpAxisChanged\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x11\n\tobject_id\x18\x02 \x01(\r\x12\x37\n\x07up_axis\x18\x03 \x01(\x0e\x32&.Anki.Vector.external_interface.UpAxis\"4\n\x0cObjectTapped\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x11\n\tobject_id\x18\x02 \x01(\r\"\xf0\x02\n\x13RobotObservedObject\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12G\n\robject_family\x18\x02 \x01(\x0e\x32,.Anki.Vector.external_interface.ObjectFamilyB\x02\x18\x01\x12?\n\x0bobject_type\x18\x03 \x01(\x0e\x32*.Anki.Vector.external_interface.ObjectType\x12\x11\n\tobject_id\x18\x04 \x01(\x05\x12:\n\x08img_rect\x18\x05 \x01(\x0b\x32(.Anki.Vector.external_interface.CladRect\x12\x38\n\x04pose\x18\x06 \x01(\x0b\x32*.Anki.Vector.external_interface.PoseStruct\x12 \n\x18top_face_orientation_rad\x18\x07 \x01(\x02\x12\x11\n\tis_active\x18\x08 \x01(\r\"\x14\n\x12\x43ubeConnectionLost\"d\n\x1a\x44\x65leteCustomObjectsRequest\x12\x46\n\x04mode\x18\x01 \x01(\x0e\x32\x38.Anki.Vector.external_interface.CustomObjectDeletionMode\"]\n\x1b\x44\x65leteCustomObjectsResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\"\x93\x01\n\x1e\x43reateFixedCustomObjectRequest\x12\x38\n\x04pose\x18\x01 \x01(\x0b\x32*.Anki.Vector.external_interface.PoseStruct\x12\x11\n\tx_size_mm\x18\x02 \x01(\x02\x12\x11\n\ty_size_mm\x18\x03 \x01(\x02\x12\x11\n\tz_size_mm\x18\x04 \x01(\x02\"t\n\x1f\x43reateFixedCustomObjectResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\x12\x11\n\tobject_id\x18\x02 \x01(\r\"\xba\x04\n\x13\x43ustomBoxDefinition\x12H\n\x0cmarker_front\x18\x01 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12G\n\x0bmarker_back\x18\x02 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12\x46\n\nmarker_top\x18\x03 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12I\n\rmarker_bottom\x18\x04 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12G\n\x0bmarker_left\x18\x05 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12H\n\x0cmarker_right\x18\x06 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12\x11\n\tx_size_mm\x18\x07 \x01(\x02\x12\x11\n\ty_size_mm\x18\x08 \x01(\x02\x12\x11\n\tz_size_mm\x18\t \x01(\x02\x12\x17\n\x0fmarker_width_mm\x18\n \x01(\x02\x12\x18\n\x10marker_height_mm\x18\x0b \x01(\x02\"\x9e\x01\n\x14\x43ustomCubeDefinition\x12\x42\n\x06marker\x18\x01 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12\x0f\n\x07size_mm\x18\x02 \x01(\x02\x12\x17\n\x0fmarker_width_mm\x18\x03 \x01(\x02\x12\x18\n\x10marker_height_mm\x18\x04 \x01(\x02\"\xb2\x01\n\x14\x43ustomWallDefinition\x12\x42\n\x06marker\x18\x01 \x01(\x0e\x32\x32.Anki.Vector.external_interface.CustomObjectMarker\x12\x10\n\x08width_mm\x18\x02 \x01(\x02\x12\x11\n\theight_mm\x18\x03 \x01(\x02\x12\x17\n\x0fmarker_width_mm\x18\x04 \x01(\x02\x12\x18\n\x10marker_height_mm\x18\x05 \x01(\x02\"\xf0\x02\n\x19\x44\x65\x66ineCustomObjectRequest\x12?\n\x0b\x63ustom_type\x18\x01 \x01(\x0e\x32*.Anki.Vector.external_interface.CustomType\x12\x11\n\tis_unique\x18\x02 \x01(\x08\x12I\n\ncustom_box\x18\x03 \x01(\x0b\x32\x33.Anki.Vector.external_interface.CustomBoxDefinitionH\x00\x12K\n\x0b\x63ustom_cube\x18\x04 \x01(\x0b\x32\x34.Anki.Vector.external_interface.CustomCubeDefinitionH\x00\x12K\n\x0b\x63ustom_wall\x18\x05 \x01(\x0b\x32\x34.Anki.Vector.external_interface.CustomWallDefinitionH\x00\x42\x1a\n\x18\x63ustom_object_definition\"m\n\x1a\x44\x65\x66ineCustomObjectResponse\x12>\n\x06status\x18\x01 \x01(\x0b\x32..Anki.Vector.external_interface.ResponseStatus\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\xac\x05\n\x0bObjectEvent\x12K\n\x10object_available\x18\x01 \x01(\x0b\x32/.Anki.Vector.external_interface.ObjectAvailableH\x00\x12X\n\x17object_connection_state\x18\x02 \x01(\x0b\x32\x35.Anki.Vector.external_interface.ObjectConnectionStateH\x00\x12\x43\n\x0cobject_moved\x18\x03 \x01(\x0b\x32+.Anki.Vector.external_interface.ObjectMovedH\x00\x12T\n\x15object_stopped_moving\x18\x04 \x01(\x0b\x32\x33.Anki.Vector.external_interface.ObjectStoppedMovingH\x00\x12U\n\x16object_up_axis_changed\x18\x05 \x01(\x0b\x32\x33.Anki.Vector.external_interface.ObjectUpAxisChangedH\x00\x12\x45\n\robject_tapped\x18\x06 \x01(\x0b\x32,.Anki.Vector.external_interface.ObjectTappedH\x00\x12T\n\x15robot_observed_object\x18\x07 \x01(\x0b\x32\x33.Anki.Vector.external_interface.RobotObservedObjectH\x00\x12R\n\x14\x63ube_connection_lost\x18\x08 \x01(\x0b\x32\x32.Anki.Vector.external_interface.CubeConnectionLostH\x00\x42\x13\n\x11object_event_type*{\n\nObjectType\x12\x12\n\x0eINVALID_OBJECT\x10\x00\x12\x12\n\x0eUNKNOWN_OBJECT\x10\x01\x12\x14\n\x10\x42LOCK_LIGHTCUBE1\x10\x02\x12\x11\n\rCHARGER_BASIC\x10\x06\x12\x1c\n\x18\x46IRST_CUSTOM_OBJECT_TYPE\x10\x0f*\xd0\x03\n\nCustomType\x12\x17\n\x13INVALID_CUSTOM_TYPE\x10\x00\x12\x12\n\x0e\x43USTOM_TYPE_00\x10\x01\x12\x12\n\x0e\x43USTOM_TYPE_01\x10\x02\x12\x12\n\x0e\x43USTOM_TYPE_02\x10\x03\x12\x12\n\x0e\x43USTOM_TYPE_03\x10\x04\x12\x12\n\x0e\x43USTOM_TYPE_04\x10\x05\x12\x12\n\x0e\x43USTOM_TYPE_05\x10\x06\x12\x12\n\x0e\x43USTOM_TYPE_06\x10\x07\x12\x12\n\x0e\x43USTOM_TYPE_07\x10\x08\x12\x12\n\x0e\x43USTOM_TYPE_08\x10\t\x12\x12\n\x0e\x43USTOM_TYPE_09\x10\n\x12\x12\n\x0e\x43USTOM_TYPE_10\x10\x0b\x12\x12\n\x0e\x43USTOM_TYPE_11\x10\x0c\x12\x12\n\x0e\x43USTOM_TYPE_12\x10\r\x12\x12\n\x0e\x43USTOM_TYPE_13\x10\x0e\x12\x12\n\x0e\x43USTOM_TYPE_14\x10\x0f\x12\x12\n\x0e\x43USTOM_TYPE_15\x10\x10\x12\x12\n\x0e\x43USTOM_TYPE_16\x10\x11\x12\x12\n\x0e\x43USTOM_TYPE_17\x10\x12\x12\x12\n\x0e\x43USTOM_TYPE_18\x10\x13\x12\x12\n\x0e\x43USTOM_TYPE_19\x10\x14\x12\x15\n\x11\x43USTOM_TYPE_COUNT\x10\x14\x1a\x02\x10\x01*\x8e\x01\n\x0cObjectFamily\x12\x12\n\x0eINVALID_FAMILY\x10\x00\x12\x12\n\x0eUNKNOWN_FAMILY\x10\x01\x12\t\n\x05\x42LOCK\x10\x02\x12\x0e\n\nLIGHT_CUBE\x10\x03\x12\x0b\n\x07\x43HARGER\x10\x04\x12\x11\n\rCUSTOM_OBJECT\x10\x07\x12\x17\n\x13OBJECT_FAMILY_COUNT\x10\x07\x1a\x02\x10\x01*\x88\x01\n\x06UpAxis\x12\x10\n\x0cINVALID_AXIS\x10\x00\x12\x0e\n\nX_NEGATIVE\x10\x01\x12\x0e\n\nX_POSITIVE\x10\x02\x12\x0e\n\nY_NEGATIVE\x10\x03\x12\x0e\n\nY_POSITIVE\x10\x04\x12\x0e\n\nZ_NEGATIVE\x10\x05\x12\x0e\n\nZ_POSITIVE\x10\x06\x12\x0c\n\x08NUM_AXES\x10\x07*P\n\x0fObjectConstants\x12\x19\n\x15OBJECT_CONSTANTS_NULL\x10\x00\x12\"\n\x1e\x46IXED_CUSTOM_WALL_THICKNESS_MM\x10\n*\xac\x04\n\x12\x43ustomObjectMarker\x12\x19\n\x15\x43USTOM_MARKER_UNKNOWN\x10\x00\x12\x1b\n\x17\x43USTOM_MARKER_CIRCLES_2\x10\x01\x12\x1b\n\x17\x43USTOM_MARKER_CIRCLES_3\x10\x02\x12\x1b\n\x17\x43USTOM_MARKER_CIRCLES_4\x10\x03\x12\x1b\n\x17\x43USTOM_MARKER_CIRCLES_5\x10\x04\x12\x1c\n\x18\x43USTOM_MARKER_DIAMONDS_2\x10\x05\x12\x1c\n\x18\x43USTOM_MARKER_DIAMONDS_3\x10\x06\x12\x1c\n\x18\x43USTOM_MARKER_DIAMONDS_4\x10\x07\x12\x1c\n\x18\x43USTOM_MARKER_DIAMONDS_5\x10\x08\x12\x1c\n\x18\x43USTOM_MARKER_HEXAGONS_2\x10\t\x12\x1c\n\x18\x43USTOM_MARKER_HEXAGONS_3\x10\n\x12\x1c\n\x18\x43USTOM_MARKER_HEXAGONS_4\x10\x0b\x12\x1c\n\x18\x43USTOM_MARKER_HEXAGONS_5\x10\x0c\x12\x1d\n\x19\x43USTOM_MARKER_TRIANGLES_2\x10\r\x12\x1d\n\x19\x43USTOM_MARKER_TRIANGLES_3\x10\x0e\x12\x1d\n\x19\x43USTOM_MARKER_TRIANGLES_4\x10\x0f\x12\x1d\n\x19\x43USTOM_MARKER_TRIANGLES_5\x10\x10\x12\x17\n\x13\x43USTOM_MARKER_COUNT\x10\x10\x1a\x02\x10\x01*\xa4\x01\n\x18\x43ustomObjectDeletionMode\x12\x19\n\x15\x44\x45LETION_MASK_UNKNOWN\x10\x00\x12&\n\"DELETION_MASK_FIXED_CUSTOM_OBJECTS\x10\x01\x12\'\n#DELETION_MASK_CUSTOM_MARKER_OBJECTS\x10\x02\x12\x1c\n\x18\x44\x45LETION_MASK_ARCHETYPES\x10\x03\x62\x06proto3')

_OBJECTTYPE = DESCRIPTOR.enum_types_by_name['ObjectType']
ObjectType = enum_type_wrapper.EnumTypeWrapper(_OBJECTTYPE)
_CUSTOMTYPE = DESCRIPTOR.enum_types_by_name['CustomType']
CustomType = enum_type_wrapper.EnumTypeWrapper(_CUSTOMTYPE)
_OBJECTFAMILY = DESCRIPTOR.enum_types_by_name['ObjectFamily']
ObjectFamily = enum_type_wrapper.EnumTypeWrapper(_OBJECTFAMILY)
_UPAXIS = DESCRIPTOR.enum_types_by_name['UpAxis']
UpAxis = enum_type_wrapper.EnumTypeWrapper(_UPAXIS)
_OBJECTCONSTANTS = DESCRIPTOR.enum_types_by_name['ObjectConstants']
ObjectConstants = enum_type_wrapper.EnumTypeWrapper(_OBJECTCONSTANTS)
_CUSTOMOBJECTMARKER = DESCRIPTOR.enum_types_by_name['CustomObjectMarker']
CustomObjectMarker = enum_type_wrapper.EnumTypeWrapper(_CUSTOMOBJECTMARKER)
_CUSTOMOBJECTDELETIONMODE = DESCRIPTOR.enum_types_by_name['CustomObjectDeletionMode']
CustomObjectDeletionMode = enum_type_wrapper.EnumTypeWrapper(_CUSTOMOBJECTDELETIONMODE)
INVALID_OBJECT = 0
UNKNOWN_OBJECT = 1
BLOCK_LIGHTCUBE1 = 2
CHARGER_BASIC = 6
FIRST_CUSTOM_OBJECT_TYPE = 15
INVALID_CUSTOM_TYPE = 0
CUSTOM_TYPE_00 = 1
CUSTOM_TYPE_01 = 2
CUSTOM_TYPE_02 = 3
CUSTOM_TYPE_03 = 4
CUSTOM_TYPE_04 = 5
CUSTOM_TYPE_05 = 6
CUSTOM_TYPE_06 = 7
CUSTOM_TYPE_07 = 8
CUSTOM_TYPE_08 = 9
CUSTOM_TYPE_09 = 10
CUSTOM_TYPE_10 = 11
CUSTOM_TYPE_11 = 12
CUSTOM_TYPE_12 = 13
CUSTOM_TYPE_13 = 14
CUSTOM_TYPE_14 = 15
CUSTOM_TYPE_15 = 16
CUSTOM_TYPE_16 = 17
CUSTOM_TYPE_17 = 18
CUSTOM_TYPE_18 = 19
CUSTOM_TYPE_19 = 20
CUSTOM_TYPE_COUNT = 20
INVALID_FAMILY = 0
UNKNOWN_FAMILY = 1
BLOCK = 2
LIGHT_CUBE = 3
CHARGER = 4
CUSTOM_OBJECT = 7
OBJECT_FAMILY_COUNT = 7
INVALID_AXIS = 0
X_NEGATIVE = 1
X_POSITIVE = 2
Y_NEGATIVE = 3
Y_POSITIVE = 4
Z_NEGATIVE = 5
Z_POSITIVE = 6
NUM_AXES = 7
OBJECT_CONSTANTS_NULL = 0
FIXED_CUSTOM_WALL_THICKNESS_MM = 10
CUSTOM_MARKER_UNKNOWN = 0
CUSTOM_MARKER_CIRCLES_2 = 1
CUSTOM_MARKER_CIRCLES_3 = 2
CUSTOM_MARKER_CIRCLES_4 = 3
CUSTOM_MARKER_CIRCLES_5 = 4
CUSTOM_MARKER_DIAMONDS_2 = 5
CUSTOM_MARKER_DIAMONDS_3 = 6
CUSTOM_MARKER_DIAMONDS_4 = 7
CUSTOM_MARKER_DIAMONDS_5 = 8
CUSTOM_MARKER_HEXAGONS_2 = 9
CUSTOM_MARKER_HEXAGONS_3 = 10
CUSTOM_MARKER_HEXAGONS_4 = 11
CUSTOM_MARKER_HEXAGONS_5 = 12
CUSTOM_MARKER_TRIANGLES_2 = 13
CUSTOM_MARKER_TRIANGLES_3 = 14
CUSTOM_MARKER_TRIANGLES_4 = 15
CUSTOM_MARKER_TRIANGLES_5 = 16
CUSTOM_MARKER_COUNT = 16
DELETION_MASK_UNKNOWN = 0
DELETION_MASK_FIXED_CUSTOM_OBJECTS = 1
DELETION_MASK_CUSTOM_MARKER_OBJECTS = 2
DELETION_MASK_ARCHETYPES = 3


_CONNECTCUBEREQUEST = DESCRIPTOR.message_types_by_name['ConnectCubeRequest']
_CONNECTCUBERESPONSE = DESCRIPTOR.message_types_by_name['ConnectCubeResponse']
_CUBESAVAILABLEREQUEST = DESCRIPTOR.message_types_by_name['CubesAvailableRequest']
_CUBESAVAILABLERESPONSE = DESCRIPTOR.message_types_by_name['CubesAvailableResponse']
_DISCONNECTCUBEREQUEST = DESCRIPTOR.message_types_by_name['DisconnectCubeRequest']
_DISCONNECTCUBERESPONSE = DESCRIPTOR.message_types_by_name['DisconnectCubeResponse']
_FLASHCUBELIGHTSREQUEST = DESCRIPTOR.message_types_by_name['FlashCubeLightsRequest']
_FLASHCUBELIGHTSRESPONSE = DESCRIPTOR.message_types_by_name['FlashCubeLightsResponse']
_FORGETPREFERREDCUBEREQUEST = DESCRIPTOR.message_types_by_name['ForgetPreferredCubeRequest']
_FORGETPREFERREDCUBERESPONSE = DESCRIPTOR.message_types_by_name['ForgetPreferredCubeResponse']
_SETPREFERREDCUBEREQUEST = DESCRIPTOR.message_types_by_name['SetPreferredCubeRequest']
_SETPREFERREDCUBERESPONSE = DESCRIPTOR.message_types_by_name['SetPreferredCubeResponse']
_SETCUBELIGHTSREQUEST = DESCRIPTOR.message_types_by_name['SetCubeLightsRequest']
_SETCUBELIGHTSRESPONSE = DESCRIPTOR.message_types_by_name['SetCubeLightsResponse']
_OBJECTAVAILABLE = DESCRIPTOR.message_types_by_name['ObjectAvailable']
_OBJECTCONNECTIONSTATE = DESCRIPTOR.message_types_by_name['ObjectConnectionState']
_OBJECTMOVED = DESCRIPTOR.message_types_by_name['ObjectMoved']
_OBJECTSTOPPEDMOVING = DESCRIPTOR.message_types_by_name['ObjectStoppedMoving']
_OBJECTUPAXISCHANGED = DESCRIPTOR.message_types_by_name['ObjectUpAxisChanged']
_OBJECTTAPPED = DESCRIPTOR.message_types_by_name['ObjectTapped']
_ROBOTOBSERVEDOBJECT = DESCRIPTOR.message_types_by_name['RobotObservedObject']
_CUBECONNECTIONLOST = DESCRIPTOR.message_types_by_name['CubeConnectionLost']
_DELETECUSTOMOBJECTSREQUEST = DESCRIPTOR.message_types_by_name['DeleteCustomObjectsRequest']
_DELETECUSTOMOBJECTSRESPONSE = DESCRIPTOR.message_types_by_name['DeleteCustomObjectsResponse']
_CREATEFIXEDCUSTOMOBJECTREQUEST = DESCRIPTOR.message_types_by_name['CreateFixedCustomObjectRequest']
_CREATEFIXEDCUSTOMOBJECTRESPONSE = DESCRIPTOR.message_types_by_name['CreateFixedCustomObjectResponse']
_CUSTOMBOXDEFINITION = DESCRIPTOR.message_types_by_name['CustomBoxDefinition']
_CUSTOMCUBEDEFINITION = DESCRIPTOR.message_types_by_name['CustomCubeDefinition']
_CUSTOMWALLDEFINITION = DESCRIPTOR.message_types_by_name['CustomWallDefinition']
_DEFINECUSTOMOBJECTREQUEST = DESCRIPTOR.message_types_by_name['DefineCustomObjectRequest']
_DEFINECUSTOMOBJECTRESPONSE = DESCRIPTOR.message_types_by_name['DefineCustomObjectResponse']
_OBJECTEVENT = DESCRIPTOR.message_types_by_name['ObjectEvent']
_SETCUBELIGHTSREQUEST_MAKERELATIVEMODE = _SETCUBELIGHTSREQUEST.enum_types_by_name['MakeRelativeMode']
ConnectCubeRequest = _reflection.GeneratedProtocolMessageType('ConnectCubeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTCUBEREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ConnectCubeRequest)
  })
_sym_db.RegisterMessage(ConnectCubeRequest)

ConnectCubeResponse = _reflection.GeneratedProtocolMessageType('ConnectCubeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTCUBERESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ConnectCubeResponse)
  })
_sym_db.RegisterMessage(ConnectCubeResponse)

CubesAvailableRequest = _reflection.GeneratedProtocolMessageType('CubesAvailableRequest', (_message.Message,), {
  'DESCRIPTOR' : _CUBESAVAILABLEREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CubesAvailableRequest)
  })
_sym_db.RegisterMessage(CubesAvailableRequest)

CubesAvailableResponse = _reflection.GeneratedProtocolMessageType('CubesAvailableResponse', (_message.Message,), {
  'DESCRIPTOR' : _CUBESAVAILABLERESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CubesAvailableResponse)
  })
_sym_db.RegisterMessage(CubesAvailableResponse)

DisconnectCubeRequest = _reflection.GeneratedProtocolMessageType('DisconnectCubeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECTCUBEREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.DisconnectCubeRequest)
  })
_sym_db.RegisterMessage(DisconnectCubeRequest)

DisconnectCubeResponse = _reflection.GeneratedProtocolMessageType('DisconnectCubeResponse', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECTCUBERESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.DisconnectCubeResponse)
  })
_sym_db.RegisterMessage(DisconnectCubeResponse)

FlashCubeLightsRequest = _reflection.GeneratedProtocolMessageType('FlashCubeLightsRequest', (_message.Message,), {
  'DESCRIPTOR' : _FLASHCUBELIGHTSREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.FlashCubeLightsRequest)
  })
_sym_db.RegisterMessage(FlashCubeLightsRequest)

FlashCubeLightsResponse = _reflection.GeneratedProtocolMessageType('FlashCubeLightsResponse', (_message.Message,), {
  'DESCRIPTOR' : _FLASHCUBELIGHTSRESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.FlashCubeLightsResponse)
  })
_sym_db.RegisterMessage(FlashCubeLightsResponse)

ForgetPreferredCubeRequest = _reflection.GeneratedProtocolMessageType('ForgetPreferredCubeRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORGETPREFERREDCUBEREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ForgetPreferredCubeRequest)
  })
_sym_db.RegisterMessage(ForgetPreferredCubeRequest)

ForgetPreferredCubeResponse = _reflection.GeneratedProtocolMessageType('ForgetPreferredCubeResponse', (_message.Message,), {
  'DESCRIPTOR' : _FORGETPREFERREDCUBERESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ForgetPreferredCubeResponse)
  })
_sym_db.RegisterMessage(ForgetPreferredCubeResponse)

SetPreferredCubeRequest = _reflection.GeneratedProtocolMessageType('SetPreferredCubeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPREFERREDCUBEREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.SetPreferredCubeRequest)
  })
_sym_db.RegisterMessage(SetPreferredCubeRequest)

SetPreferredCubeResponse = _reflection.GeneratedProtocolMessageType('SetPreferredCubeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPREFERREDCUBERESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.SetPreferredCubeResponse)
  })
_sym_db.RegisterMessage(SetPreferredCubeResponse)

SetCubeLightsRequest = _reflection.GeneratedProtocolMessageType('SetCubeLightsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETCUBELIGHTSREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.SetCubeLightsRequest)
  })
_sym_db.RegisterMessage(SetCubeLightsRequest)

SetCubeLightsResponse = _reflection.GeneratedProtocolMessageType('SetCubeLightsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETCUBELIGHTSRESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.SetCubeLightsResponse)
  })
_sym_db.RegisterMessage(SetCubeLightsResponse)

ObjectAvailable = _reflection.GeneratedProtocolMessageType('ObjectAvailable', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTAVAILABLE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ObjectAvailable)
  })
_sym_db.RegisterMessage(ObjectAvailable)

ObjectConnectionState = _reflection.GeneratedProtocolMessageType('ObjectConnectionState', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTCONNECTIONSTATE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ObjectConnectionState)
  })
_sym_db.RegisterMessage(ObjectConnectionState)

ObjectMoved = _reflection.GeneratedProtocolMessageType('ObjectMoved', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMOVED,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ObjectMoved)
  })
_sym_db.RegisterMessage(ObjectMoved)

ObjectStoppedMoving = _reflection.GeneratedProtocolMessageType('ObjectStoppedMoving', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTOPPEDMOVING,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ObjectStoppedMoving)
  })
_sym_db.RegisterMessage(ObjectStoppedMoving)

ObjectUpAxisChanged = _reflection.GeneratedProtocolMessageType('ObjectUpAxisChanged', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTUPAXISCHANGED,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ObjectUpAxisChanged)
  })
_sym_db.RegisterMessage(ObjectUpAxisChanged)

ObjectTapped = _reflection.GeneratedProtocolMessageType('ObjectTapped', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTTAPPED,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ObjectTapped)
  })
_sym_db.RegisterMessage(ObjectTapped)

RobotObservedObject = _reflection.GeneratedProtocolMessageType('RobotObservedObject', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTOBSERVEDOBJECT,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.RobotObservedObject)
  })
_sym_db.RegisterMessage(RobotObservedObject)

CubeConnectionLost = _reflection.GeneratedProtocolMessageType('CubeConnectionLost', (_message.Message,), {
  'DESCRIPTOR' : _CUBECONNECTIONLOST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CubeConnectionLost)
  })
_sym_db.RegisterMessage(CubeConnectionLost)

DeleteCustomObjectsRequest = _reflection.GeneratedProtocolMessageType('DeleteCustomObjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECUSTOMOBJECTSREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.DeleteCustomObjectsRequest)
  })
_sym_db.RegisterMessage(DeleteCustomObjectsRequest)

DeleteCustomObjectsResponse = _reflection.GeneratedProtocolMessageType('DeleteCustomObjectsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETECUSTOMOBJECTSRESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.DeleteCustomObjectsResponse)
  })
_sym_db.RegisterMessage(DeleteCustomObjectsResponse)

CreateFixedCustomObjectRequest = _reflection.GeneratedProtocolMessageType('CreateFixedCustomObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFIXEDCUSTOMOBJECTREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CreateFixedCustomObjectRequest)
  })
_sym_db.RegisterMessage(CreateFixedCustomObjectRequest)

CreateFixedCustomObjectResponse = _reflection.GeneratedProtocolMessageType('CreateFixedCustomObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFIXEDCUSTOMOBJECTRESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CreateFixedCustomObjectResponse)
  })
_sym_db.RegisterMessage(CreateFixedCustomObjectResponse)

CustomBoxDefinition = _reflection.GeneratedProtocolMessageType('CustomBoxDefinition', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMBOXDEFINITION,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CustomBoxDefinition)
  })
_sym_db.RegisterMessage(CustomBoxDefinition)

CustomCubeDefinition = _reflection.GeneratedProtocolMessageType('CustomCubeDefinition', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMCUBEDEFINITION,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CustomCubeDefinition)
  })
_sym_db.RegisterMessage(CustomCubeDefinition)

CustomWallDefinition = _reflection.GeneratedProtocolMessageType('CustomWallDefinition', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMWALLDEFINITION,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.CustomWallDefinition)
  })
_sym_db.RegisterMessage(CustomWallDefinition)

DefineCustomObjectRequest = _reflection.GeneratedProtocolMessageType('DefineCustomObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEFINECUSTOMOBJECTREQUEST,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.DefineCustomObjectRequest)
  })
_sym_db.RegisterMessage(DefineCustomObjectRequest)

DefineCustomObjectResponse = _reflection.GeneratedProtocolMessageType('DefineCustomObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEFINECUSTOMOBJECTRESPONSE,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.DefineCustomObjectResponse)
  })
_sym_db.RegisterMessage(DefineCustomObjectResponse)

ObjectEvent = _reflection.GeneratedProtocolMessageType('ObjectEvent', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTEVENT,
  '__module__' : 'cube_pb2'
  # @@protoc_insertion_point(class_scope:Anki.Vector.external_interface.ObjectEvent)
  })
_sym_db.RegisterMessage(ObjectEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CUSTOMTYPE._options = None
  _CUSTOMTYPE._serialized_options = b'\020\001'
  _OBJECTFAMILY._options = None
  _OBJECTFAMILY._serialized_options = b'\020\001'
  _CUSTOMOBJECTMARKER._options = None
  _CUSTOMOBJECTMARKER._serialized_options = b'\020\001'
  _ROBOTOBSERVEDOBJECT.fields_by_name['object_family']._options = None
  _ROBOTOBSERVEDOBJECT.fields_by_name['object_family']._serialized_options = b'\030\001'
  _OBJECTTYPE._serialized_start=4823
  _OBJECTTYPE._serialized_end=4946
  _CUSTOMTYPE._serialized_start=4949
  _CUSTOMTYPE._serialized_end=5413
  _OBJECTFAMILY._serialized_start=5416
  _OBJECTFAMILY._serialized_end=5558
  _UPAXIS._serialized_start=5561
  _UPAXIS._serialized_end=5697
  _OBJECTCONSTANTS._serialized_start=5699
  _OBJECTCONSTANTS._serialized_end=5779
  _CUSTOMOBJECTMARKER._serialized_start=5782
  _CUSTOMOBJECTMARKER._serialized_end=6338
  _CUSTOMOBJECTDELETIONMODE._serialized_start=6341
  _CUSTOMOBJECTDELETIONMODE._serialized_end=6505
  _CONNECTCUBEREQUEST._serialized_start=85
  _CONNECTCUBEREQUEST._serialized_end=105
  _CONNECTCUBERESPONSE._serialized_start=108
  _CONNECTCUBERESPONSE._serialized_end=249
  _CUBESAVAILABLEREQUEST._serialized_start=251
  _CUBESAVAILABLEREQUEST._serialized_end=274
  _CUBESAVAILABLERESPONSE._serialized_start=276
  _CUBESAVAILABLERESPONSE._serialized_end=385
  _DISCONNECTCUBEREQUEST._serialized_start=387
  _DISCONNECTCUBEREQUEST._serialized_end=410
  _DISCONNECTCUBERESPONSE._serialized_start=412
  _DISCONNECTCUBERESPONSE._serialized_end=500
  _FLASHCUBELIGHTSREQUEST._serialized_start=502
  _FLASHCUBELIGHTSREQUEST._serialized_end=526
  _FLASHCUBELIGHTSRESPONSE._serialized_start=528
  _FLASHCUBELIGHTSRESPONSE._serialized_end=617
  _FORGETPREFERREDCUBEREQUEST._serialized_start=619
  _FORGETPREFERREDCUBEREQUEST._serialized_end=647
  _FORGETPREFERREDCUBERESPONSE._serialized_start=649
  _FORGETPREFERREDCUBERESPONSE._serialized_end=742
  _SETPREFERREDCUBEREQUEST._serialized_start=744
  _SETPREFERREDCUBEREQUEST._serialized_end=789
  _SETPREFERREDCUBERESPONSE._serialized_start=791
  _SETPREFERREDCUBERESPONSE._serialized_end=881
  _SETCUBELIGHTSREQUEST._serialized_start=884
  _SETCUBELIGHTSREQUEST._serialized_end=1316
  _SETCUBELIGHTSREQUEST_MAKERELATIVEMODE._serialized_start=1248
  _SETCUBELIGHTSREQUEST_MAKERELATIVEMODE._serialized_end=1316
  _SETCUBELIGHTSRESPONSE._serialized_start=1318
  _SETCUBELIGHTSRESPONSE._serialized_end=1405
  _OBJECTAVAILABLE._serialized_start=1407
  _OBJECTAVAILABLE._serialized_end=1444
  _OBJECTCONNECTIONSTATE._serialized_start=1447
  _OBJECTCONNECTIONSTATE._serialized_end=1593
  _OBJECTMOVED._serialized_start=1595
  _OBJECTMOVED._serialized_end=1646
  _OBJECTSTOPPEDMOVING._serialized_start=1648
  _OBJECTSTOPPEDMOVING._serialized_end=1707
  _OBJECTUPAXISCHANGED._serialized_start=1709
  _OBJECTUPAXISCHANGED._serialized_end=1825
  _OBJECTTAPPED._serialized_start=1827
  _OBJECTTAPPED._serialized_end=1879
  _ROBOTOBSERVEDOBJECT._serialized_start=1882
  _ROBOTOBSERVEDOBJECT._serialized_end=2250
  _CUBECONNECTIONLOST._serialized_start=2252
  _CUBECONNECTIONLOST._serialized_end=2272
  _DELETECUSTOMOBJECTSREQUEST._serialized_start=2274
  _DELETECUSTOMOBJECTSREQUEST._serialized_end=2374
  _DELETECUSTOMOBJECTSRESPONSE._serialized_start=2376
  _DELETECUSTOMOBJECTSRESPONSE._serialized_end=2469
  _CREATEFIXEDCUSTOMOBJECTREQUEST._serialized_start=2472
  _CREATEFIXEDCUSTOMOBJECTREQUEST._serialized_end=2619
  _CREATEFIXEDCUSTOMOBJECTRESPONSE._serialized_start=2621
  _CREATEFIXEDCUSTOMOBJECTRESPONSE._serialized_end=2737
  _CUSTOMBOXDEFINITION._serialized_start=2740
  _CUSTOMBOXDEFINITION._serialized_end=3310
  _CUSTOMCUBEDEFINITION._serialized_start=3313
  _CUSTOMCUBEDEFINITION._serialized_end=3471
  _CUSTOMWALLDEFINITION._serialized_start=3474
  _CUSTOMWALLDEFINITION._serialized_end=3652
  _DEFINECUSTOMOBJECTREQUEST._serialized_start=3655
  _DEFINECUSTOMOBJECTREQUEST._serialized_end=4023
  _DEFINECUSTOMOBJECTRESPONSE._serialized_start=4025
  _DEFINECUSTOMOBJECTRESPONSE._serialized_end=4134
  _OBJECTEVENT._serialized_start=4137
  _OBJECTEVENT._serialized_end=4821
# @@protoc_insertion_point(module_scope)
