# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serialize.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fserialize.proto\x12\x08NodeNote\"\x98\x01\n\x11PortSerialization\x12\x0f\n\x07port_id\x18\x01 \x01(\x03\x12\x11\n\tport_type\x18\x02 \x01(\x05\x12\x12\n\nport_truth\x18\x03 \x01(\x08\x12\x10\n\x08pipes_id\x18\x04 \x03(\x03\x12\x12\n\nport_width\x18\x05 \x01(\x02\x12\x12\n\nport_color\x18\x06 \x03(\x03\x12\x11\n\tport_flag\x18\x07 \x03(\x08\"\x80+\n\x11ViewSerialization\x12K\n\x13scene_serialization\x18\x01 \x03(\x0b\x32..NodeNote.ViewSerialization.SceneSerialization\x12\x18\n\x10\x63urrent_scene_id\x18\x02 \x01(\x03\x12\x17\n\nimage_path\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x14\x61ll_attr_font_family\x18\x06 \x01(\t\x12\x1a\n\x12\x61ll_attr_font_size\x18\x07 \x01(\x05\x12\x16\n\x0e\x61ll_attr_color\x18\x08 \x03(\x03\x12\x17\n\x0f\x61ll_logic_color\x18\t \x03(\x03\x12\x16\n\x0e\x61ll_pipe_width\x18\n \x01(\x02\x12\x16\n\x0e\x61ll_pipe_color\x18\x0b \x03(\x03\x12\x16\n\x0e\x61ll_port_width\x18\x0c \x01(\x02\x12\x16\n\x0e\x61ll_port_color\x18\r \x03(\x03\x12\x16\n\x0e\x61ll_draw_width\x18\x0e \x01(\x02\x12\x16\n\x0e\x61ll_draw_color\x18\x0f \x01(\x03\x12\x17\n\ntext_width\x18\x10 \x01(\x01H\x01\x88\x01\x01\x12\x16\n\tline_flag\x18\x11 \x01(\x08H\x02\x88\x01\x01\x12\x16\n\tundo_flag\x18\x12 \x01(\x08H\x03\x88\x01\x01\x12!\n\x14\x61ll_pipe_font_family\x18\x13 \x01(\tH\x04\x88\x01\x01\x12\x1f\n\x12\x61ll_pipe_font_size\x18\x14 \x01(\x05H\x05\x88\x01\x01\x12\x19\n\x0c\x66lowing_flag\x18\x15 \x01(\x08H\x06\x88\x01\x01\x12!\n\x14\x61ll_background_image\x18\x16 \x01(\tH\x07\x88\x01\x01\x12\x17\n\nstyle_path\x18\x17 \x01(\tH\x08\x88\x01\x01\x1a\xe8$\n\x12SceneSerialization\x12\x10\n\x08scene_id\x18\x01 \x01(\x03\x12\\\n\x12\x61ttr_serialization\x18\x02 \x03(\x0b\x32@.NodeNote.ViewSerialization.SceneSerialization.AttrSerialization\x12^\n\x13logic_serialization\x18\x03 \x03(\x0b\x32\x41.NodeNote.ViewSerialization.SceneSerialization.LogicSerialization\x12\\\n\x12pipe_serialization\x18\x04 \x03(\x0b\x32@.NodeNote.ViewSerialization.SceneSerialization.PipeSerialization\x12\\\n\x12\x64raw_serialization\x18\x05 \x03(\x0b\x32@.NodeNote.ViewSerialization.SceneSerialization.DrawSerialization\x12\x18\n\x10\x62\x61\x63kground_image\x18\x06 \x01(\t\x12#\n\x16scene_attr_font_family\x18\x07 \x01(\tH\x00\x88\x01\x01\x12!\n\x14scene_attr_font_size\x18\x08 \x01(\x05H\x01\x88\x01\x01\x12(\n\x1bscene_attr_style_font_color\x18\t \x01(\x03H\x02\x88\x01\x01\x12.\n!scene_attr_style_background_color\x18\n \x01(\x03H\x03\x88\x01\x01\x12\x37\n*scene_attr_style_selected_background_color\x18\x0b \x01(\x03H\x04\x88\x01\x01\x12*\n\x1dscene_attr_style_border_color\x18\x0c \x01(\x03H\x05\x88\x01\x01\x12\x33\n&scene_attr_style_selected_border_color\x18\r \x01(\x03H\x06\x88\x01\x01\x12/\n\"scene_logic_style_background_color\x18\x0e \x01(\x03H\x07\x88\x01\x01\x12\x38\n+scene_logic_style_selected_background_color\x18\x0f \x01(\x03H\x08\x88\x01\x01\x12+\n\x1escene_logic_style_border_color\x18\x10 \x01(\x03H\t\x88\x01\x01\x12\x34\n\'scene_logic_style_selected_border_color\x18\x11 \x01(\x03H\n\x88\x01\x01\x12\x1d\n\x10scene_pipe_width\x18\x12 \x01(\x02H\x0b\x88\x01\x01\x12.\n!scene_pipe_style_background_color\x18\x13 \x01(\x03H\x0c\x88\x01\x01\x12\x37\n*scene_pipe_style_selected_background_color\x18\x14 \x01(\x03H\r\x88\x01\x01\x12\x18\n\x10scene_port_width\x18\x15 \x01(\x02\x12#\n\x16scene_port_style_color\x18\x16 \x01(\x03H\x0e\x88\x01\x01\x12*\n\x1dscene_port_style_border_color\x18\x17 \x01(\x03H\x0f\x88\x01\x01\x12+\n\x1escene_port_style_hovered_color\x18\x18 \x01(\x03H\x10\x88\x01\x01\x12\x32\n%scene_port_style_hovered_border_color\x18\x19 \x01(\x03H\x11\x88\x01\x01\x12-\n scene_port_style_activated_color\x18\x1a \x01(\x03H\x12\x88\x01\x01\x12\x34\n\'scene_port_style_activated_border_color\x18\x1b \x01(\x03H\x13\x88\x01\x01\x12\x0e\n\x01x\x18\x1c \x01(\x02H\x14\x88\x01\x01\x12\x0e\n\x01y\x18\x1d \x01(\x02H\x15\x88\x01\x01\x12\x12\n\x05width\x18\x1e \x01(\x02H\x16\x88\x01\x01\x12\x13\n\x06height\x18\x1f \x01(\x02H\x17\x88\x01\x01\x12#\n\x16scene_pipe_font_family\x18  \x01(\tH\x18\x88\x01\x01\x12!\n\x14scene_pipe_font_size\x18! \x01(\x05H\x19\x88\x01\x01\x12\"\n\x15scene_pipe_font_color\x18\" \x01(\x03H\x1a\x88\x01\x01\x12\"\n\x15\x62\x61\x63kground_image_flag\x18# \x01(\x08H\x1b\x88\x01\x01\x1a\x9a\x0b\n\x11\x41ttrSerialization\x12\x0f\n\x07\x61ttr_id\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x03(\x02\x12\x10\n\x08position\x18\x03 \x03(\x02\x12\x10\n\x08\x63ontents\x18\x04 \x01(\t\x12.\n\tattr_port\x18\x05 \x03(\x0b\x32\x1b.NodeNote.PortSerialization\x12\x14\n\x0cnext_attr_id\x18\x06 \x03(\x03\x12\x15\n\rnext_logic_id\x18\x07 \x03(\x03\x12\x14\n\x0clast_attr_id\x18\x08 \x03(\x03\x12\x15\n\rlast_logic_id\x18\t \x03(\x03\x12\x10\n\x08sub_attr\x18\n \x03(\x03\x12n\n\x12\x66ile_serialization\x18\x0b \x03(\x0b\x32R.NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.FileSerialization\x12t\n\x15subview_serialization\x18\x0c \x03(\x0b\x32U.NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.SubviewSerialization\x12n\n\x12todo_serialization\x18\r \x03(\x0b\x32R.NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.TodoSerialization\x12n\n\x12none_serialization\x18\x0e \x03(\x0b\x32R.NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.NoneSerialization\x12O\n\x17sub_scene_serialization\x18\x0f \x03(\x0b\x32..NodeNote.ViewSerialization.SceneSerialization\x12\x13\n\x0bhighlighter\x18\x10 \x01(\x08\x12\x15\n\rattr_location\x18\x11 \x03(\x05\x12\x15\n\rnext_location\x18\x12 \x03(\x05\x12\x1d\n\x15self_attr_font_family\x18\x13 \x01(\t\x12\x1b\n\x13self_attr_font_size\x18\x14 \x01(\x05\x12\x17\n\x0fself_attr_color\x18\x15 \x03(\x03\x12\x11\n\tattr_flag\x18\x16 \x03(\x08\x12\x17\n\nmouse_flag\x18\x17 \x01(\x08H\x00\x88\x01\x01\x12\x1d\n\x10mouse_text_width\x18\x18 \x01(\x01H\x01\x88\x01\x01\x1at\n\x11\x46ileSerialization\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\x03\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\r\n\x05\x63over\x18\x03 \x01(\t\x12\x11\n\x04\x66ile\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x15\n\rfile_location\x18\x05 \x03(\x05\x42\x07\n\x05_file\x1a\x80\x01\n\x14SubviewSerialization\x12\x12\n\nsubview_id\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x03(\x02\x12\x18\n\x10subview_location\x18\x03 \x03(\x05\x12,\n\x07subview\x18\x04 \x03(\x0b\x32\x1b.NodeNote.ViewSerialization\x1aW\n\x11TodoSerialization\x12\x0f\n\x07todo_id\x18\x01 \x01(\x03\x12\x0c\n\x04task\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x02\x12\x15\n\rtodo_location\x18\x04 \x03(\x05\x1a\x36\n\x11NoneSerialization\x12\x0f\n\x07none_id\x18\x01 \x01(\x03\x12\x10\n\x08none_pos\x18\x02 \x03(\x05\x42\r\n\x0b_mouse_flagB\x13\n\x11_mouse_text_width\x1a\x93\x02\n\x12LogicSerialization\x12\x10\n\x08logic_id\x18\x01 \x01(\x03\x12\x16\n\x0elogic_position\x18\x02 \x03(\x02\x12\x13\n\x0blogic_truth\x18\x03 \x03(\x05\x12/\n\nlogic_port\x18\x04 \x03(\x0b\x32\x1b.NodeNote.PortSerialization\x12\x17\n\x0flogic_next_attr\x18\x05 \x03(\x03\x12\x18\n\x10logic_next_logic\x18\x06 \x03(\x03\x12\x17\n\x0flogic_last_attr\x18\x07 \x03(\x03\x12\x18\n\x10logic_last_logic\x18\x08 \x03(\x03\x12\x13\n\x0blogic_color\x18\t \x03(\x03\x12\x12\n\nlogic_flag\x18\n \x03(\x08\x1a\x99\x03\n\x11PipeSerialization\x12\x0f\n\x07pipe_id\x18\x01 \x01(\x03\x12\x14\n\x0cpipe_port_id\x18\x02 \x03(\x03\x12\x11\n\tpipe_text\x18\x03 \x01(\t\x12\x13\n\x0bstart_point\x18\x04 \x03(\x02\x12\x11\n\tend_point\x18\x05 \x03(\x02\x12\x1a\n\x12source_move_status\x18\x06 \x01(\x08\x12\x1f\n\x17\x64\x65stination_move_status\x18\x07 \x01(\x08\x12\x1a\n\x12offset_start_point\x18\x08 \x03(\x02\x12 \n\x18offset_destination_point\x18\t \x03(\x02\x12\x17\n\x0fself_pipe_width\x18\n \x01(\x02\x12\x17\n\x0fself_pipe_color\x18\x0b \x03(\x03\x12\x11\n\tpipe_flag\x18\x0c \x03(\x08\x12\x1d\n\x10pipe_font_family\x18\x0f \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0epipe_font_size\x18\x10 \x01(\x05H\x01\x88\x01\x01\x42\x13\n\x11_pipe_font_familyB\x11\n\x0f_pipe_font_size\x1aW\n\x11\x44rawSerialization\x12\x0f\n\x07\x64raw_id\x18\x01 \x01(\x03\x12\x11\n\tdraw_size\x18\x02 \x03(\x02\x12\x10\n\x08\x64raw_pos\x18\x03 \x03(\x02\x12\x0c\n\x04path\x18\x04 \x01(\tB\x19\n\x17_scene_attr_font_familyB\x17\n\x15_scene_attr_font_sizeB\x1e\n\x1c_scene_attr_style_font_colorB$\n\"_scene_attr_style_background_colorB-\n+_scene_attr_style_selected_background_colorB \n\x1e_scene_attr_style_border_colorB)\n\'_scene_attr_style_selected_border_colorB%\n#_scene_logic_style_background_colorB.\n,_scene_logic_style_selected_background_colorB!\n\x1f_scene_logic_style_border_colorB*\n(_scene_logic_style_selected_border_colorB\x13\n\x11_scene_pipe_widthB$\n\"_scene_pipe_style_background_colorB-\n+_scene_pipe_style_selected_background_colorB\x19\n\x17_scene_port_style_colorB \n\x1e_scene_port_style_border_colorB!\n\x1f_scene_port_style_hovered_colorB(\n&_scene_port_style_hovered_border_colorB#\n!_scene_port_style_activated_colorB*\n(_scene_port_style_activated_border_colorB\x04\n\x02_xB\x04\n\x02_yB\x08\n\x06_widthB\t\n\x07_heightB\x19\n\x17_scene_pipe_font_familyB\x17\n\x15_scene_pipe_font_sizeB\x18\n\x16_scene_pipe_font_colorB\x18\n\x16_background_image_flagB\r\n\x0b_image_pathB\r\n\x0b_text_widthB\x0c\n\n_line_flagB\x0c\n\n_undo_flagB\x17\n\x15_all_pipe_font_familyB\x15\n\x13_all_pipe_font_sizeB\x0f\n\r_flowing_flagB\x17\n\x15_all_background_imageB\r\n\x0b_style_pathb\x06proto3')



