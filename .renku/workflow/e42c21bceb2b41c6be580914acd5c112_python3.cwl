arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_costfactors.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: '0.2'
    inputBinding:
      position: 10
      prefix: --cpccf_step
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_100:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff3.0/best/input/pars.txt
    inputBinding:
      position: 100
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_101:
    default:
      class: File
      path: ../../data/fPAR/fpar_howard_v5.txt
    inputBinding:
      position: 101
      prefix: --fpar1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_102:
    default:
      class: File
      path: ../../data/fPAR/fpar_litchfield_v5.txt
    inputBinding:
      position: 102
      prefix: --fpar2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_103:
    default:
      class: File
      path: ../../data/fPAR/fpar_adelaide_v5.txt
    inputBinding:
      position: 103
      prefix: --fpar3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_104:
    default:
      class: File
      path: ../../data/fPAR/fpar_daly_v5.txt
    inputBinding:
      position: 104
      prefix: --fpar4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_105:
    default:
      class: File
      path: ../../data/fPAR/fpar_dry_v5.txt
    inputBinding:
      position: 105
      prefix: --fpar5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_106:
    default:
      class: File
      path: ../../data/fPAR/fpar_sturt_v5.txt
    inputBinding:
      position: 106
      prefix: --fpar6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_107:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 107
      prefix: --fpar_dates
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_108:
    default: data/img/6_cpcff.png
    inputBinding:
      position: 108
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff0.2/best/input/pars.txt
    inputBinding:
      position: 11
      prefix: --in1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff0.4/best/input/pars.txt
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff0.6/best/input/pars.txt
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff0.8/best/input/pars.txt
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.2/best/input/pars.txt
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.4/best/input/pars.txt
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.6/best/input/pars.txt
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.8/best/input/pars.txt
    inputBinding:
      position: 19
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default: Howard Springs
    inputBinding:
      position: 2
      prefix: --sites
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_20:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff2.0/best/input/pars.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff2.2/best/input/pars.txt
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff2.4/best/input/pars.txt
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff2.6/best/input/pars.txt
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff2.8/best/input/pars.txt
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff3.0/best/input/pars.txt
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff0.2/best/input/pars.txt
    inputBinding:
      position: 26
      prefix: --in2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff0.4/best/input/pars.txt
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff0.6/best/input/pars.txt
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff0.8/best/input/pars.txt
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: Litchfield
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_30:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_31:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff1.2/best/input/pars.txt
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_32:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff1.4/best/input/pars.txt
    inputBinding:
      position: 32
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff1.6/best/input/pars.txt
    inputBinding:
      position: 33
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff1.8/best/input/pars.txt
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff2.0/best/input/pars.txt
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_36:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff2.2/best/input/pars.txt
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff2.4/best/input/pars.txt
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_38:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff2.6/best/input/pars.txt
    inputBinding:
      position: 38
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_39:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff2.8/best/input/pars.txt
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: Adelaide River
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_40:
    default:
      class: File
      path: ../../work/Litchfield/freedrainage_cpcff3.0/best/input/pars.txt
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_41:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff0.2/best/input/pars.txt
    inputBinding:
      position: 41
      prefix: --in3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_42:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff0.4/best/input/pars.txt
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_43:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff0.6/best/input/pars.txt
    inputBinding:
      position: 43
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_44:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff0.8/best/input/pars.txt
    inputBinding:
      position: 44
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_45:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 45
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_46:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff1.2/best/input/pars.txt
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_47:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff1.4/best/input/pars.txt
    inputBinding:
      position: 47
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_48:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff1.6/best/input/pars.txt
    inputBinding:
      position: 48
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_49:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff1.8/best/input/pars.txt
    inputBinding:
      position: 49
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default: Daly Uncleared
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_50:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff2.0/best/input/pars.txt
    inputBinding:
      position: 50
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_51:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff2.2/best/input/pars.txt
    inputBinding:
      position: 51
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_52:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff2.4/best/input/pars.txt
    inputBinding:
      position: 52
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_53:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff2.6/best/input/pars.txt
    inputBinding:
      position: 53
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_54:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff2.8/best/input/pars.txt
    inputBinding:
      position: 54
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_55:
    default:
      class: File
      path: ../../work/AdelaideRiver/freedrainage_cpcff3.0/best/input/pars.txt
    inputBinding:
      position: 55
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_56:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff0.2/best/input/pars.txt
    inputBinding:
      position: 56
      prefix: --in4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_57:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff0.4/best/input/pars.txt
    inputBinding:
      position: 57
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_58:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff0.6/best/input/pars.txt
    inputBinding:
      position: 58
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_59:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff0.8/best/input/pars.txt
    inputBinding:
      position: 59
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: Dry River
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_60:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 60
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_61:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff1.2/best/input/pars.txt
    inputBinding:
      position: 61
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_62:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff1.4/best/input/pars.txt
    inputBinding:
      position: 62
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_63:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff1.6/best/input/pars.txt
    inputBinding:
      position: 63
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_64:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff1.8/best/input/pars.txt
    inputBinding:
      position: 64
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_65:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff2.0/best/input/pars.txt
    inputBinding:
      position: 65
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_66:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff2.2/best/input/pars.txt
    inputBinding:
      position: 66
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_67:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff2.4/best/input/pars.txt
    inputBinding:
      position: 67
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_68:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff2.6/best/input/pars.txt
    inputBinding:
      position: 68
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_69:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff2.8/best/input/pars.txt
    inputBinding:
      position: 69
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default: Sturt Plains
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_70:
    default:
      class: File
      path: ../../work/DalyUncleared/freedrainage_cpcff3.0/best/input/pars.txt
    inputBinding:
      position: 70
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_71:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff0.2/best/input/pars.txt
    inputBinding:
      position: 71
      prefix: --in5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_72:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff0.4/best/input/pars.txt
    inputBinding:
      position: 72
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_73:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff0.6/best/input/pars.txt
    inputBinding:
      position: 73
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_74:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff0.8/best/input/pars.txt
    inputBinding:
      position: 74
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_75:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 75
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_76:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff1.2/best/input/pars.txt
    inputBinding:
      position: 76
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_77:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff1.4/best/input/pars.txt
    inputBinding:
      position: 77
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_78:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff1.6/best/input/pars.txt
    inputBinding:
      position: 78
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_79:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff1.8/best/input/pars.txt
    inputBinding:
      position: 79
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default: '0.2'
    inputBinding:
      position: 8
      prefix: --cpccf_min
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_80:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff2.0/best/input/pars.txt
    inputBinding:
      position: 80
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_81:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff2.2/best/input/pars.txt
    inputBinding:
      position: 81
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_82:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff2.4/best/input/pars.txt
    inputBinding:
      position: 82
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_83:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff2.6/best/input/pars.txt
    inputBinding:
      position: 83
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_84:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff2.8/best/input/pars.txt
    inputBinding:
      position: 84
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_85:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff3.0/best/input/pars.txt
    inputBinding:
      position: 85
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_86:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff0.2/best/input/pars.txt
    inputBinding:
      position: 86
      prefix: --in6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_87:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff0.4/best/input/pars.txt
    inputBinding:
      position: 87
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_88:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff0.6/best/input/pars.txt
    inputBinding:
      position: 88
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_89:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff0.8/best/input/pars.txt
    inputBinding:
      position: 89
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: '3.0'
    inputBinding:
      position: 9
      prefix: --cpccf_max
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_90:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 90
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_91:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff1.2/best/input/pars.txt
    inputBinding:
      position: 91
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_92:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff1.4/best/input/pars.txt
    inputBinding:
      position: 92
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_93:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff1.6/best/input/pars.txt
    inputBinding:
      position: 93
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_94:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff1.8/best/input/pars.txt
    inputBinding:
      position: 94
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_95:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff2.0/best/input/pars.txt
    inputBinding:
      position: 95
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_96:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff2.2/best/input/pars.txt
    inputBinding:
      position: 96
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_97:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff2.4/best/input/pars.txt
    inputBinding:
      position: 97
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_98:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff2.6/best/input/pars.txt
    inputBinding:
      position: 98
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_99:
    default:
      class: File
      path: ../../work/SturtPlains/freedrainage_cpcff2.8/best/input/pars.txt
    inputBinding:
      position: 99
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_108)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/img
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_costfactors.py
    writable: false
  - entry: $(inputs.input_11)
    entryname: work/HowardSprings/freedrainage_cpcff0.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: work/HowardSprings/freedrainage_cpcff0.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_13)
    entryname: work/HowardSprings/freedrainage_cpcff0.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: work/HowardSprings/freedrainage_cpcff0.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: work/HowardSprings/freedrainage_cpcff1.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_17)
    entryname: work/HowardSprings/freedrainage_cpcff1.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_18)
    entryname: work/HowardSprings/freedrainage_cpcff1.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_19)
    entryname: work/HowardSprings/freedrainage_cpcff1.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: work/HowardSprings/freedrainage_cpcff2.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: work/HowardSprings/freedrainage_cpcff2.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: work/HowardSprings/freedrainage_cpcff2.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: work/HowardSprings/freedrainage_cpcff2.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: work/HowardSprings/freedrainage_cpcff2.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: work/HowardSprings/freedrainage_cpcff3.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_26)
    entryname: work/Litchfield/freedrainage_cpcff0.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_27)
    entryname: work/Litchfield/freedrainage_cpcff0.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_28)
    entryname: work/Litchfield/freedrainage_cpcff0.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_29)
    entryname: work/Litchfield/freedrainage_cpcff0.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_30)
    entryname: work/Litchfield/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_31)
    entryname: work/Litchfield/freedrainage_cpcff1.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_32)
    entryname: work/Litchfield/freedrainage_cpcff1.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_33)
    entryname: work/Litchfield/freedrainage_cpcff1.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_34)
    entryname: work/Litchfield/freedrainage_cpcff1.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_35)
    entryname: work/Litchfield/freedrainage_cpcff2.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_36)
    entryname: work/Litchfield/freedrainage_cpcff2.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_37)
    entryname: work/Litchfield/freedrainage_cpcff2.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_38)
    entryname: work/Litchfield/freedrainage_cpcff2.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_39)
    entryname: work/Litchfield/freedrainage_cpcff2.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_40)
    entryname: work/Litchfield/freedrainage_cpcff3.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_41)
    entryname: work/AdelaideRiver/freedrainage_cpcff0.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_42)
    entryname: work/AdelaideRiver/freedrainage_cpcff0.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_43)
    entryname: work/AdelaideRiver/freedrainage_cpcff0.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_44)
    entryname: work/AdelaideRiver/freedrainage_cpcff0.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_45)
    entryname: work/AdelaideRiver/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_46)
    entryname: work/AdelaideRiver/freedrainage_cpcff1.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_47)
    entryname: work/AdelaideRiver/freedrainage_cpcff1.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_48)
    entryname: work/AdelaideRiver/freedrainage_cpcff1.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_49)
    entryname: work/AdelaideRiver/freedrainage_cpcff1.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_50)
    entryname: work/AdelaideRiver/freedrainage_cpcff2.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_51)
    entryname: work/AdelaideRiver/freedrainage_cpcff2.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_52)
    entryname: work/AdelaideRiver/freedrainage_cpcff2.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_53)
    entryname: work/AdelaideRiver/freedrainage_cpcff2.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_54)
    entryname: work/AdelaideRiver/freedrainage_cpcff2.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_55)
    entryname: work/AdelaideRiver/freedrainage_cpcff3.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_56)
    entryname: work/DalyUncleared/freedrainage_cpcff0.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_57)
    entryname: work/DalyUncleared/freedrainage_cpcff0.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_58)
    entryname: work/DalyUncleared/freedrainage_cpcff0.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_59)
    entryname: work/DalyUncleared/freedrainage_cpcff0.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_60)
    entryname: work/DalyUncleared/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_61)
    entryname: work/DalyUncleared/freedrainage_cpcff1.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_62)
    entryname: work/DalyUncleared/freedrainage_cpcff1.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_63)
    entryname: work/DalyUncleared/freedrainage_cpcff1.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_64)
    entryname: work/DalyUncleared/freedrainage_cpcff1.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_65)
    entryname: work/DalyUncleared/freedrainage_cpcff2.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_66)
    entryname: work/DalyUncleared/freedrainage_cpcff2.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_67)
    entryname: work/DalyUncleared/freedrainage_cpcff2.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_68)
    entryname: work/DalyUncleared/freedrainage_cpcff2.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_69)
    entryname: work/DalyUncleared/freedrainage_cpcff2.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_70)
    entryname: work/DalyUncleared/freedrainage_cpcff3.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_71)
    entryname: work/DryRiver/freedrainage_cpcff0.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_72)
    entryname: work/DryRiver/freedrainage_cpcff0.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_73)
    entryname: work/DryRiver/freedrainage_cpcff0.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_74)
    entryname: work/DryRiver/freedrainage_cpcff0.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_75)
    entryname: work/DryRiver/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_76)
    entryname: work/DryRiver/freedrainage_cpcff1.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_77)
    entryname: work/DryRiver/freedrainage_cpcff1.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_78)
    entryname: work/DryRiver/freedrainage_cpcff1.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_79)
    entryname: work/DryRiver/freedrainage_cpcff1.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_80)
    entryname: work/DryRiver/freedrainage_cpcff2.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_81)
    entryname: work/DryRiver/freedrainage_cpcff2.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_82)
    entryname: work/DryRiver/freedrainage_cpcff2.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_83)
    entryname: work/DryRiver/freedrainage_cpcff2.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_84)
    entryname: work/DryRiver/freedrainage_cpcff2.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_85)
    entryname: work/DryRiver/freedrainage_cpcff3.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_86)
    entryname: work/SturtPlains/freedrainage_cpcff0.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_87)
    entryname: work/SturtPlains/freedrainage_cpcff0.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_88)
    entryname: work/SturtPlains/freedrainage_cpcff0.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_89)
    entryname: work/SturtPlains/freedrainage_cpcff0.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_90)
    entryname: work/SturtPlains/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_91)
    entryname: work/SturtPlains/freedrainage_cpcff1.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_92)
    entryname: work/SturtPlains/freedrainage_cpcff1.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_93)
    entryname: work/SturtPlains/freedrainage_cpcff1.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_94)
    entryname: work/SturtPlains/freedrainage_cpcff1.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_95)
    entryname: work/SturtPlains/freedrainage_cpcff2.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_96)
    entryname: work/SturtPlains/freedrainage_cpcff2.2/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_97)
    entryname: work/SturtPlains/freedrainage_cpcff2.4/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_98)
    entryname: work/SturtPlains/freedrainage_cpcff2.6/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_99)
    entryname: work/SturtPlains/freedrainage_cpcff2.8/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_100)
    entryname: work/SturtPlains/freedrainage_cpcff3.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_101)
    entryname: data/fPAR/fpar_howard_v5.txt
    writable: false
  - entry: $(inputs.input_102)
    entryname: data/fPAR/fpar_litchfield_v5.txt
    writable: false
  - entry: $(inputs.input_103)
    entryname: data/fPAR/fpar_adelaide_v5.txt
    writable: false
  - entry: $(inputs.input_104)
    entryname: data/fPAR/fpar_daly_v5.txt
    writable: false
  - entry: $(inputs.input_105)
    entryname: data/fPAR/fpar_dry_v5.txt
    writable: false
  - entry: $(inputs.input_106)
    entryname: data/fPAR/fpar_sturt_v5.txt
    writable: false
  - entry: $(inputs.input_107)
    entryname: data/fPAR/dates_v5
    writable: false
successCodes: []
temporaryFailCodes: []
