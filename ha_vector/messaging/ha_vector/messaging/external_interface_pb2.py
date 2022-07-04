# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ha_vector/messaging/external_interface.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ha_vector.messaging import behavior_pb2 as ha__vector_dot_messaging_dot_behavior__pb2
from ha_vector.messaging import cube_pb2 as ha__vector_dot_messaging_dot_cube__pb2
from ha_vector.messaging import messages_pb2 as ha__vector_dot_messaging_dot_messages__pb2
from ha_vector.messaging import nav_map_pb2 as ha__vector_dot_messaging_dot_nav__map__pb2
from ha_vector.messaging import shared_pb2 as ha__vector_dot_messaging_dot_shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,ha_vector/messaging/external_interface.proto\x12\x1e\x41nki.Vector.external_interface\x1a\x1cgoogle/api/annotations.proto\x1a\"ha_vector/messaging/behavior.proto\x1a\x1eha_vector/messaging/cube.proto\x1a\"ha_vector/messaging/messages.proto\x1a!ha_vector/messaging/nav_map.proto\x1a ha_vector/messaging/shared.proto*o\n\x0fProtocolVersion\x12\x1c\n\x18PROTOCOL_VERSION_UNKNOWN\x10\x00\x12\x1c\n\x18PROTOCOL_VERSION_MINIMUM\x10\x00\x12\x1c\n\x18PROTOCOL_VERSION_CURRENT\x10\x05\x1a\x02\x10\x01\x32\xddT\n\x11\x45xternalInterface\x12\xa3\x01\n\x0fProtocolVersion\x12\x36.Anki.Vector.external_interface.ProtocolVersionRequest\x1a\x37.Anki.Vector.external_interface.ProtocolVersionResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/v1/protocol_version:\x01*\x12\xab\x01\n\x11SDKInitialization\x12\x38.Anki.Vector.external_interface.SDKInitializationRequest\x1a\x39.Anki.Vector.external_interface.SDKInitializationResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/sdk_initialization:\x01*\x12x\n\x0b\x44riveWheels\x12\x32.Anki.Vector.external_interface.DriveWheelsRequest\x1a\x33.Anki.Vector.external_interface.DriveWheelsResponse\"\x00\x12\x8c\x01\n\x14PlayAnimationTrigger\x12;.Anki.Vector.external_interface.PlayAnimationTriggerRequest\x1a\x35.Anki.Vector.external_interface.PlayAnimationResponse\"\x00\x12~\n\rPlayAnimation\x12\x34.Anki.Vector.external_interface.PlayAnimationRequest\x1a\x35.Anki.Vector.external_interface.PlayAnimationResponse\"\x00\x12\x9f\x01\n\x0eListAnimations\x12\x35.Anki.Vector.external_interface.ListAnimationsRequest\x1a\x36.Anki.Vector.external_interface.ListAnimationsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/list_animations:\x01*\x12\xbc\x01\n\x15ListAnimationTriggers\x12<.Anki.Vector.external_interface.ListAnimationTriggersRequest\x1a=.Anki.Vector.external_interface.ListAnimationTriggersResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/list_animation_triggers:\x01*\x12o\n\x08MoveHead\x12/.Anki.Vector.external_interface.MoveHeadRequest\x1a\x30.Anki.Vector.external_interface.MoveHeadResponse\"\x00\x12o\n\x08MoveLift\x12/.Anki.Vector.external_interface.MoveLiftRequest\x1a\x30.Anki.Vector.external_interface.MoveLiftResponse\"\x00\x12~\n\rStopAllMotors\x12\x34.Anki.Vector.external_interface.StopAllMotorsRequest\x1a\x35.Anki.Vector.external_interface.StopAllMotorsResponse\"\x00\x12\xb5\x01\n\x13\x44isplayFaceImageRGB\x12:.Anki.Vector.external_interface.DisplayFaceImageRGBRequest\x1a;.Anki.Vector.external_interface.DisplayFaceImageRGBResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/display_face_image_rgb:\x01*\x12\x9d\x01\n\x0b\x45ventStream\x12,.Anki.Vector.external_interface.EventRequest\x1a-.Anki.Vector.external_interface.EventResponse\"/\x82\xd3\xe4\x93\x02)\"\x10/v1/event_stream:\x01*Z\x12\x12\x10/v1/event_stream0\x01\x12\x9c\x01\n\x1b\x45xternalAudioStreamPlayback\x12:.Anki.Vector.external_interface.ExternalAudioStreamRequest\x1a;.Anki.Vector.external_interface.ExternalAudioStreamResponse\"\x00(\x01\x30\x01\x12\x88\x01\n\x0f\x42\x65haviorControl\x12\x36.Anki.Vector.external_interface.BehaviorControlRequest\x1a\x37.Anki.Vector.external_interface.BehaviorControlResponse\"\x00(\x01\x30\x01\x12\xb2\x01\n\x15\x41ssumeBehaviorControl\x12\x36.Anki.Vector.external_interface.BehaviorControlRequest\x1a\x37.Anki.Vector.external_interface.BehaviorControlResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/assume_behavior_control:\x01*0\x01\x12\xb8\x01\n\x14\x43\x61ncelFaceEnrollment\x12;.Anki.Vector.external_interface.CancelFaceEnrollmentRequest\x1a<.Anki.Vector.external_interface.CancelFaceEnrollmentResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/cancel_face_enrollment:\x01*\x12\xb8\x01\n\x14RequestEnrolledNames\x12;.Anki.Vector.external_interface.RequestEnrolledNamesRequest\x1a<.Anki.Vector.external_interface.RequestEnrolledNamesResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/request_enrolled_names:\x01*\x12\xc2\x01\n\x16UpdateEnrolledFaceByID\x12=.Anki.Vector.external_interface.UpdateEnrolledFaceByIDRequest\x1a>.Anki.Vector.external_interface.UpdateEnrolledFaceByIDResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/v1/update_enrolled_face_by_id:\x01*\x12\xbe\x01\n\x15\x45raseEnrolledFaceByID\x12<.Anki.Vector.external_interface.EraseEnrolledFaceByIDRequest\x1a=.Anki.Vector.external_interface.EraseEnrolledFaceByIDResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/v1/erase_enrolled_face_by_id:\x01*\x12\xbd\x01\n\x15\x45raseAllEnrolledFaces\x12<.Anki.Vector.external_interface.EraseAllEnrolledFacesRequest\x1a=.Anki.Vector.external_interface.EraseAllEnrolledFacesResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v1/erase_all_enrolled_faces:\x01*\x12\xa5\x01\n\x0fSetFaceToEnroll\x12\x36.Anki.Vector.external_interface.SetFaceToEnrollRequest\x1a\x37.Anki.Vector.external_interface.SetFaceToEnrollResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/set_face_to_enroll:\x01*\x12\xbc\x01\n\x15\x45nableMarkerDetection\x12<.Anki.Vector.external_interface.EnableMarkerDetectionRequest\x1a=.Anki.Vector.external_interface.EnableMarkerDetectionResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/enable_marker_detection:\x01*\x12\xb4\x01\n\x13\x45nableFaceDetection\x12:.Anki.Vector.external_interface.EnableFaceDetectionRequest\x1a;.Anki.Vector.external_interface.EnableFaceDetectionResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/enable_face_detection:\x01*\x12\xbc\x01\n\x15\x45nableMotionDetection\x12<.Anki.Vector.external_interface.EnableMotionDetectionRequest\x1a=.Anki.Vector.external_interface.EnableMotionDetectionResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/enable_motion_detection:\x01*\x12\xa8\x01\n\x10\x45nableMirrorMode\x12\x37.Anki.Vector.external_interface.EnableMirrorModeRequest\x1a\x38.Anki.Vector.external_interface.EnableMirrorModeResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/enable_mirror_mode:\x01*\x12\xb8\x01\n\x14\x45nableImageStreaming\x12;.Anki.Vector.external_interface.EnableImageStreamingRequest\x1a<.Anki.Vector.external_interface.EnableImageStreamingResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/enable_image_streaming:\x01*\x12\xc5\x01\n\x17IsImageStreamingEnabled\x12>.Anki.Vector.external_interface.IsImageStreamingEnabledRequest\x1a?.Anki.Vector.external_interface.IsImageStreamingEnabledResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/v1/is_image_streaming_enabled:\x01*\x12\xb6\x01\n\x13\x43\x61ncelActionByIdTag\x12:.Anki.Vector.external_interface.CancelActionByIdTagRequest\x1a;.Anki.Vector.external_interface.CancelActionByIdTagResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/cancel_action_by_id_tag:\x01*\x12\x88\x01\n\x08GoToPose\x12/.Anki.Vector.external_interface.GoToPoseRequest\x1a\x30.Anki.Vector.external_interface.GoToPoseResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/go_to_pose:\x01*\x12\x98\x01\n\x0c\x44ockWithCube\x12\x33.Anki.Vector.external_interface.DockWithCubeRequest\x1a\x34.Anki.Vector.external_interface.DockWithCubeResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/dock_with_cube:\x01*\x12\xa4\x01\n\x0f\x44riveOffCharger\x12\x36.Anki.Vector.external_interface.DriveOffChargerRequest\x1a\x37.Anki.Vector.external_interface.DriveOffChargerResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1/drive_off_charger:\x01*\x12\xa0\x01\n\x0e\x44riveOnCharger\x12\x35.Anki.Vector.external_interface.DriveOnChargerRequest\x1a\x36.Anki.Vector.external_interface.DriveOnChargerResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/v1/drive_on_charger:\x01*\x12\x8b\x01\n\tFindFaces\x12\x30.Anki.Vector.external_interface.FindFacesRequest\x1a\x31.Anki.Vector.external_interface.FindFacesResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/find_faces:\x01*\x12\xad\x01\n\x11LookAroundInPlace\x12\x38.Anki.Vector.external_interface.LookAroundInPlaceRequest\x1a\x39.Anki.Vector.external_interface.LookAroundInPlaceResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/look_around_in_place:\x01*\x12\x8b\x01\n\tRollBlock\x12\x30.Anki.Vector.external_interface.RollBlockRequest\x1a\x31.Anki.Vector.external_interface.RollBlockResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/roll_block:\x01*\x12\x8f\x01\n\nPhotosInfo\x12\x31.Anki.Vector.external_interface.PhotosInfoRequest\x1a\x32.Anki.Vector.external_interface.PhotosInfoResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/photos_info:\x01*\x12z\n\x05Photo\x12,.Anki.Vector.external_interface.PhotoRequest\x1a-.Anki.Vector.external_interface.PhotoResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\"\t/v1/photo:\x01*\x12\x8a\x01\n\tThumbnail\x12\x30.Anki.Vector.external_interface.ThumbnailRequest\x1a\x31.Anki.Vector.external_interface.ThumbnailResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v1/thumbnail:\x01*\x12\x93\x01\n\x0b\x44\x65letePhoto\x12\x32.Anki.Vector.external_interface.DeletePhotoRequest\x1a\x33.Anki.Vector.external_interface.DeletePhotoResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/delete_photo:\x01*\x12~\n\rDriveStraight\x12\x34.Anki.Vector.external_interface.DriveStraightRequest\x1a\x35.Anki.Vector.external_interface.DriveStraightResponse\"\x00\x12x\n\x0bTurnInPlace\x12\x32.Anki.Vector.external_interface.TurnInPlaceRequest\x1a\x33.Anki.Vector.external_interface.TurnInPlaceResponse\"\x00\x12{\n\x0cSetHeadAngle\x12\x33.Anki.Vector.external_interface.SetHeadAngleRequest\x1a\x34.Anki.Vector.external_interface.SetHeadAngleResponse\"\x00\x12~\n\rSetLiftHeight\x12\x34.Anki.Vector.external_interface.SetLiftHeightRequest\x1a\x35.Anki.Vector.external_interface.SetLiftHeightResponse\"\x00\x12\x84\x01\n\x0fTurnTowardsFace\x12\x36.Anki.Vector.external_interface.TurnTowardsFaceRequest\x1a\x37.Anki.Vector.external_interface.TurnTowardsFaceResponse\"\x00\x12u\n\nGoToObject\x12\x31.Anki.Vector.external_interface.GoToObjectRequest\x1a\x32.Anki.Vector.external_interface.GoToObjectResponse\"\x00\x12u\n\nRollObject\x12\x31.Anki.Vector.external_interface.RollObjectRequest\x1a\x32.Anki.Vector.external_interface.RollObjectResponse\"\x00\x12x\n\x0bPopAWheelie\x12\x32.Anki.Vector.external_interface.PopAWheelieRequest\x1a\x33.Anki.Vector.external_interface.PopAWheelieResponse\"\x00\x12{\n\x0cPickupObject\x12\x33.Anki.Vector.external_interface.PickupObjectRequest\x1a\x34.Anki.Vector.external_interface.PickupObjectResponse\"\x00\x12\x9c\x01\n\x17PlaceObjectOnGroundHere\x12>.Anki.Vector.external_interface.PlaceObjectOnGroundHereRequest\x1a?.Anki.Vector.external_interface.PlaceObjectOnGroundHereResponse\"\x00\x12~\n\x0fSetMasterVolume\x12\x33.Anki.Vector.external_interface.MasterVolumeRequest\x1a\x34.Anki.Vector.external_interface.MasterVolumeResponse\"\x00\x12\xaf\x01\n\x12UserAuthentication\x12\x39.Anki.Vector.external_interface.UserAuthenticationRequest\x1a:.Anki.Vector.external_interface.UserAuthenticationResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/user_authentication:\x01*\x12\x97\x01\n\x0c\x42\x61tteryState\x12\x33.Anki.Vector.external_interface.BatteryStateRequest\x1a\x34.Anki.Vector.external_interface.BatteryStateResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/battery_state:\x01*\x12\x97\x01\n\x0cVersionState\x12\x33.Anki.Vector.external_interface.VersionStateRequest\x1a\x34.Anki.Vector.external_interface.VersionStateResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/version_state:\x01*\x12\x83\x01\n\x07SayText\x12..Anki.Vector.external_interface.SayTextRequest\x1a/.Anki.Vector.external_interface.SayTextResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/say_text:\x01*\x12\x93\x01\n\x0b\x43onnectCube\x12\x32.Anki.Vector.external_interface.ConnectCubeRequest\x1a\x33.Anki.Vector.external_interface.ConnectCubeResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/connect_cube:\x01*\x12\x9f\x01\n\x0e\x44isconnectCube\x12\x35.Anki.Vector.external_interface.DisconnectCubeRequest\x1a\x36.Anki.Vector.external_interface.DisconnectCubeResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/disconnect_cube:\x01*\x12\x9f\x01\n\x0e\x43ubesAvailable\x12\x35.Anki.Vector.external_interface.CubesAvailableRequest\x1a\x36.Anki.Vector.external_interface.CubesAvailableResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/cubes_available:\x01*\x12\xa4\x01\n\x0f\x46lashCubeLights\x12\x36.Anki.Vector.external_interface.FlashCubeLightsRequest\x1a\x37.Anki.Vector.external_interface.FlashCubeLightsResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1/flash_cube_lights:\x01*\x12\xb4\x01\n\x13\x46orgetPreferredCube\x12:.Anki.Vector.external_interface.ForgetPreferredCubeRequest\x1a;.Anki.Vector.external_interface.ForgetPreferredCubeResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/forget_preferred_cube:\x01*\x12\xa8\x01\n\x10SetPreferredCube\x12\x37.Anki.Vector.external_interface.SetPreferredCubeRequest\x1a\x38.Anki.Vector.external_interface.SetPreferredCubeResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/set_preferred_cube:\x01*\x12\xb4\x01\n\x13\x44\x65leteCustomObjects\x12:.Anki.Vector.external_interface.DeleteCustomObjectsRequest\x1a;.Anki.Vector.external_interface.DeleteCustomObjectsResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/delete_custom_objects:\x01*\x12\xc5\x01\n\x17\x43reateFixedCustomObject\x12>.Anki.Vector.external_interface.CreateFixedCustomObjectRequest\x1a?.Anki.Vector.external_interface.CreateFixedCustomObjectResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/v1/create_fixed_custom_object:\x01*\x12\xb0\x01\n\x12\x44\x65\x66ineCustomObject\x12\x39.Anki.Vector.external_interface.DefineCustomObjectRequest\x1a:.Anki.Vector.external_interface.DefineCustomObjectResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/define_custom_object:\x01*\x12~\n\rSetCubeLights\x12\x34.Anki.Vector.external_interface.SetCubeLightsRequest\x1a\x35.Anki.Vector.external_interface.SetCubeLightsResponse\"\x00\x12\x8d\x01\n\tAudioFeed\x12\x30.Anki.Vector.external_interface.AudioFeedRequest\x1a\x31.Anki.Vector.external_interface.AudioFeedResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/audio_feed:\x01*0\x01\x12\x91\x01\n\nCameraFeed\x12\x31.Anki.Vector.external_interface.CameraFeedRequest\x1a\x32.Anki.Vector.external_interface.CameraFeedResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/camera_feed:\x01*0\x01\x12\xb0\x01\n\x12\x43\x61ptureSingleImage\x12\x39.Anki.Vector.external_interface.CaptureSingleImageRequest\x1a:.Anki.Vector.external_interface.CaptureSingleImageResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/capture_single_image:\x01*\x12\x94\x01\n\x0bSetEyeColor\x12\x32.Anki.Vector.external_interface.SetEyeColorRequest\x1a\x33.Anki.Vector.external_interface.SetEyeColorResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/set_eye_color:\x01*\x12\x92\x01\n\nNavMapFeed\x12\x31.Anki.Vector.external_interface.NavMapFeedRequest\x1a\x32.Anki.Vector.external_interface.NavMapFeedResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/nav_map_feed:\x01*0\x01\x62\x06proto3')