_PORTSERIALIZATION = DESCRIPTOR.message_types_by_name['PortSerialization']
_VIEWSERIALIZATION = DESCRIPTOR.message_types_by_name['ViewSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION = _VIEWSERIALIZATION.nested_types_by_name['SceneSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION.nested_types_by_name['AttrSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_FILESERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION.nested_types_by_name['FileSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_SUBVIEWSERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION.nested_types_by_name['SubviewSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_TODOSERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION.nested_types_by_name['TodoSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_NONESERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION.nested_types_by_name['NoneSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_LOGICSERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION.nested_types_by_name['LogicSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_PIPESERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION.nested_types_by_name['PipeSerialization']
_VIEWSERIALIZATION_SCENESERIALIZATION_DRAWSERIALIZATION = _VIEWSERIALIZATION_SCENESERIALIZATION.nested_types_by_name['DrawSerialization']
PortSerialization = _reflection.GeneratedProtocolMessageType('PortSerialization', (_message.Message,), {
  'DESCRIPTOR' : _PORTSERIALIZATION,
  '__module__' : 'serialize_pb2'
  # @@protoc_insertion_point(class_scope:NodeNote.PortSerialization)
  })
_sym_db.RegisterMessage(PortSerialization)

ViewSerialization = _reflection.GeneratedProtocolMessageType('ViewSerialization', (_message.Message,), {

  'SceneSerialization' : _reflection.GeneratedProtocolMessageType('SceneSerialization', (_message.Message,), {

    'AttrSerialization' : _reflection.GeneratedProtocolMessageType('AttrSerialization', (_message.Message,), {

      'FileSerialization' : _reflection.GeneratedProtocolMessageType('FileSerialization', (_message.Message,), {
        'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_FILESERIALIZATION,
        '__module__' : 'serialize_pb2'
        # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.FileSerialization)
        })
      ,

      'SubviewSerialization' : _reflection.GeneratedProtocolMessageType('SubviewSerialization', (_message.Message,), {
        'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_SUBVIEWSERIALIZATION,
        '__module__' : 'serialize_pb2'
        # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.SubviewSerialization)
        })
      ,

      'TodoSerialization' : _reflection.GeneratedProtocolMessageType('TodoSerialization', (_message.Message,), {
        'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_TODOSERIALIZATION,
        '__module__' : 'serialize_pb2'
        # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.TodoSerialization)
        })
      ,

      'NoneSerialization' : _reflection.GeneratedProtocolMessageType('NoneSerialization', (_message.Message,), {
        'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_NONESERIALIZATION,
        '__module__' : 'serialize_pb2'
        # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.AttrSerialization.NoneSerialization)
        })
      ,
      'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION,
      '__module__' : 'serialize_pb2'
      # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.AttrSerialization)
      })
    ,

    'LogicSerialization' : _reflection.GeneratedProtocolMessageType('LogicSerialization', (_message.Message,), {
      'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_LOGICSERIALIZATION,
      '__module__' : 'serialize_pb2'
      # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.LogicSerialization)
      })
    ,

    'PipeSerialization' : _reflection.GeneratedProtocolMessageType('PipeSerialization', (_message.Message,), {
      'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_PIPESERIALIZATION,
      '__module__' : 'serialize_pb2'
      # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.PipeSerialization)
      })
    ,

    'DrawSerialization' : _reflection.GeneratedProtocolMessageType('DrawSerialization', (_message.Message,), {
      'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION_DRAWSERIALIZATION,
      '__module__' : 'serialize_pb2'
      # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization.DrawSerialization)
      })
    ,
    'DESCRIPTOR' : _VIEWSERIALIZATION_SCENESERIALIZATION,
    '__module__' : 'serialize_pb2'
    # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization.SceneSerialization)
    })
  ,
  'DESCRIPTOR' : _VIEWSERIALIZATION,
  '__module__' : 'serialize_pb2'
  # @@protoc_insertion_point(class_scope:NodeNote.ViewSerialization)
  })
_sym_db.RegisterMessage(ViewSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.AttrSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.AttrSerialization.FileSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.AttrSerialization.SubviewSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.AttrSerialization.TodoSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.AttrSerialization.NoneSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.LogicSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.PipeSerialization)
_sym_db.RegisterMessage(ViewSerialization.SceneSerialization.DrawSerialization)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PORTSERIALIZATION._serialized_start=30
  _PORTSERIALIZATION._serialized_end=182
  _VIEWSERIALIZATION._serialized_start=185
  _VIEWSERIALIZATION._serialized_end=5689
  _VIEWSERIALIZATION_SCENESERIALIZATION._serialized_start=814
  _VIEWSERIALIZATION_SCENESERIALIZATION._serialized_end=5526
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION._serialized_start=2439
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION._serialized_end=3873
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_FILESERIALIZATION._serialized_start=3445
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_FILESERIALIZATION._serialized_end=3561
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_SUBVIEWSERIALIZATION._serialized_start=3564
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_SUBVIEWSERIALIZATION._serialized_end=3692
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_TODOSERIALIZATION._serialized_start=3694
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_TODOSERIALIZATION._serialized_end=3781
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_NONESERIALIZATION._serialized_start=3783
  _VIEWSERIALIZATION_SCENESERIALIZATION_ATTRSERIALIZATION_NONESERIALIZATION._serialized_end=3837
  _VIEWSERIALIZATION_SCENESERIALIZATION_LOGICSERIALIZATION._serialized_start=3876
  _VIEWSERIALIZATION_SCENESERIALIZATION_LOGICSERIALIZATION._serialized_end=4151
  _VIEWSERIALIZATION_SCENESERIALIZATION_PIPESERIALIZATION._serialized_start=4154
  _VIEWSERIALIZATION_SCENESERIALIZATION_PIPESERIALIZATION._serialized_end=4563
  _VIEWSERIALIZATION_SCENESERIALIZATION_DRAWSERIALIZATION._serialized_start=4565
  _VIEWSERIALIZATION_SCENESERIALIZATION_DRAWSERIALIZATION._serialized_end=4652
# @@protoc_insertion_point(module_scope)