_PROTOCOLVERSION = DESCRIPTOR.enum_types_by_name['ProtocolVersion']
ProtocolVersion = enum_type_wrapper.EnumTypeWrapper(_PROTOCOLVERSION)
PROTOCOL_VERSION_UNKNOWN = 0
PROTOCOL_VERSION_MINIMUM = 0
PROTOCOL_VERSION_CURRENT = 5


_EXTERNALINTERFACE = DESCRIPTOR.services_by_name['ExternalInterface']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROTOCOLVERSION._options = None
  _PROTOCOLVERSION._serialized_options = b'\020\001'
  _EXTERNALINTERFACE.methods_by_name['ProtocolVersion']._options = None
  _EXTERNALINTERFACE.methods_by_name['ProtocolVersion']._serialized_options = b'\202\323\344\223\002\031\"\024/v1/protocol_version:\001*'
  _EXTERNALINTERFACE.methods_by_name['SDKInitialization']._options = None
  _EXTERNALINTERFACE.methods_by_name['SDKInitialization']._serialized_options = b'\202\323\344\223\002\033\"\026/v1/sdk_initialization:\001*'
  _EXTERNALINTERFACE.methods_by_name['ListAnimations']._options = None
  _EXTERNALINTERFACE.methods_by_name['ListAnimations']._serialized_options = b'\202\323\344\223\002\030\"\023/v1/list_animations:\001*'
  _EXTERNALINTERFACE.methods_by_name['ListAnimationTriggers']._options = None
  _EXTERNALINTERFACE.methods_by_name['ListAnimationTriggers']._serialized_options = b'\202\323\344\223\002 \"\033/v1/list_animation_triggers:\001*'
  _EXTERNALINTERFACE.methods_by_name['DisplayFaceImageRGB']._options = None
  _EXTERNALINTERFACE.methods_by_name['DisplayFaceImageRGB']._serialized_options = b'\202\323\344\223\002\037\"\032/v1/display_face_image_rgb:\001*'
  _EXTERNALINTERFACE.methods_by_name['EventStream']._options = None
  _EXTERNALINTERFACE.methods_by_name['EventStream']._serialized_options = b'\202\323\344\223\002)\"\020/v1/event_stream:\001*Z\022\022\020/v1/event_stream'
  _EXTERNALINTERFACE.methods_by_name['AssumeBehaviorControl']._options = None
  _EXTERNALINTERFACE.methods_by_name['AssumeBehaviorControl']._serialized_options = b'\202\323\344\223\002 \"\033/v1/assume_behavior_control:\001*'
  _EXTERNALINTERFACE.methods_by_name['CancelFaceEnrollment']._options = None
  _EXTERNALINTERFACE.methods_by_name['CancelFaceEnrollment']._serialized_options = b'\202\323\344\223\002\037\"\032/v1/cancel_face_enrollment:\001*'
  _EXTERNALINTERFACE.methods_by_name['RequestEnrolledNames']._options = None
  _EXTERNALINTERFACE.methods_by_name['RequestEnrolledNames']._serialized_options = b'\202\323\344\223\002\037\"\032/v1/request_enrolled_names:\001*'
  _EXTERNALINTERFACE.methods_by_name['UpdateEnrolledFaceByID']._options = None
  _EXTERNALINTERFACE.methods_by_name['UpdateEnrolledFaceByID']._serialized_options = b'\202\323\344\223\002#\"\036/v1/update_enrolled_face_by_id:\001*'
  _EXTERNALINTERFACE.methods_by_name['EraseEnrolledFaceByID']._options = None
  _EXTERNALINTERFACE.methods_by_name['EraseEnrolledFaceByID']._serialized_options = b'\202\323\344\223\002\"\"\035/v1/erase_enrolled_face_by_id:\001*'
  _EXTERNALINTERFACE.methods_by_name['EraseAllEnrolledFaces']._options = None
  _EXTERNALINTERFACE.methods_by_name['EraseAllEnrolledFaces']._serialized_options = b'\202\323\344\223\002!\"\034/v1/erase_all_enrolled_faces:\001*'
  _EXTERNALINTERFACE.methods_by_name['SetFaceToEnroll']._options = None
  _EXTERNALINTERFACE.methods_by_name['SetFaceToEnroll']._serialized_options = b'\202\323\344\223\002\033\"\026/v1/set_face_to_enroll:\001*'
  _EXTERNALINTERFACE.methods_by_name['EnableMarkerDetection']._options = None
  _EXTERNALINTERFACE.methods_by_name['EnableMarkerDetection']._serialized_options = b'\202\323\344\223\002 \"\033/v1/enable_marker_detection:\001*'
  _EXTERNALINTERFACE.methods_by_name['EnableFaceDetection']._options = None
  _EXTERNALINTERFACE.methods_by_name['EnableFaceDetection']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/enable_face_detection:\001*'
  _EXTERNALINTERFACE.methods_by_name['EnableMotionDetection']._options = None
  _EXTERNALINTERFACE.methods_by_name['EnableMotionDetection']._serialized_options = b'\202\323\344\223\002 \"\033/v1/enable_motion_detection:\001*'
  _EXTERNALINTERFACE.methods_by_name['EnableMirrorMode']._options = None
  _EXTERNALINTERFACE.methods_by_name['EnableMirrorMode']._serialized_options = b'\202\323\344\223\002\033\"\026/v1/enable_mirror_mode:\001*'
  _EXTERNALINTERFACE.methods_by_name['EnableImageStreaming']._options = None
  _EXTERNALINTERFACE.methods_by_name['EnableImageStreaming']._serialized_options = b'\202\323\344\223\002\037\"\032/v1/enable_image_streaming:\001*'
  _EXTERNALINTERFACE.methods_by_name['IsImageStreamingEnabled']._options = None
  _EXTERNALINTERFACE.methods_by_name['IsImageStreamingEnabled']._serialized_options = b'\202\323\344\223\002#\"\036/v1/is_image_streaming_enabled:\001*'
  _EXTERNALINTERFACE.methods_by_name['CancelActionByIdTag']._options = None
  _EXTERNALINTERFACE.methods_by_name['CancelActionByIdTag']._serialized_options = b'\202\323\344\223\002 \"\033/v1/cancel_action_by_id_tag:\001*'
  _EXTERNALINTERFACE.methods_by_name['GoToPose']._options = None
  _EXTERNALINTERFACE.methods_by_name['GoToPose']._serialized_options = b'\202\323\344\223\002\023\"\016/v1/go_to_pose:\001*'
  _EXTERNALINTERFACE.methods_by_name['DockWithCube']._options = None
  _EXTERNALINTERFACE.methods_by_name['DockWithCube']._serialized_options = b'\202\323\344\223\002\027\"\022/v1/dock_with_cube:\001*'
  _EXTERNALINTERFACE.methods_by_name['DriveOffCharger']._options = None
  _EXTERNALINTERFACE.methods_by_name['DriveOffCharger']._serialized_options = b'\202\323\344\223\002\032\"\025/v1/drive_off_charger:\001*'
  _EXTERNALINTERFACE.methods_by_name['DriveOnCharger']._options = None
  _EXTERNALINTERFACE.methods_by_name['DriveOnCharger']._serialized_options = b'\202\323\344\223\002\031\"\024/v1/drive_on_charger:\001*'
  _EXTERNALINTERFACE.methods_by_name['FindFaces']._options = None
  _EXTERNALINTERFACE.methods_by_name['FindFaces']._serialized_options = b'\202\323\344\223\002\023\"\016/v1/find_faces:\001*'
  _EXTERNALINTERFACE.methods_by_name['LookAroundInPlace']._options = None
  _EXTERNALINTERFACE.methods_by_name['LookAroundInPlace']._serialized_options = b'\202\323\344\223\002\035\"\030/v1/look_around_in_place:\001*'
  _EXTERNALINTERFACE.methods_by_name['RollBlock']._options = None
  _EXTERNALINTERFACE.methods_by_name['RollBlock']._serialized_options = b'\202\323\344\223\002\023\"\016/v1/roll_block:\001*'
  _EXTERNALINTERFACE.methods_by_name['PhotosInfo']._options = None
  _EXTERNALINTERFACE.methods_by_name['PhotosInfo']._serialized_options = b'\202\323\344\223\002\024\"\017/v1/photos_info:\001*'
  _EXTERNALINTERFACE.methods_by_name['Photo']._options = None
  _EXTERNALINTERFACE.methods_by_name['Photo']._serialized_options = b'\202\323\344\223\002\016\"\t/v1/photo:\001*'
  _EXTERNALINTERFACE.methods_by_name['Thumbnail']._options = None
  _EXTERNALINTERFACE.methods_by_name['Thumbnail']._serialized_options = b'\202\323\344\223\002\022\"\r/v1/thumbnail:\001*'
  _EXTERNALINTERFACE.methods_by_name['DeletePhoto']._options = None
  _EXTERNALINTERFACE.methods_by_name['DeletePhoto']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/delete_photo:\001*'
  _EXTERNALINTERFACE.methods_by_name['UserAuthentication']._options = None
  _EXTERNALINTERFACE.methods_by_name['UserAuthentication']._serialized_options = b'\202\323\344\223\002\034\"\027/v1/user_authentication:\001*'
  _EXTERNALINTERFACE.methods_by_name['BatteryState']._options = None
  _EXTERNALINTERFACE.methods_by_name['BatteryState']._serialized_options = b'\202\323\344\223\002\026\"\021/v1/battery_state:\001*'
  _EXTERNALINTERFACE.methods_by_name['VersionState']._options = None
  _EXTERNALINTERFACE.methods_by_name['VersionState']._serialized_options = b'\202\323\344\223\002\026\"\021/v1/version_state:\001*'
  _EXTERNALINTERFACE.methods_by_name['SayText']._options = None
  _EXTERNALINTERFACE.methods_by_name['SayText']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/say_text:\001*'
  _EXTERNALINTERFACE.methods_by_name['ConnectCube']._options = None
  _EXTERNALINTERFACE.methods_by_name['ConnectCube']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/connect_cube:\001*'
  _EXTERNALINTERFACE.methods_by_name['DisconnectCube']._options = None
  _EXTERNALINTERFACE.methods_by_name['DisconnectCube']._serialized_options = b'\202\323\344\223\002\030\"\023/v1/disconnect_cube:\001*'
  _EXTERNALINTERFACE.methods_by_name['CubesAvailable']._options = None
  _EXTERNALINTERFACE.methods_by_name['CubesAvailable']._serialized_options = b'\202\323\344\223\002\030\"\023/v1/cubes_available:\001*'
  _EXTERNALINTERFACE.methods_by_name['FlashCubeLights']._options = None
  _EXTERNALINTERFACE.methods_by_name['FlashCubeLights']._serialized_options = b'\202\323\344\223\002\032\"\025/v1/flash_cube_lights:\001*'
  _EXTERNALINTERFACE.methods_by_name['ForgetPreferredCube']._options = None
  _EXTERNALINTERFACE.methods_by_name['ForgetPreferredCube']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/forget_preferred_cube:\001*'
  _EXTERNALINTERFACE.methods_by_name['SetPreferredCube']._options = None
  _EXTERNALINTERFACE.methods_by_name['SetPreferredCube']._serialized_options = b'\202\323\344\223\002\033\"\026/v1/set_preferred_cube:\001*'
  _EXTERNALINTERFACE.methods_by_name['DeleteCustomObjects']._options = None
  _EXTERNALINTERFACE.methods_by_name['DeleteCustomObjects']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/delete_custom_objects:\001*'
  _EXTERNALINTERFACE.methods_by_name['CreateFixedCustomObject']._options = None
  _EXTERNALINTERFACE.methods_by_name['CreateFixedCustomObject']._serialized_options = b'\202\323\344\223\002#\"\036/v1/create_fixed_custom_object:\001*'
  _EXTERNALINTERFACE.methods_by_name['DefineCustomObject']._options = None
  _EXTERNALINTERFACE.methods_by_name['DefineCustomObject']._serialized_options = b'\202\323\344\223\002\035\"\030/v1/define_custom_object:\001*'
  _EXTERNALINTERFACE.methods_by_name['AudioFeed']._options = None
  _EXTERNALINTERFACE.methods_by_name['AudioFeed']._serialized_options = b'\202\323\344\223\002\023\"\016/v1/audio_feed:\001*'
  _EXTERNALINTERFACE.methods_by_name['CameraFeed']._options = None
  _EXTERNALINTERFACE.methods_by_name['CameraFeed']._serialized_options = b'\202\323\344\223\002\024\"\017/v1/camera_feed:\001*'
  _EXTERNALINTERFACE.methods_by_name['CaptureSingleImage']._options = None
  _EXTERNALINTERFACE.methods_by_name['CaptureSingleImage']._serialized_options = b'\202\323\344\223\002\035\"\030/v1/capture_single_image:\001*'
  _EXTERNALINTERFACE.methods_by_name['SetEyeColor']._options = None
  _EXTERNALINTERFACE.methods_by_name['SetEyeColor']._serialized_options = b'\202\323\344\223\002\026\"\021/v1/set_eye_color:\001*'
  _EXTERNALINTERFACE.methods_by_name['NavMapFeed']._options = None
  _EXTERNALINTERFACE.methods_by_name['NavMapFeed']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/nav_map_feed:\001*'
  _PROTOCOLVERSION._serialized_start=283
  _PROTOCOLVERSION._serialized_end=394
  _EXTERNALINTERFACE._serialized_start=397
  _EXTERNALINTERFACE._serialized_end=11242
# @@protoc_insertion_point(module_scope)
